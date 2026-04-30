from work_file_parsers.pdf_parser import PdfParser
from utils.get_file_format import get_file_format

parsers = {
    'pdf': PdfParser,
}

def work_parser(file_name):
    format = get_file_format(file_name)
    parser = parsers[format]
    return parser(file_name)
