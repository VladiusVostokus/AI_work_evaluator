import unittest
from store_api.json_subject_dao import JSONSubjectDAO
from store_api.subject_dto import Task
import os
import json

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

    def test_task_creation(self):
        db_path = './tests/db'
        subject = 'Алгоритми і структури даних'
        subject_path = f'{db_path}/{subject}.json'
        task = Task('lab1','just lab 1','1. Create program\n2. Test it', '5 very well\n0 very bad')
        dao = JSONSubjectDAO(db_path)
        dao.create_subject(subject)
        dao.create_task(task, subject)
        with open(subject_path, 'r') as t:
            data = json.load(t)
            self.assertEqual(data['lab1']['description'], 'just lab 1')
            self.assertEqual(data['lab1']['structure'], '1. Create program\n2. Test it')
            self.assertEqual(data['lab1']['criteria'], '5 very well\n0 very bad')

        task2 = Task('lab2','just lab 2','1. Do something', '5 very well\n0 very bad')
        dao.create_task(task2, subject)
        with open(subject_path, 'r') as t:
            data = json.load(t)
            self.assertIsNotNone(data['lab1'])
            self.assertEqual(data['lab2']['description'], 'just lab 2')
            self.assertEqual(data['lab2']['structure'], '1. Do something')
            self.assertEqual(data['lab2']['criteria'], '5 very well\n0 very bad')
        os.remove(subject_path)
        os.rmdir(db_path)

if __name__ == '__main__':
    unittest.main()    