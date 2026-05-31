import unittest
from store_api.json_subject_dao import JSONSubjectDAO
from store_api.task_dto import Task
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
        task = Task('lab1','just lab 1\n1. Create program\n2. Test it', '5 very well\n0 very bad')
        dao = JSONSubjectDAO(db_path)
        dao.create_subject(subject)
        dao.create_task(task, subject)
        with open(subject_path, 'r') as t:
            data = json.load(t)
            self.assertEqual(data['lab1']['description'], 'just lab 1\n1. Create program\n2. Test it')
            self.assertEqual(data['lab1']['criteria'], '5 very well\n0 very bad')

        task2 = Task('lab2','just lab 2\n1. Do something', '5 very well\n0 very bad')
        dao.create_task(task2, subject)
        with open(subject_path, 'r') as t:
            data = json.load(t)
            self.assertIsNotNone(data['lab1'])
            self.assertEqual(data['lab2']['description'], 'just lab 2\n1. Do something')
            self.assertEqual(data['lab2']['criteria'], '5 very well\n0 very bad')
        os.remove(subject_path)
        os.rmdir(db_path)

    def test_get_subject_data(self):
        db_path = './tests/db'
        subject = 'Алгоритми і структури даних'
        subject_path = f'{db_path}/{subject}.json'
        task = Task('lab1','just lab 1\n1. Create program\n2. Test it', '5 very well\n0 very bad')
        task2 = Task('lab2','just lab 2\n1. Do something', '5 very well\n0 very bad')
        dao = JSONSubjectDAO(db_path)

        dao.create_subject(subject)
        dao.create_task(task, subject)
        dao.create_task(task2, subject)
        data = dao.get_subject_data(subject)
        self.assertIsNotNone(data)

        self.assertEqual(data['lab1']['description'], 'just lab 1\n1. Create program\n2. Test it')
        self.assertEqual(data['lab2']['description'], 'just lab 2\n1. Do something')

        os.remove(subject_path)
        os.rmdir(db_path)
    
    def test_get_task_data(self):
        db_path = './tests/db'
        subject = 'Алгоритми і структури даних'
        subject_path = f'{db_path}/{subject}.json'
        task = Task('Завдання 1','just lab 1\n1. Create program\n2. Test it', '5 very well\n0 very bad')
        dao = JSONSubjectDAO(db_path)

        dao.create_subject(subject)
        dao.create_task(task, subject)

        data = dao.get_task_data(subject, 'Завдання 1')
        self.assertIsNotNone(data)
        self.assertEqual(data.description, 'just lab 1\n1. Create program\n2. Test it')

        os.remove(subject_path)
        os.rmdir(db_path)

    def test_non_existent_subject(self):
        db_path = './tests/db'
        subject = 'Алгоритми і структури даних'
        non_existent_subject = 'asdasdasada'
        subject_path = f'{db_path}/{subject}.json'
        dao = JSONSubjectDAO(db_path)
        dao.create_subject(subject)

        with self.assertRaises(Exception):
            dao.get_subject_data(non_existent_subject)

        os.remove(subject_path)
        os.rmdir(db_path)

    def test_get_empty_subject(self):
        db_path = './tests/db'
        subject = 'Алгоритми і структури даних'
        subject_path = f'{db_path}/{subject}.json'
        dao = JSONSubjectDAO(db_path)
        dao.create_subject(subject)

        with self.assertRaises(Exception):
            dao.get_subject_data(subject)

        os.remove(subject_path)
        os.rmdir(db_path)


    def test_non_existent_task(self):
        db_path = './tests/db'
        subject = 'Алгоритми і структури даних'
        non_existent_subject = 'asdasdasada'
        non_existent_task = 'Task asdasdasada'
        task = Task('Завдання 1','just lab 1\n1. Create program\n2. Test it', '5 very well\n0 very bad')
        subject_path = f'{db_path}/{subject}.json'
        dao = JSONSubjectDAO(db_path)
        dao.create_subject(subject)
        dao.create_task(task, subject)

        with self.assertRaises(Exception):
            dao.get_task_data(subject, non_existent_task)

        with self.assertRaises(Exception):
            dao.get_task_data(non_existent_subject, non_existent_task)

        with self.assertRaises(Exception):
            dao.get_task_data(non_existent_subject, 'Завдання 1')

        os.remove(subject_path)
        os.rmdir(db_path)

    def test_creation_of_subject_that_exist(self):
        db_path = './tests/db'
        subject = 'Алгоритми і структури даних'
        subject_path = f'{db_path}/{subject}.json'
        dao = JSONSubjectDAO(db_path)

        dao.create_subject(subject)

        with self.assertRaises(Exception):
            dao.create_subject(subject)

        os.remove(subject_path)
        os.rmdir(db_path)

    def test_creation_of_task_that_exist(self):
        db_path = './tests/db'
        subject = 'Алгоритми і структури даних'
        subject_path = f'{db_path}/{subject}.json'
        task = Task('Завдання 1','just lab 1\n1. Create program\n2. Test it', '5 very well\n0 very bad')
        dao = JSONSubjectDAO(db_path)

        dao.create_subject(subject)
        dao.create_task(task, subject)

        with self.assertRaises(Exception):
            dao.create_task(task, subject)

        os.remove(subject_path)
        os.rmdir(db_path)

    def test_teation_task_on_unexisting_subject(self):
        db_path = './tests/db'
        subject = 'Алгоритми і структури даних'
        non_existent_subject = 'asdasdasada'
        subject_path = f'{db_path}/{subject}.json'
        task = Task('Завдання 1','just lab 1\n1. Create program\n2. Test it', '5 very well\n0 very bad')
        dao = JSONSubjectDAO(db_path)
        dao.create_subject(subject)
        dao.create_task(task, subject)

        with self.assertRaises(Exception):
            dao.create_task(task, non_existent_subject)

        os.remove(subject_path)
        os.rmdir(db_path)

    def test_delete_subject(self):
        db_path = './tests/db'
        subject = 'Алгоритми і структури даних'
        subject_path = f'{db_path}/{subject}.json'
        dao = JSONSubjectDAO(db_path)
        dao.create_subject(subject)

        dao.delete_subject(subject)

        with self.assertRaises(Exception):
            dao.get_subject_data(subject)

        if os.path.exists(subject_path):
            os.remove(subject_path)
        os.rmdir(db_path)

    def test_delete_subject_that_not_exist(self):
        db_path = './tests/db'
        subject = 'Алгоритми і структури даних'
        non_existent_subject = 'asdasdasada'
        subject_path = f'{db_path}/{subject}.json'
        dao = JSONSubjectDAO(db_path)
        dao.create_subject(subject)

        with self.assertRaises(Exception):
            dao.delete_subject(non_existent_subject)

        os.remove(subject_path)
        os.rmdir(db_path)

    def test_delete_task(self):
        db_path = './tests/db'
        subject = 'Алгоритми і структури даних'
        task = Task('Завдання 1','just lab 1\n1. Create program\n2. Test it', '5 very well\n0 very bad')
        subject_path = f'{db_path}/{subject}.json'

        dao = JSONSubjectDAO(db_path)
        dao.create_subject(subject)
        dao.create_task(task, subject)

        dao.delete_task(subject, 'Завдання 1')

        with self.assertRaises(Exception):
            dao.get_task_data(subject, 'Завдання 1')

        os.remove(subject_path)
        os.rmdir(db_path)

    def test_delete_task_that_not_exist(self):
        db_path = './tests/db'
        subject = 'Алгоритми і структури даних'
        non_existent_subject = 'asdasdasada'
        task = Task('Завдання 1','just lab 1\n1. Create program\n2. Test it', '5 very well\n0 very bad')
        subject_path = f'{db_path}/{subject}.json'

        dao = JSONSubjectDAO(db_path)
        dao.create_subject(subject)
        dao.create_task(task, subject)

        with self.assertRaises(Exception):
            dao.delete_task(subject, 'Завдання 2')

        with self.assertRaises(Exception):
            dao.delete_task(non_existent_subject, 'Завдання 1')

        with self.assertRaises(Exception):
            dao.delete_task(non_existent_subject, 'Завдання 2')

        os.remove(subject_path)
        os.rmdir(db_path)

    def test_update_subject(self):
        db_path = './tests/db'
        subject = 'Алгоритми і структури даних'
        updated_subject = 'Cтруктури даних і алгоритми'
        task = Task('Завдання 1','just lab 1\n1. Create program\n2. Test it', '5 very well\n0 very bad')
        subject_path = f'{db_path}/{updated_subject}.json'

        dao = JSONSubjectDAO(db_path)
        dao.create_subject(subject)
        dao.create_task(task, subject)
        dao.rename_subject(subject, updated_subject)

        self.assertIsNotNone(dao.get_subject_data(updated_subject))

        os.remove(subject_path)
        os.rmdir(db_path)

    def test_update_task(self):
        db_path = './tests/db'
        subject = 'Алгоритми і структури даних'
        subject_path = f'{db_path}/{subject}.json'
        task = Task('Завдання 1','just lab 1\n1. Create program\n2. Test it', '5 very well\n0 very bad')
        update_task = Task('Завдання 2', 'task 2', '5 - OMG!!!!, 0 - cringre')

        dao = JSONSubjectDAO(db_path)
        dao.create_subject(subject)
        dao.create_task(task, subject)
        dao.update_task(subject, 'Завдання 1', update_task)

        data = dao.get_task_data(subject, 'Завдання 2')
        self.assertEqual(data.name, 'Завдання 2')
        self.assertEqual(data.description, 'task 2')
        self.assertEqual(data.criteria, '5 - OMG!!!!, 0 - cringre')
        os.remove(subject_path)
        os.rmdir(db_path)
        
    def test_update_task_name_only(self):
        db_path = './tests/db'
        subject = 'Алгоритми і структури даних'
        subject_path = f'{db_path}/{subject}.json'
        task = Task('Завдання 1','just lab 1\n1. Create program\n2. Test it', '5 very well\n0 very bad')
        update_task = Task('Завдання 2', '', '')

        dao = JSONSubjectDAO(db_path)
        dao.create_subject(subject)
        dao.create_task(task, subject)
        dao.update_task(subject, 'Завдання 1', update_task)

        data = dao.get_task_data(subject, 'Завдання 2')
        self.assertEqual(data.name, 'Завдання 2')
        self.assertEqual(data.description, 'just lab 1\n1. Create program\n2. Test it')
        self.assertEqual(data.criteria, '5 very well\n0 very bad')
        os.remove(subject_path)
        os.rmdir(db_path)

    def test_update_task_descr_and_criteria_only(self):
        db_path = './tests/db'
        subject = 'Алгоритми і структури даних'
        subject_path = f'{db_path}/{subject}.json'
        task = Task('Завдання 1','just lab 1\n1. Create program\n2. Test it', '5 very well\n0 very bad')
        update_task = Task('', 'task 2', '5 - OMG!!!!, 0 - cringre')

        dao = JSONSubjectDAO(db_path)
        dao.create_subject(subject)
        dao.create_task(task, subject)
        dao.update_task(subject, 'Завдання 1', update_task)

        data = dao.get_task_data(subject, 'Завдання 1')
        self.assertEqual(data.name, 'Завдання 1')
        self.assertEqual(data.description, 'task 2')
        self.assertEqual(data.criteria,'5 - OMG!!!!, 0 - cringre')
        os.remove(subject_path)
        os.rmdir(db_path)

    def test_update_task_that_not_exits(self):
        db_path = './tests/db'
        subject = 'Алгоритми і структури даних'
        non_existent_subject = 'asdasdasada'
        subject_path = f'{db_path}/{subject}.json'
        task = Task('Завдання 1','just lab 1\n1. Create program\n2. Test it', '5 very well\n0 very bad')
        update_task = Task('', 'task 2', '5 - OMG!!!!, 0 - cringre')

        dao = JSONSubjectDAO(db_path)
        dao.create_subject(subject)
        dao.create_task(task, subject)
        with self.assertRaises(Exception):
            dao.update_task(subject, 'dasdasdad', update_task)

        with self.assertRaises(Exception):
            dao.update_task(non_existent_subject, 'Завдання 1', update_task)

        with self.assertRaises(Exception):
            dao.update_task(non_existent_subject, 'dasdasdad', update_task)

        os.remove(subject_path)
        os.rmdir(db_path)

    def test_is_subject_exist(self):
        db_path = './tests/db'
        subject = 'Алгоритми і структури даних'
        non_existent_subject = 'asdasdasada'
        subject_path = f'{db_path}/{subject}.json'

        dao = JSONSubjectDAO(db_path)
        dao.create_subject(subject)

        self.assertTrue(dao.is_subject_exist(subject))
        self.assertFalse(dao.is_subject_exist(non_existent_subject))

        os.remove(subject_path)
        os.rmdir(db_path)

    def test_is_task_exist(self):
        db_path = './tests/db'
        subject1 = 'Алгоритми і структури даних'
        subject2 = 'Основи IoT'
        subject_path1 = f'{db_path}/{subject1}.json'
        subject_path2 = f'{db_path}/{subject2}.json'
        task = Task('Завдання 1','just lab 1\n1. Create program\n2. Test it', '5 very well\n0 very bad')

        dao = JSONSubjectDAO(db_path)
        dao.create_subject(subject1)
        dao.create_subject(subject2)
        dao.create_task(task, subject1)

        self.assertTrue(dao.is_task_exist(subject1, 'Завдання 1'))
        self.assertFalse(dao.is_task_exist(subject1, 'Завдання 2'))
        self.assertFalse(dao.is_task_exist(subject2, 'Завдання 1'))

        os.remove(subject_path1)
        os.remove(subject_path2)
        os.rmdir(db_path)

    def test_addition_of_multiple_subjects_and_tasks(self):
        db_path = './tests/db'
        subject1 = 'Алгоритми і структури даних'
        subject2 = 'Основи IoT'
        subject_path1 = f'{db_path}/{subject1}.json'
        subject_path2 = f'{db_path}/{subject2}.json'
        task1 = Task('Завдання 1','just lab 1\n1. Create program 1\n2. Test it', '1 very well\n0 very bad')
        task2 = Task('Завдання 2','just lab 2\n1. Create program 2\n2. Test it', '2 very well\n0 very bad ')
        task3 = Task('Завдання 3','just lab 3\n1. Create program 3\n2. Test it', '3 very well\n0 very bad')
        task4 = Task('Завдання 4','just lab 4\n1. Create program 4\n2. Test it', '4 very well\n0 very bad')
        classroom_data = {
            subject1: [task1, task2],
            subject2: [task3, task4]
        }
        dao = JSONSubjectDAO(db_path)
        dao.fill_db(classroom_data)
        data1 = dao.get_subject_data(subject1)
        data2 = dao.get_subject_data(subject2)
        self.assertEqual(data1['Завдання 1']['description'], 'just lab 1\n1. Create program 1\n2. Test it')
        self.assertEqual(data1['Завдання 2']['description'], 'just lab 2\n1. Create program 2\n2. Test it')
        self.assertEqual(data2['Завдання 3']['description'], 'just lab 3\n1. Create program 3\n2. Test it')
        self.assertEqual(data2['Завдання 4']['description'], 'just lab 4\n1. Create program 4\n2. Test it')

        os.remove(subject_path1)
        os.remove(subject_path2)
        os.rmdir(db_path)

    def test_add_only_new_tasks(self):
        db_path = './tests/db'
        subject = 'Алгоритми і структури даних'
        subject_path = f'{db_path}/{subject}.json'
        task1 = Task('Завдання 1','just lab 1\n1. Create program 1\n2. Test it', '1 very well\n0 very bad')
        updated_task1 = Task('Завдання 1','just lab 1!!!\n1. Create program 1\n2. Test it', '1 very well\n0 very bad')
        task2 = Task('Завдання 2','just lab 2\n1. Create program 2\n2. Test it', '2 very well\n0 very bad ')
        classroom_data = {
            subject: [updated_task1, task2],
        }
        dao = JSONSubjectDAO(db_path)
        dao.create_subject(subject)
        dao.create_task(task1, subject)
        dao.fill_db(classroom_data, True)
        data = dao.get_subject_data(subject)
        self.assertEqual(data['Завдання 1']['description'], 'just lab 1\n1. Create program 1\n2. Test it')
        self.assertEqual(data['Завдання 2']['description'], 'just lab 2\n1. Create program 2\n2. Test it')

        os.remove(subject_path)
        os.rmdir(db_path)

    def test_update_task_when_fill_db(self):
        db_path = './tests/db'
        subject = 'Алгоритми і структури даних'
        subject_path = f'{db_path}/{subject}.json'
        task1 = Task('Завдання 1','just lab 1\n1. Create program 1\n2. Test it', '1 very well\n0 very bad')
        updated_task1 = Task('Завдання 1','just lab 1!!!\n1. Create program 1\n2. Test it', '1 very well\n0 very bad')
        task2 = Task('Завдання 2','just lab 2\n1. Create program 2\n2. Test it', '2 very well\n0 very bad ')
        classroom_data = {
            subject: [updated_task1, task2],
        }
        dao = JSONSubjectDAO(db_path)
        dao.create_subject(subject)
        dao.create_task(task1, subject)
        dao.fill_db(classroom_data)
        data = dao.get_subject_data(subject)
        self.assertEqual(data['Завдання 1']['description'], 'just lab 1!!!\n1. Create program 1\n2. Test it')
        self.assertEqual(data['Завдання 2']['description'], 'just lab 2\n1. Create program 2\n2. Test it')

        os.remove(subject_path)
        os.rmdir(db_path)

    def test_backup_db(self):
        db_path = './tests/db'
        subject1 = 'Алгоритми і структури даних'
        subject2 = 'Основи IoT'
        subject_path1 = f'{db_path}/{subject1}.json'
        subject_path2 = f'{db_path}/{subject2}.json'
        task1 = Task('Завдання 1','just lab 1\n1. Create program 1\n2. Test it', '1 very well\n0 very bad')
        task2 = Task('Завдання 2','just lab 2\n1. Create program 2\n2. Test it', '2 very well\n0 very bad ')
        task3 = Task('Завдання 3','just lab 3\n1. Create program 3\n2. Test it', '3 very well\n0 very bad')
        task4 = Task('Завдання 4','just lab 4\n1. Create program 4\n2. Test it', '4 very well\n0 very bad')
        updated_task1 = Task('Завдання 1','Some corrucped data', 'corrupted criteria')
        updated_task4 = Task('Завдання 4','Some corrucped data', 'corrupted criteria')
        classroom_data = {
            subject1: [task1, task2],
            subject2: [task3, task4]
        }
        dao = JSONSubjectDAO(db_path)
        dao.fill_db(classroom_data)
        backup_data = dao.make_backup()
        dao.update_task(subject1, 'Завдання 1', updated_task1)
        dao.update_task(subject2, 'Завдання 4', updated_task4)

        dao.load_backup(backup_data)
        data1 = dao.get_subject_data(subject1)
        data2 = dao.get_subject_data(subject2)
        self.assertEqual(data1['Завдання 1']['description'], 'just lab 1\n1. Create program 1\n2. Test it')
        self.assertEqual(data1['Завдання 2']['description'], 'just lab 2\n1. Create program 2\n2. Test it')
        self.assertEqual(data2['Завдання 3']['description'], 'just lab 3\n1. Create program 3\n2. Test it')
        self.assertEqual(data2['Завдання 4']['description'], 'just lab 4\n1. Create program 4\n2. Test it')

        os.remove(subject_path1)
        os.remove(subject_path2)
        os.rmdir(db_path)


if __name__ == '__main__':
    unittest.main()    