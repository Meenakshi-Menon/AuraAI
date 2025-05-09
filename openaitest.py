import openai
from config import apikey  # Import API key from config.py

# Set API key
client = openai.OpenAI(api_key=apikey)

# Make an API request
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello, how are you?"}],
    temperature=1,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# Print the response
print(response.choices[0].message.content)

