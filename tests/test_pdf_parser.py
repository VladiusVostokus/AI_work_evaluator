import unittest
from work_file_parsers.pdf_parser import PdfParser
from files.parsed_file2 import work_file

class TestPdfParser(unittest.TestCase):
    def test_simple_pdf(self):
        file = 'tests/files/file1.pdf'
        parser = PdfParser(file)
        work_data = parser.get_all_content()
        self.assertEqual(work_data, 'Some file with text \n')

    def test_tables_pdf(self):
        file = 'tests/files/doc.pdf'
        parser = PdfParser(file)
        work_data = parser.get_all_tables()
        self.assertIsNotNone(work_data)

if __name__ == '__main__':
    unittest.main()