import unittest
from utils.mark_table_bounds import mark_table_bounds

class TestPdfParser(unittest.TestCase):
    def test_emply(self):
        table=''
        self.assertEqual(mark_table_bounds(table), '')

    def test_text(self):
        text = [{'type': 'text', 'data': 'Some text here'}]
        self.assertEqual(mark_table_bounds(text), 'Some text here\n\n')

    def test_table(self):
        table = [{'type': 'table', 'data': [['1', '2', '3'], 
                 ['4', '5', '6'], 
                 ['7', '8', '9']]}]
        result_table = '===TABLE START===\n| 1 | 2 | 3 |\n| --- | --- | --- |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |\n===TABLE END===\n\n'
        self.assertEqual(mark_table_bounds(table), result_table)

    def test_text_and_table(self):
        table = [{'type': 'text', 'data': 'Some text here'},
                {'type': 'table', 'data': [['1', '2', '3'], 
                                            ['4', '5', '6'], 
                                            ['7', '8', '9']]},
                {'type': 'text', 'data': 'Some text here2'}]
        
        result_table = 'Some text here\n\n===TABLE START===\n| 1 | 2 | 3 |\n| --- | --- | --- |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |\n===TABLE END===\n\nSome text here2\n\n'
        self.assertEqual(mark_table_bounds(table), result_table)


if __name__ == '__main__':
    unittest.main()