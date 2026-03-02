from ollama import chat
from ollama import ChatResponse
from message_template_parts.sys_msg import sys_msg
from message_template_parts.usr_msg import usr_msg

response: ChatResponse = chat(model='gpt-oss:20b', messages=[
  {
    'role':'system',
    'content': sys_msg
  },
  {
    'role': 'user',
    'content': usr_msg,
  },
])

print(response.message.content)