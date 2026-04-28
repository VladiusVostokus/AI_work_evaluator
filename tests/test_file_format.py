import unittest
from utils.get_file_format import get_file_format

class TestSimpleGetFormat(unittest.TestCase):
    def test_pdf(self):
        self.assertEqual(get_file_format('somework.pdf'), 'pdf')

if __name__ == '__main__':
    unittest.main()