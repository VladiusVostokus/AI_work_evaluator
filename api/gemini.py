from google import genai
from interfaces.llm_model import LLMModel
import os
from dotenv import load_dotenv
from message_template_parts.sys_msg import sys_msg_template, role_descriprion, response_format, response_constrains, task_description, task_structure, criteria_format
from work_file_parsers.parser_factory import work_parser


class Gemini(LLMModel):
    def __init__(self, model_name):
        load_dotenv()
        GEM_API = os.getenv('GEM_API') 
        self.client = genai.Client(api_key=GEM_API)
        self.model = model_name

    def form_message(self, file, criteria):
        criteria_parser = work_parser(criteria)
        criteria = criteria_parser.get_all_content()
        self.sys_msg = sys_msg_template.to_string(
            role_descriprion=role_descriprion,
            task_description=task_description,
            task_structure=task_structure,
            criteria_format=criteria_format,
            criteria_description=criteria,
            response_constrains=response_constrains,
            response_format=response_format)
        
        parser = work_parser(file)
        self.usr_msg = parser.get_all_content()

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