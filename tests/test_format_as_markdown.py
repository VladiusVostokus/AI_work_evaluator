import unittest
from utils.format_as_markdown import format_as_markdown

class TestSimpleGetFormat(unittest.TestCase):
    def test_emply(self):
        table=''
        self.assertEqual(format_as_markdown(table), '')

    def test_simple_table(self):
        table = [['1', '2', '3']]
        result_table = '| 1 | 2 | 3 |\n| --- | --- | --- |\n'
        self.assertEqual(format_as_markdown(table), result_table)

    def test_bigger_table(self):
        table = [['1', '2', '3'], 
                 ['4', '5', '6'], 
                 ['7', '8', '9']]
        result_table = '| 1 | 2 | 3 |\n| --- | --- | --- |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |\n'
        self.assertEqual(format_as_markdown(table), result_table)

    def test_bigger_table_with_holes(self):
        table = [['1', '2', '3'], 
                 ['4', '5', ''], 
                 ['7', '8', '9']]
        result_table = '| 1 | 2 | 3 |\n| --- | --- | --- |\n| 4 | 5 |  |\n| 7 | 8 | 9 |\n'
        self.assertEqual(format_as_markdown(table), result_table)

if __name__ == '__main__':
    unittest.main()