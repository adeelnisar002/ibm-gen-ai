import base64
import json
from flask import Flask, render_template, request
from worker import speech_to_text, text_to_speech, openai_process_message
from flask_cors import CORS
import os

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/speech-to-text', methods=['POST'])
def speech_to_text_route():
    print("processing speech-to-text")
    audio_binary = request.data # Get the user's speech from their request
    text = speech_to_text(audio_binary) # Call speech_to_text function to transcribe the speech
    
    if text is None:
        return app.response_class(
            response=json.dumps({'error': 'Failed to process speech'}),
            status=500,
            mimetype='application/json'
        )

    # Return the response back to the user in JSON format
    response = app.response_class(
        response=json.dumps({'text': text}),
        status=200,
        mimetype='application/json'
    )
    print(response)
    print(response.data)
    return response

@app.route('/process-message', methods=['POST'])
def process_message_route():
    try:
        user_message = request.json['userMessage'] # Get user's message from their request
        print('user_message', user_message)

        voice = request.json['voice'] # Get user's preferred voice from their request
        print('voice', voice)

        # Call openai_process_message function to process the user's message and get a response back
        openai_response_text = openai_process_message(user_message)
        if not openai_response_text:
            raise Exception("Failed to get response from AI")

        # Clean the response to remove any emptylines
        openai_response_text = os.linesep.join([s for s in openai_response_text.splitlines() if s])

        # Call our text_to_speech function to convert OpenAI Api's reponse to speech
        openai_response_speech = text_to_speech(openai_response_text, voice)

        response_data = {
            "openaiResponseText": openai_response_text,
        }
        
        # Only include speech if it was generated successfully
        if openai_response_speech is not None:
            response_data["openaiResponseSpeech"] = base64.b64encode(openai_response_speech).decode('utf-8')

        # Send a JSON response back to the user containing their message's response both in text and speech formats
        response = app.response_class(
            response=json.dumps(response_data),
            status=200,
            mimetype='application/json'
        )

        print(response)
        return response
        
    except Exception as e:
        print(f"Error in process_message_route: {str(e)}")
        return app.response_class(
            response=json.dumps({
                "error": "An error occurred processing your request",
                "openaiResponseText": "I apologize, but I encountered an error processing your request. Please try again."
            }),
            status=500,
            mimetype='application/json'
        )


if __name__ == "__main__":
    app.run(port=8000, host='0.0.0.0')
