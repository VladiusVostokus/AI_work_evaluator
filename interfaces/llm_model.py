from abc import ABC, abstractmethod

class LLMModel(ABC):
    
    @abstractmethod
    def form_message():
        pass

    @abstractmethod
    def make_request():
        pass
    
    @abstractmethod
    def get_response():
        pass