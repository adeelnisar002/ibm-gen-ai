# AI Chatbot with BlenderBot

A conversational AI chatbot built using Flask and Facebook's BlenderBot model. This chatbot maintains conversation history and provides natural language responses through a web interface.

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and navigate to `http://localhost:5000`

## Features

- Web-based chat interface
- Conversation history tracking
- Powered by Facebook's BlenderBot (400M-distill model)
- Docker support included

## Models

- **BlenderBot-400M-distill**: A distilled version of Facebook's BlenderBot model, optimized for efficient inference while maintaining conversational capabilities
- **Tokenizer**: AutoTokenizer from Hugging Face's Transformers library for text processing

## API Usage

Send POST requests to `/chatbot` with JSON body:
```json
{
    "prompt": "Your message here"
}
```

## Project Structure

```
.
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
├── static/            # Static assets
└── templates/         # HTML templates
```
