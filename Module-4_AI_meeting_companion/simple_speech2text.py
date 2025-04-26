import os
from groq import Groq

# Initialize Groq client
client = Groq()

# Define the local file path where the audio file will be saved
audio_file_path = "downloaded_audio.mp3"

# Transcribe the audio file using Groq's Whisper
with open(audio_file_path, "rb") as file:
    transcription = client.audio.transcriptions.create(
        file=(audio_file_path, file.read()),
        model="whisper-large-v3",
        response_format="verbose_json",
    )

# Print the transcribed text to the console
print(transcription.text)