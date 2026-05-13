from google import genai
from interfaces.llm_model import LLMModel
import os
from dotenv import load_dotenv
from message_template_parts.sys_msg import sys_msg_template, message_mock
from work_file_parsers.parser_factory import work_parser
from store_api.task_dto import Task


class Gemini(LLMModel):
    def __init__(self, model_name):
        load_dotenv()
        GEM_API = os.getenv('GEM_API') 
        self.client = genai.Client(api_key=GEM_API)
        self.model = model_name

    def form_message(self, subject_name: str, task_path: str, task_data: Task):
        self.sys_msg = sys_msg_template.to_string(
            role_descriprion=subject_name,
            task_description=task_data.description,
            criteria=task_data.criteria,
            response_constrains=message_mock['response_constrains'],
            response_format=message_mock['response_format']
        )
        
        parser = work_parser(task_path)
        self.usr_msg = parser.get_parsed_data()

    def make_request(self):
        self.response = self.client.models.generate_content(
            model=self.model,
            contents=[
                { 
                    "role":"system",
                    "parts": [
                    { "text": self.sys_msg }
                ]
            },
            {
                "role":"user",
                "parts":[
                    {"text": self.usr_msg }
                ]
            },
        ]
    )

    def get_response(self):
        return self.response.text