import os
from google import genai

# Pass your AQ. key directly or load from environment variable
client = genai.Client(api_key="your APIKEY")

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Hello! Test connection.",
)

print(response.text)