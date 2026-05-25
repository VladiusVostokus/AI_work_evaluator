from ollama import chat
from ollama import ChatResponse
from dotenv import load_dotenv, dotenv_values
from message_template_parts.sys_msg import sys_msg_template, message_mock, response_format2
from interfaces.llm_model import LLMModel
from work_file_parsers.parser_factory import work_parser
from store_api.task_dto import Task

class OpenAI(LLMModel):
    def __init__(self, modelname):
        self.model = modelname

    def form_message(self, subject_name: str, task_path: str, task_data: Task):
        self.sys_msg = sys_msg_template.to_string(
            role_descriprion=subject_name,
            task_description=task_data.description,
            criteria=task_data.criteria,
            response_constrains=message_mock['response_constrains'],
            response_format=response_format2
        )
        
        parser = work_parser(task_path)
        self.usr_msg = parser.get_parsed_data()

    def make_request(self):
        self.response = chat(
            model= self.model,
            messages = [
                {
                    'role':'system',
                    'content': self.sys_msg,  
                },
                {
                    'role': 'user',
                    'content': self.usr_msg,
                },
            ],
        )

    def get_response(self):
        return self.response.message.content