from interfaces.SubjectDAO import SubjectDAO
from store_api.subject_dto import Task
import json
import os

class JSONSubjectDAO(SubjectDAO):
    def __init__(self, store: str):
        self.store = store
        if not os.path.exists(store):
            os.mkdir(store)

    def create_subject(self, name: str):
        subject_path = f'{self.store}/{name}.json'
        if not os.path.exists(subject_path):
            with open(subject_path, 'w'):
                pass
        
    def get_subject_data(self, name: str):
        subject_path = f'{self.store}/{name}.json'
        if os.path.exists(subject_path):
            with open(subject_path, 'r') as s:
                data = json.load(s)  
                return data

    def create_task(self, task_data: Task, subject: str):
        subject_path = f'{self.store}/{subject}.json'
        if os.path.exists(subject_path) and os.path.getsize != 0:
            with open(subject_path, 'r') as t:
                try:
                    data = json.load(t)
                except json.JSONDecodeError:
                    data = {}
        else:
            data = {}
        
        data[task_data.name] = {
                'description': task_data.description,
                'structure': task_data.structure,
                'criteria': task_data.criteria
            }
        with open(subject_path, 'w', encoding='utf-8') as t:
            json.dump(data, t, ensure_ascii=False, indent=2)

        
