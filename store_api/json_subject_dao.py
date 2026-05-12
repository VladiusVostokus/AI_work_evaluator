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
        
    def get_subject_data(self):
        pass

    def create_task(self, task_data: Task):
        pass
