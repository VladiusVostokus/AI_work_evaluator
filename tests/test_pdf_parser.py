import unittest
from work_file_parsers.pdf_parser import PdfParser

class TestPdfParser(unittest.TestCase):
    def test_simple_pdf(self):
        file = 'tests/files/file1.pdf'
        parser = PdfParser(file)
        work_data = parser.get_all_content()
        self.assertEqual(work_data, 'Some file with text \n')