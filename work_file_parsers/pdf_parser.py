from interfaces.work_parser import WorkParser
import pymupdf

class PdfParser(WorkParser):
    def __init__(self, filename):
        self.file = filename

    def get_all_content(self):
        data = pymupdf.open(self.file)
        return data[0].get_text()

    def get_all_tables(self):
        pass

    def get_parsed_data(self):
        pass
    