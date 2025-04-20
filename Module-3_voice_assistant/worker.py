import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Groq client with API key from environment variables
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def chunk_text(text, max_chars=500):
    """Split text into chunks to avoid rate limits"""
    sentences = text.split('. ')
    chunks = []
    current_chunk = []
    current_length = 0
    
    for sentence in sentences:
        sentence_length = len(sentence)
        if current_length + sentence_length <= max_chars:
            current_chunk.append(sentence)
            current_length += sentence_length
        else:
            chunks.append('. '.join(current_chunk) + '.')
            current_chunk = [sentence]
            current_length = sentence_length
    
    if current_chunk:
        chunks.append('. '.join(current_chunk))
    
    return chunks

def speech_to_text(audio_binary):
    # Save the audio binary to a temporary file
    temp_audio_path = str(Path(__file__).parent / "temp_audio.m4a")
    with open(temp_audio_path, "wb") as f:
        f.write(audio_binary)
    
    try:
        # Use Groq's Whisper model for transcription
        with open(temp_audio_path, "rb") as file:
            transcription = client.audio.transcriptions.create(
                file=(os.path.basename(temp_audio_path), file.read()),
                model="whisper-large-v3",
                response_format="verbose_json",
            )
        
        return transcription.text
    except Exception as e:
        print(f"Error in speech_to_text: {str(e)}")
        return None
    finally:
        # Clean up the temporary file
        if os.path.exists(temp_audio_path):
            os.remove(temp_audio_path)

def text_to_speech(text, voice=""):
    # Set default voice if none specified
    if not voice or voice == "default":
        voice = "Aaliyah-PlayAI"
    
    try:
        # Generate speech using Groq's TTS
        response = client.audio.speech.create(
            model="playai-tts",
            voice=voice,
            response_format="wav",
            input=text,
        )
        
        # Get the raw bytes from the response
        if hasattr(response, 'read'):
            # If response is file-like
            audio_data = response.read()
        else:
            # If response has raw bytes
            audio_data = response._content if hasattr(response, '_content') else response.content
            
        return audio_data
    
    except Exception as e:
        print(f"Error in text_to_speech: {str(e)}")
        return None

def openai_process_message(user_message):
    try:
        # Use Groq's chat completion with shorter max tokens
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "Act like a personal assistant. You can respond to questions, translate sentences, summarize news, and give recommendations. Keep responses concise."},
                {"role": "user", "content": user_message}
            ],
            temperature=1,
            max_tokens=800,  # Reduced max tokens
            top_p=1,
            stream=False,
            stop=None,
        )
        
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error in openai_process_message: {str(e)}")
        return "I apologize, but I encountered an error processing your request. Please try again with a shorter message."
