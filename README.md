# GPT Speech to Text

[繁體中文](#繁體中文) | [简体中文](#简体中文) | [English](#english)

# 繁體中文

一個使用 OpenAI Whisper API 將音訊檔轉換成文字的工具。支援長音訊自動分段處理，適合處理演講、課程等長時間錄音。

## 功能特點

- 自動分段處理長音訊
- 輸出文字檔與輸入檔案同名
- 可自訂分段大小

## 安裝步驟

1. 安裝相依套件：
```bash
pip install openai pydub
```

2. 安裝 ffmpeg（必要）：
   - macOS: `brew install ffmpeg`
   - Ubuntu: `sudo apt-get install ffmpeg`
   - Windows: 從 [ffmpeg 官網](https://ffmpeg.org/download.html) 下載

3. 設定 OpenAI API Key：
```bash
cp config.example.json config.json
```
編輯 config.json，填入您的 OpenAI API Key

## 使用方法

基本使用：
```bash
python transcribe.py input.mp3
```

指定輸出目錄：
```bash
python transcribe.py input.mp3 --output_dir ./my_outputs
```

調整分段大小（預設 60 秒）：
```bash
python transcribe.py input.mp3 --chunk-size 30000
```

# 简体中文

一个使用 OpenAI Whisper API 将音频文件转换成文字的工具。支持长音频自动分段处理，适合处理演讲、课程等长时间录音。

## 功能特点

- 自动分段处理长音频
- 输出文字文件与输入文件同名
- 可自定义分段大小

## 安装步骤

1. 安装依赖包：
```bash
pip install openai pydub
```

2. 安装 ffmpeg（必要）：
   - macOS: `brew install ffmpeg`
   - Ubuntu: `sudo apt-get install ffmpeg`
   - Windows: 从 [ffmpeg 官网](https://ffmpeg.org/download.html) 下载

3. 设置 OpenAI API Key：
```bash
cp config.example.json config.json
```
编辑 config.json，填入您的 OpenAI API Key

## 使用方法

基本使用：
```bash
python transcribe.py input.mp3
```

指定输出目录：
```bash
python transcribe.py input.mp3 --output_dir ./my_outputs
```

调整分段大小（默认 60 秒）：
```bash
python transcribe.py input.mp3 --chunk-size 30000
```

# English

A tool that uses the OpenAI Whisper API to convert audio files to text. Supports automatic segmentation of long audio files, suitable for processing lectures, courses, and other long recordings.

## Features

- Automatic segmentation of long audio files
- Output text file name matches input file name
- Customizable segment size

## Installation

1. Install dependencies:
```bash
pip install openai pydub
```

2. Install ffmpeg (required):
   - macOS: `brew install ffmpeg`
   - Ubuntu: `sudo apt-get install ffmpeg`
   - Windows: Download from [ffmpeg website](https://ffmpeg.org/download.html)

3. Configure OpenAI API Key:
```bash
cp config.example.json config.json
```
Edit config.json and enter your OpenAI API Key

## Usage

Basic usage:
```bash
python transcribe.py input.mp3
```

Specify output directory:
```bash
python transcribe.py input.mp3 --output_dir ./my_outputs
```

Adjust chunk size (default 60 seconds):
```bash
python transcribe.py input.mp3 --chunk-size 30000
```
