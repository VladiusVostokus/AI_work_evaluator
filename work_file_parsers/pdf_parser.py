from interfaces.work_parser import WorkParser
import pymupdf

class PdfParser(WorkParser):
    def __init__(self, filename):
        self.file = filename

    def get_all_content(self):
        data = pymupdf.open(self.file)
        result = ''
        for page in data:
            result += page.get_text()
        return result

    def get_all_tables(self):
        pass

    def get_parsed_data(self):
        pass
    