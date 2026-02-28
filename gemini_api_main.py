from google import genai
import os
from dotenv import load_dotenv, dotenv_values 

load_dotenv()
GEM_API = os.getenv('GEM_API') 

client = genai.Client(api_key=GEM_API)

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)
print(response.text)