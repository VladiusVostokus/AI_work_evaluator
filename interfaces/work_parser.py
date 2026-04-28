from abc import ABC, abstractmethod

class WorkParser(ABC):

    @abstractmethod
    def get_all_content():
        pass

    @abstractmethod
    def get_all_tables():
        pass
    
    @abstractmethod
    def get_parsed_data():
        pass