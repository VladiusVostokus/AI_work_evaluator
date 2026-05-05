from work_file_parsers.pdf_parser import PdfParser
from work_file_parsers.docx_parser import DocxParser
from utils.get_file_format import get_file_format

parsers = {
    'pdf': PdfParser,
    'docx': DocxParser,
}

def work_parser(file_name):
    format = get_file_format(file_name)
    parser = parsers[format]
    return parser(file_name)
