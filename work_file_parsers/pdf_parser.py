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
        data = pymupdf.open(self.file)
        result = ''
        for page in data:
            tables = page.find_tables()
            for table in tables:
                result += table.to_markdown()
        return result


    def get_parsed_data(self):
        pass
    