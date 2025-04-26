import os
import gradio as gr
from groq import Groq

# Initialize Groq client
client = Groq()

# Function to transcribe audio using Groq's Whisper model
def transcript_audio(audio_file):
    # Transcribe the audio file using Groq's Whisper
    with open(audio_file, "rb") as file:
        transcription = client.audio.transcriptions.create(
            file=(audio_file, file.read()),
            model="whisper-large-v3",
            response_format="verbose_json",
        )
    return transcription.text

# Set up Gradio interface
audio_input = gr.Audio(sources="upload", type="filepath")  # Audio input
output_text = gr.Textbox()  # Text output

# Create the Gradio interface with the function, inputs, and outputs
iface = gr.Interface(fn=transcript_audio, 
                     inputs=audio_input, 
                     outputs=output_text, 
                     title="Audio Transcription App",
                     description="Upload the audio file")

# Launch the Gradio app
iface.launch(server_name="0.0.0.0", server_port=7860)