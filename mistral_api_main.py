import os
from mistralai import Mistral
from dotenv import load_dotenv, dotenv_values
from message_template_parts.sys_msg import sys_msg
from message_template_parts.usr_msg import usr_msg


load_dotenv()
MISTR_API = os.getenv('MISTR_API') 

model = "mistral-medium-latest"

client = Mistral(api_key=MISTR_API)

chat_response = client.chat.complete(
    model= model,
    messages = [
  {
    'role':'system',
    'content': sys_msg,  
  },
  {
    'role': 'user',
    'content': usr_msg,
  },
]
)

print(chat_response.choices[0].message.content)