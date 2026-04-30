import unittest
from work_file_parsers.parser_factory import work_parser
from work_file_parsers.pdf_parser import PdfParser

class TestParserFactory(unittest.TestCase):
    def test_pdf(self):
        filename = 'somedir/somefile.pdf'
        parser = work_parser(filename)
        self.assertEqual(type(parser), PdfParser)
