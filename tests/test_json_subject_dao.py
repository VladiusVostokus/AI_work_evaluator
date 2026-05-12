import unittest
from store_api.json_subject_dao import JSONSubjectDAO
import os

class TestJSONSubjectDao(unittest.TestCase):

    def test_db_creation(self):
        db_path = './tests/db'
        dao = JSONSubjectDAO(db_path)
        self.assertTrue(os.path.exists(db_path))
        os.rmdir(db_path)

    def test_subject_creation(self):
        db_path = './tests/db'
        subject = 'Алгоритми і структури даних'
        subject_path = f'{db_path}/{subject}.json'
        dao = JSONSubjectDAO(db_path)
        dao.create_subject(subject)
        self.assertTrue(os.path.exists(subject_path))
        os.remove(subject_path)
        os.rmdir(db_path)

if __name__ == '__main__':
    unittest.main()    