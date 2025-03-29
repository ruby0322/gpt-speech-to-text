import argparse
import json
import os

import openai
from pydub import AudioSegment
from pydub.utils import which

# Load configuration
try:
    with open('config.json') as f:
        config = json.load(f)
    api_key = config['openai_api_key']
except FileNotFoundError:
    print("Please create config.json file based on config.example.json")
    exit(1)

# Set your OpenAI API key
client = openai.OpenAI(api_key=api_key)
AudioSegment.converter = which("ffmpeg")


# Function to split the audio into chunks
def split_audio(audio, chunk_size_ms=60000):
    chunks = []
    for i in range(0, len(audio), chunk_size_ms):
        chunks.append(audio[i:i + chunk_size_ms])
    return chunks


def get_output_path(input_path, output_dir):
    # Get the base filename without extension
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    # Create output filename with .txt extension
    output_filename = f"{base_name}.txt"
    # Join with output directory
    return os.path.join(output_dir, output_filename)


def transcribe_audio(file_path, output_dir, chunk_size_ms=60000):
    try:
        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate output file path
        output_path = get_output_path(file_path, output_dir)
        
        print(f"Loading audio file: {file_path}")
        # Load the audio file
        audio = AudioSegment.from_file(file_path)

        # Split the audio into smaller chunks
        print(f"Splitting audio into chunks of {chunk_size_ms / 1000} seconds")
        audio_chunks = split_audio(audio, chunk_size_ms)

        transcription = ""
        for i, chunk in enumerate(audio_chunks):
            print(f"Processing chunk {i + 1}/{len(audio_chunks)}")

            # Save each chunk as a temporary file
            temp_audio_path = f'temp_audio_chunk_{i}.mp3'
            chunk.export(temp_audio_path, format='mp3')

            # Read the audio file
            audio_data = open(temp_audio_path, 'rb')

            # Remove temporary file
            os.remove(temp_audio_path)

            print(f"Sending chunk {i + 1} to OpenAI for transcription")
            # Send the audio data to OpenAI for transcription
            response = client.audio.transcriptions.create(
                file=audio_data, model="whisper-1", response_format="text")
            print(f'Chunk {i}:', response)

            # Extract the transcription text and append to the final transcription
            transcription += response + "\n"

        print(f"Saving transcription to {output_path}")
        # Save the transcription to a text file
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(transcription)

        print(f"Transcription saved successfully to {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Transcribe audio file to text using OpenAI Whisper API')
    parser.add_argument('input', help='Path to input audio file')
    parser.add_argument('--output_dir', default="./outputs", help='Directory path for output text file')
    parser.add_argument('--chunk-size', type=int, default=60000,
                      help='Chunk size in milliseconds (default: 60000)')
    
    args = parser.parse_args()

    transcribe_audio(args.input, args.output_dir, args.chunk_size)
    print(f"Transcription process completed.")
