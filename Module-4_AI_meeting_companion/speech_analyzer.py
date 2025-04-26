import os
import gradio as gr
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv('GROQ_API_KEY')
if not api_key:
    raise ValueError("Please set your GROQ_API_KEY in the .env file or environment variables")

# Initialize Groq client with API key
client = Groq(api_key=api_key)

#######------------- Prompt Template-------------####

def get_llm_response(context):
    completion = client.chat.completions.create(
        model="gemma2-9b-it",
        messages=[
            {"role": "system", "content": "List the key points with details from the context:"},
            {"role": "user", "content": context}
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
    )
    return completion.choices[0].message.content

#######------------- Speech2text-------------####

def transcript_audio(audio_file):
    # Transcribe the audio file using Groq's Whisper
    with open(audio_file, "rb") as file:
        transcription = client.audio.transcriptions.create(
            file=(audio_file, file.read()),
            model="whisper-large-v3",
            response_format="verbose_json",
        )
    
    # Get LLM response for the transcribed text
    result = get_llm_response(transcription.text)
    return result

#######------------- Gradio-------------####

audio_input = gr.Audio(sources="upload", type="filepath")
output_text = gr.Textbox()

iface = gr.Interface(fn=transcript_audio, 
                    inputs=audio_input, 
                    outputs=output_text, 
                    title="Audio Transcription App",
                    description="Upload the audio file")

print("\nStarting the server...")
print("You can access the application at: http://localhost:7860")
print("Press Ctrl+C to stop the server\n")

iface.launch(server_name="127.0.0.1", server_port=7860, share=False)