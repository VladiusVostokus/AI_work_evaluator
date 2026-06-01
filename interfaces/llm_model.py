from abc import ABC, abstractmethod
from store_api.task_dto import Task

class LLMModel(ABC):
    
    @abstractmethod
    def form_message(subject_name: str, task_path: str, task_data: Task):
        pass

    @abstractmethod
    def make_request():
        pass
    
    @abstractmethod
    def get_response():
        pass