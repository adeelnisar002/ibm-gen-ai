document.addEventListener('DOMContentLoaded', () => {
    const chatContainer = document.getElementById('chatContainer');
    const userInput = document.getElementById('userInput');
    const sendBtn = document.getElementById('sendBtn');
    const micBtn = document.getElementById('micBtn');
    const themeToggle = document.getElementById('themeToggle');
    const voiceSelect = document.getElementById('voiceSelect');
    
    let isRecording = false;
    let mediaRecorder = null;
    let audioChunks = [];

    // Theme Toggle
    themeToggle.addEventListener('change', () => {
        document.body.classList.toggle('dark-mode');
    });

    // Send message function
    const sendMessage = async (message, isVoice = false) => {
        if (!message.trim()) return;

        // Add user message to chat
        appendMessage('user', message);
        userInput.value = '';

        try {
            // Send message to backend
            const response = await fetch('/process-message', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    userMessage: message,
                    voice: voiceSelect.value
                }),
            });

            const data = await response.json();
            
            // Add assistant's response to chat
            appendMessage('assistant', data.openaiResponseText);

            // Play audio response
            if (data.openaiResponseSpeech) {
                const audio = new Audio('data:audio/wav;base64,' + data.openaiResponseSpeech);
                audio.play();
            }
        } catch (error) {
            console.error('Error:', error);
            appendMessage('assistant', 'Sorry, there was an error processing your request.');
        }
    };

    // Append message to chat
    const appendMessage = (sender, text) => {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', `${sender}-message`);
        messageDiv.textContent = text;
        chatContainer.appendChild(messageDiv);
        chatContainer.scrollTop = chatContainer.scrollHeight;
    };

    // Handle send button click
    sendBtn.addEventListener('click', () => {
        sendMessage(userInput.value);
    });

    // Handle enter key press
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage(userInput.value);
        }
    });

    // Handle microphone button click
    micBtn.addEventListener('click', async () => {
        if (!isRecording) {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
                mediaRecorder = new MediaRecorder(stream);
                audioChunks = [];

                mediaRecorder.addEventListener('dataavailable', (event) => {
                    audioChunks.push(event.data);
                });

                mediaRecorder.addEventListener('stop', async () => {
                    const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
                    
                    try {
                        const response = await fetch('/speech-to-text', {
                            method: 'POST',
                            body: audioBlob
                        });
                        
                        const data = await response.json();
                        if (data.text) {
                            sendMessage(data.text, true);
                        }
                    } catch (error) {
                        console.error('Error:', error);
                        appendMessage('assistant', 'Sorry, there was an error processing your speech.');
                    }

                    stream.getTracks().forEach(track => track.stop());
                });

                mediaRecorder.start();
                isRecording = true;
                micBtn.classList.add('recording');
            } catch (error) {
                console.error('Error accessing microphone:', error);
                appendMessage('assistant', 'Error accessing microphone. Please check your permissions.');
            }
        } else {
            mediaRecorder.stop();
            isRecording = false;
            micBtn.classList.remove('recording');
        }
    });
}); 