import os
from mistralai import Mistral
from dotenv import load_dotenv, dotenv_values 

load_dotenv()
MISTR_API = os.getenv('MISTR_API') 

model = "mistral-medium-latest"

client = Mistral(api_key=MISTR_API)

chat_response = client.chat.complete(
    model= model,
    messages = [
        {
            "role": "user",
            "content": "Explain how AI works in a few words",
        },
    ]
)

print(chat_response.choices[0].message.content)