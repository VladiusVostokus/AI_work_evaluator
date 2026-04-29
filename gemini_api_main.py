from google import genai
import os
from dotenv import load_dotenv, dotenv_values 
from message_template_parts.sys_msg import sys_msg_template, role_descriprion, response_format, response_constrains, task_description, task_structure, criteria_description, criteria_format
from message_template_parts.usr_msg import usr_msg

load_dotenv()
GEM_API = os.getenv('GEM_API') 

client = genai.Client(api_key=GEM_API)

sys_msg = sys_msg_template.to_string(role_descriprion=role_descriprion,
                                   task_description=task_description,
                                   task_structure=task_structure,
                                   criteria_format=criteria_format,
                                   criteria_description=criteria_description,
                                   response_constrains=response_constrains,
                                   response_format=response_format)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        {
            "role":"system",
            "parts": [
                { "text": sys_msg }
                ]
        },
        {
            "role":"user",
            "parts":[
                {"text": usr_msg }
            ]
        },
    ]
)
print(response.text)