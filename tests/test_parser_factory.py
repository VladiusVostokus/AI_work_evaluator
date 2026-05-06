import unittest
from work_file_parsers.parser_factory import work_parser
from work_file_parsers.pdf_parser import PdfParser
from work_file_parsers.docx_parser import DocxParser

class TestParserFactory(unittest.TestCase):
    def test_pdf(self):
        filename = 'somedir/somefile.pdf'
        parser = work_parser(filename)
        self.assertEqual(type(parser), PdfParser)

    def test_docx(self):
        filename = 'somedir/somefile.docx'
        parser = work_parser(filename)
        self.assertEqual(type(parser), DocxParser)

if __name__ == '__main__':
    unittest.main()