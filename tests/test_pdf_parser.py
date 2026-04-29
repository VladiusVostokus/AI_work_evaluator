import unittest
from work_file_parsers.pdf_parser import PdfParser
from files.parsed_file2 import work_file

class TestPdfParser(unittest.TestCase):
    def test_simple_pdf(self):
        file = 'tests/files/file1.pdf'
        parser = PdfParser(file)
        work_data = parser.get_all_content()
        self.assertEqual(work_data, 'Some file with text \n')

    #def test_work_pds(self):
        #file = 'tests/files/file2.pdf'
        #parser = PdfParser(file)
        #work_data = parser.get_all_content()
        #self.assertEqual(work_data, work_file)
        
if __name__ == '__main__':
    unittest.main()