import unittest
from utils.get_file_format import get_file_format

class TestSimpleGetFormat(unittest.TestCase):
    def test_pdf(self):
        self.assertEqual(get_file_format('somework.pdf'), 'pdf')

    def test_docx(self):
        self.assertEqual(get_file_format('somework.docx'), 'docx')

    def test_jpeg(self):
        self.assertEqual(get_file_format('somework.jpeg'), 'jpeg')


if __name__ == '__main__':
    unittest.main()