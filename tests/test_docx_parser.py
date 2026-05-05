import unittest
from work_file_parsers.docx_parser import DocxParser

class TestDocxParser(unittest.TestCase):
    def test_simple_docx(self):
        file = 'tests/files/file1.docx'
        parser = DocxParser(file)
        work_data = parser.get_all_content()
        self.assertEqual(work_data, 'Some file with text')

if __name__ == '__main__':
    unittest.main()