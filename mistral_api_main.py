import os
from mistralai.client import Mistral
from dotenv import load_dotenv, dotenv_values
from message_template_parts.sys_msg import sys_msg
from message_template_parts.usr_msg import usr_msg
from message_template_parts.structured_output import Evaluation


load_dotenv()
MISTR_API = os.getenv('MISTR_API') 

model = "mistral-medium-latest"

client = Mistral(api_key=MISTR_API)

tools = [{
    "type": "function",
    "function": {
        "name": "evaluate_text",
        "parameters": Evaluation.model_json_schema()
    }
}]

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
  ],
  tools=tools,
  tool_choice="auto"
)

args = chat_response.choices[0].message.tool_calls[0].function.arguments

parsed = Evaluation.model_validate_json(args)

print(chat_response.choices[0].message.content, parsed)