from interfaces.work_parser import WorkParser
from docx import Document
from docx.document import Document as DOC_TYPE
from docx.text.paragraph import Paragraph
from docx.table import Table
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from utils.mark_table_bounds import mark_table_bounds

class DocxParser(WorkParser):
    def __init__(self, filename):
        self.file = filename

    def __generate_doc_objects(self, doc):
        if isinstance(doc, DOC_TYPE):
            parent_el = doc.element.body
        else:
            parent_el = doc._element

        for child in parent_el.iterchildren():
            if isinstance(child, CT_P):
                yield Paragraph(child, doc)
            elif isinstance(child, CT_Tbl):
                yield Table(child, doc)

    def get_all_content(self):
        document = Document(self.file)
        result = []
        for item in self.__generate_doc_objects(document):
            if isinstance(item, Paragraph):
                text = item.text.strip()
                if text:
                    result.append({'type':'text', 'data': text})
            elif isinstance(item, Table):
                table_data = []
                for row in item.rows:
                    row_content = [cell.text.strip() for cell in row.cells]
                    table_data.append(row_content)
                result.append({'type':'table', 'data': table_data})
        return result

    def get_parsed_data(self):
        file_content = self.get_all_content()
        parsed_data = mark_table_bounds(file_content)
        return parsed_data