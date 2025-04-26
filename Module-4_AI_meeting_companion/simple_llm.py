from groq import Groq

# Initialize Groq client
client = Groq()

# Create a chat completion
completion = client.chat.completions.create(
    model="gemma2-9b-it",
    messages=[
        {"role": "user", "content": "How to read a book effectively?"}
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
)

print(completion.choices[0].message.content)