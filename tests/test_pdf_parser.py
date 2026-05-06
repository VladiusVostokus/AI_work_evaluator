import unittest
from work_file_parsers.pdf_parser import PdfParser
from files.parsed_file2 import work_table

class TestPdfParser(unittest.TestCase):
    def test_simple_pdf(self):
        file = 'tests/files/file1.pdf'
        parser = PdfParser(file)
        work_data = parser.get_all_content()
        self.assertEqual(len(work_data), 1)
        self.assertEqual(work_data[0]['type'], 'text')
        self.assertEqual(work_data[0]['data'], 'Some file with text')

    def test_table_pdf(self):
        file = 'tests/files/doc.pdf'
        parser = PdfParser(file)
        work_data = parser.get_all_content()
        self.assertEqual(len(work_data), 1)
        self.assertEqual(work_data[0]['type'], 'table')
        self.assertEqual(work_data[0]['data'], work_table)

    def test_complex_pfd(self):
        file = 'tests/files/doc2.pdf'
        parser = PdfParser(file)
        work_data = parser.get_all_content()
        pdf_block_count = 6
        self.assertEqual(len(work_data), pdf_block_count)
        type_list = ['text', 'table', 'text', 'table', 'table', 'text']
        for i, block in enumerate(work_data):
            self.assertEqual(block['type'], type_list[i])

if __name__ == '__main__':
    unittest.main()