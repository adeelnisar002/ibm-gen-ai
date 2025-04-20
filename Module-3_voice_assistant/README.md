# Voice Assistant with Groq AI

A modern voice assistant web application powered by Groq's AI models for natural language processing and voice interactions. This application provides a seamless interface for text and voice-based conversations with an AI assistant.

## Features

- 🎙️ **Voice Input**: Record your questions using your microphone
- 🔊 **Voice Output**: Hear responses in natural-sounding speech
- 💬 **Text Chat**: Traditional text-based chat interface
- 🌓 **Dark/Light Mode**: Toggle between dark and light themes
- 🎭 **Voice Selection**: Choose different voices for the assistant
- 🚀 **Powered by Groq AI**: 
  - LLaMA 3.3 70B for text processing
  - Whisper Large V3 for speech recognition
  - PlayAI TTS for voice synthesis

## Prerequisites

- Python 3.7 or higher
- Groq API key
- Modern web browser with microphone support

## Installation

1. Install required Python packages:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the project root and add your Groq API key:
```
GROQ_API_KEY=your_groq_api_key_here
```

## Project Structure

```
chatapp-with-voice-and-openai-outline/
├── templates/
│   └── index.html          # Web interface template
├── static/
│   ├── css/
│   │   └── style.css      # Application styling
│   └── js/
│       └── app.js         # Frontend JavaScript
├── worker.py              # AI processing functions
├── server.py             # Flask server
└── requirements.txt      # Python dependencies
```

## Usage

1. Start the Flask server:
```bash
python server.py
```

3. Open your web browser and navigate to:
```
http://localhost:8000
```

4. You can interact with the assistant in two ways:
   - Type your message in the text input and click "Send"
   - Click the microphone button to record your voice message

## Features in Detail

### Voice Input
- Click the microphone button to start recording
- Click again to stop recording
- Your voice will be converted to text using Groq's Whisper model
- The transcribed text will be processed by the AI

### Text Processing
- Messages are processed using Groq's LLaMA 3.3 70B model
- The assistant can:
  - Answer questions
  - Translate sentences
  - Summarize news
  - Give recommendations
  - And more!

### Voice Output
- AI responses are converted to speech using Groq's PlayAI TTS
- Choose different voices from the voice selector
- Audio plays automatically when responses are received

### User Interface
- Modern, responsive design
- Dark/Light mode toggle
- Real-time chat interface
- Voice recording status indicator
- Scrollable chat history

## Error Handling

The application includes robust error handling for:
- Microphone access issues
- Network connectivity problems
- API rate limits
- Invalid responses
- Long text processing

## Technical Details

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python, Flask
- **AI Services**: Groq API
  - Text Generation: LLaMA 3.3 70B
  - Speech-to-Text: Whisper Large V3
  - Text-to-Speech: PlayAI TTS

## Acknowledgments

- Groq AI for providing the AI models and APIs
- Flask team for the web framework
- Open source community for various tools and libraries used 