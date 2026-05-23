from interfaces.SubjectDAO import SubjectDAO
from store_api.task_dto import Task
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
        else:
            raise Exception("Subject already exist")
        
    def get_subject_data(self, name: str):
        subject_path = f'{self.store}/{name}.json'
        if os.path.exists(subject_path):
            with open(subject_path, 'r', encoding='utf-8') as s:
                data = json.load(s)  
                return data
        else:
            raise Exception("Subject doesn't exist")
        
    def rename_subject(self, name: str, new_name: str):
        subject_path = f'{self.store}/{name}.json'
        if os.path.exists(subject_path):
            new_subject_path = f'{self.store}/{new_name}.json'
            os.rename(subject_path, new_subject_path)
        
    def delete_subject(self, subject: str):
        subject_path = f'{self.store}/{subject}.json'
        if os.path.exists(subject_path):
            os.remove(subject_path)
        else:
            raise Exception("Delete error: subject doesn't exist")
        

    def create_task(self, task_data: Task, subject: str):
        subject_path = f'{self.store}/{subject}.json'
        if not os.path.exists(subject_path):
            raise Exception("Subject doesn't exist to create task")
        if os.path.getsize != 0:
            with open(subject_path, 'r', encoding='utf-8') as t:
                try:
                    data = json.load(t)
                except json.JSONDecodeError:
                    data = {}
        else:
            data = {}

        if task_data.name in data:
            raise Exception("Subject already exist")
        
        data[task_data.name] = {
                'description': task_data.description,
                'criteria': task_data.criteria
            }
        with open(subject_path, 'w', encoding='utf-8') as t:
            json.dump(data, t, ensure_ascii=False, indent=2)

    def get_task_data(self, subject: str, task: str):
        subject_path = f'{self.store}/{subject}.json'
        if os.path.exists(subject_path):
            with open(subject_path, 'r', encoding='utf-8') as s:
                data = json.load(s)
                if task not in data:
                    raise Exception("Task doesn't exist")
                else:
                    task_data = data[task]
                    return Task(task, task_data['description'], task_data['criteria'])
        else:
            raise Exception("Subject doesn't exist")
        
    def update_task(self, subject: str, task: str, updated_task: Task):
        subject_path = f'{self.store}/{subject}.json'
        if os.path.exists(subject_path):
            with open(subject_path, 'r', encoding='utf-8') as t:
                data = json.load(t)
                if task not in data:
                    raise Exception("Task update error: task doesn't exist")
                task_data = data[task]
                if updated_task.criteria != '':
                    task_data['criteria'] = updated_task.criteria
                if updated_task.description != '':
                    task_data['description'] = updated_task.description
                if updated_task.name != '':
                    data.pop(task)
                    data[updated_task.name] = task_data
                    with open(subject_path, 'w', encoding='utf-8') as t:
                        json.dump(data, t, ensure_ascii=False, indent=2)
                else:
                    data[task] = task_data
                    with open(subject_path, 'w', encoding='utf-8') as t:
                        json.dump(data, t, ensure_ascii=False, indent=2)
        else:
            raise Exception("Task update error: subject doesn't exist")
            
 
    def delete_task(self, subject: str, task: str):
        subject_path = f'{self.store}/{subject}.json'
        if os.path.exists(subject_path):
            task_data = {}
            with open(subject_path, 'r', encoding='utf-8') as t:
                data = json.load(t)
                if task not in data:
                    raise Exception("Task delete error: Task doesn't exist")
                else:
                    data.pop(task)
                    task_data = data
            with open(subject_path, 'w', encoding='utf-8') as t:
                json.dump(task_data, t, ensure_ascii=False, indent=2)
        else:
            raise Exception("Task delete error: Subject doesn't exist")
        
    def is_subject_exist(self, subject: str) -> bool:
        subject_path = f'{self.store}/{subject}.json'
        if os.path.exists(subject_path):
            return True
        return False
    
    def is_task_exist(self, subject: str, task: str):
        subject_path = f'{self.store}/{subject}.json'
        with open(subject_path, 'r', encoding='utf-8') as t:
            data = json.load(t)
            if task in data:
                return True
            return False
