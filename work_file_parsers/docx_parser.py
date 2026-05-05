from interfaces.work_parser import WorkParser
from docx import Document

class DocxParser(WorkParser):
    def __init__(self, filename):
        self.file = filename

    def get_all_content(self):
        document = Document(self.file)
        result = ''
        for paragraph in document.paragraphs:
            result += paragraph.text
        return result


    def get_all_tables(self):
        pass

    def get_parsed_data(self):
        pass