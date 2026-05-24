import unittest
from work_file_parsers.docx_parser import DocxParser


class TestDocxParser(unittest.TestCase):
    def test_simple_docx(self):
        file = 'tests/files/file1.docx'
        parser = DocxParser(file)
        work_data = parser.get_all_content()
        self.assertEqual(len(work_data), 1)
        self.assertEqual(work_data[0]['type'], 'text')
        self.assertEqual(work_data[0]['data'], 'Some file with text')
    
    def test_table_docx(self):
        file = 'tests/files/doc.docx'
        parser = DocxParser(file)
        work_data = parser.get_all_content()
        self.assertEqual(len(work_data), 1)
        self.assertEqual(work_data[0]['type'], 'table')

    def test_complex_docx(self):
        file = 'tests/files/doc2.docx'
        parser = DocxParser(file)
        work_data = parser.get_all_content()
        docx_block_count = 7
        self.assertEqual(len(work_data), docx_block_count)
        type_list = ['text', 'table', 'text', 'text', 'table', 'table', 'text']
        for i, block in enumerate(work_data):
            self.assertEqual(block['type'], type_list[i])

    def test_parsed_complex_docx(self):
        file = 'tests/files/doc3.docx'
        parser = DocxParser(file)
        work_data = parser.get_all_content()
        docx_block_count = 3
        self.assertEqual(len(work_data), docx_block_count)
        parsed_data = parser.get_parsed_data()
        result_table = 'Some text\n\n===TABLE START===\n| 1 | 2 | 3 |\n| --- | --- | --- |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |\n===TABLE END===\n\nSome text 2\n\n'
        self.assertEqual(parsed_data, result_table)

    def test_file_that_not_exist(self):
        file = 'unexistent/file.docx'
        with self.assertRaises(Exception):
            parser = DocxParser(file)

if __name__ == '__main__':
    unittest.main()