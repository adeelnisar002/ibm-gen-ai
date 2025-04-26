# AI Meeting Companion

This project provides a set of tools for speech-to-text transcription and text analysis using Groq's AI services. It includes both simple command-line utilities and a web interface for audio transcription.

## Features

- Speech-to-text transcription using Groq's Whisper model
- Text analysis using Groq's Gemma2-9b-it model
- Web interface for easy audio file transcription
- Command-line utilities for quick transcription and text analysis

## Models Used

### Speech-to-Text: Whisper Large v3
- **Purpose**: Audio transcription
- **Model**: `whisper-large-v3`
- **Features**: 
  - High-accuracy speech recognition
  - Supports multiple languages
  - Handles various audio formats
  - Provides detailed transcription with timestamps

### Text Analysis: Gemma2-9b-it
- **Purpose**: Text summarization and key point extraction
- **Model**: `gemma2-9b-it`
- **Features**:
  - Instruction-tuned for better response quality
  - Capable of understanding and summarizing complex text
  - Generates structured and detailed responses
  - Optimized for inference speed

## Prerequisites

- Python 3.8 or higher
- Groq API key (Get it from [Groq's website](https://console.groq.com/))

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your Groq API key:
```bash
export GROQ_API_KEY='your-api-key-here'
```

## Usage

### Simple Speech-to-Text

```bash
python simple_speech2text.py
```
This will transcribe the audio file specified in the script.

### Simple LLM

```bash
python simple_llm.py
```
This will demonstrate the text analysis capabilities using Groq's Gemma2-9b-it model.

### Web Interface

```bash
python speech2text_app.py
```
This will launch a web interface at `http://localhost:7860` where you can upload audio files for transcription.

### Combined Speech Analysis

```bash
python speech_analyzer.py
```
This will launch a web interface that combines speech-to-text transcription with text analysis.

## Project Structure

- `simple_speech2text.py`: Basic speech-to-text transcription utility
- `simple_llm.py`: Basic text analysis utility
- `speech2text_app.py`: Web interface for speech-to-text transcription
- `speech_analyzer.py`: Combined web interface for transcription and analysis
