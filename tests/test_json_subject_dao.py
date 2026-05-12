import unittest
from store_api.json_subject_dao import JSONSubjectDAO
import os

class TestJSONSubjectDao(unittest.TestCase):

    def test_db_creation(self):
        db_path = './db'
        dao = JSONSubjectDAO(db_path)
        self.assertTrue(os.path.exists(db_path))
        os.rmdir(db_path)

if __name__ == '__main__':
    unittest.main()    