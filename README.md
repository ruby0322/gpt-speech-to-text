# GPT Speech to Text

一個使用 OpenAI Whisper API 將音訊檔轉換成文字的工具。支援長音訊自動分段處理，適合處理演講、課程等長時間錄音。

## 功能特點

- 支援多種音訊格式 (mp3, m4a 等)
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

## 檔案結構

- `transcribe.py`: 主程式
- `convert.py`: 音訊格式轉換工具
- `config.example.json`: API 設定範本
- `config.json`: 實際 API 設定（請勿提交到版本控制）
- `inputs/`: 輸入音訊檔案目錄
- `outputs/`: 輸出文字檔案目錄

## 注意事項

- 請確保 config.json 已正確設定 API Key
- 長音訊檔案會依據 chunk-size 分段處理
- 支援的輸入格式取決於 ffmpeg 支援的格式
