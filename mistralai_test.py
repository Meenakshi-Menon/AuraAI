import json
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from config import apikey  # Import API key

# Initialize Mistral Client
client = MistralClient(api_key=apikey)

# Generate Response
response = client.chat(
    model="mistral-tiny",  # Or use "mistral-small"
    messages=[ChatMessage(role="user", content="Write an email to my boss for resignation?")],
    temperature=0.7,
    max_tokens=256,
    top_p=1
)

# Convert response to dictionary and print as JSON
try:
    response_dict = response.model_dump()  # Use model_dump() if it's a Pydantic object
except AttributeError:
    response_dict = response.__dict__  # Fallback to using __dict__ if model_dump() is unavailable

print(json.dumps(response_dict, indent=2))  # Pretty-print JSON response

'''
/Users/meenakshi/PycharmProjects/PythonProject/AuraAI/.venv/bin/python /Users/meenakshi/PycharmProjects/PythonProject/AuraAI/mistralai_test.py 
{
  "id": "e86b6a0b354e425cb34757bb3984a851",
  "object": "chat.completion",
  "created": 1740636871,
  "model": "mistral-tiny",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Subject: Resignation from [Your Position] at [Company Name]\n\nDear [Boss's Name],\n\nI am writing to formally announce my resignation from my position at [Company Name], effective two weeks from today's date, [Current Date].\n\nI have greatly enjoyed working with you and the entire team at [Company Name], and I am proud of the accomplishments we have achieved together. However, after careful consideration, I have decided to pursue new opportunities that align more closely with my long-term career goals.\n\nDuring my remaining time at the company, I will do everything possible to ensure a smooth transition. I am more than willing to assist in training a replacement or handing over my responsibilities to another team member. I want to ensure that the work I have been responsible for continues without interruption.\n\nI am grateful for the opportunities I have had to grow both personally and professionally while working at [Company Name]. I will always carry the lessons I have learned and the friendships I have made with me as I move forward in my career.\n\nThank you again for the opportunity to work with you and the team. I look forward to staying in touch and wish you and [Company",
        "name": null,
        "tool_calls": null,
        "tool_call_id": null
      },
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 13,
    "total_tokens": 269,
    "completion_tokens": 256
  }
}
'''









