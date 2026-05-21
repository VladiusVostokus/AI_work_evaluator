from llm_api.llm_api_factory import llm_api
from store_api.json_subject_dao import JSONSubjectDAO
from store_api.task_dto import Task
from work_file_parsers.parser_factory import work_parser
import os

store = 'jsondb'
dao = JSONSubjectDAO(store)

def create_subject():
    print("Введіть назву дисципліни:")
    subject = input()
    dao.create_subject(subject)
    print(f"Дисципліна {subject} успішно створена")

def create_task():
    print("Оберіть дисципліну(вкажіть назву):")
    subject = input()
    print("Введіть ім'я завдання(вкажіть назву):")
    task_name = input()
    print("Додайте опис завдання(вкажіть шлях до файлу):")
    description_path = input()

    print("Додайте критерії оцінювання(вкажіть шлях до файлу):")
    criteria_path = input()

    desc_parser = work_parser(description_path)
    description = desc_parser.get_parsed_data()
    crit_parser = work_parser(criteria_path)
    criteria = crit_parser.get_parsed_data()

    task = Task(task_name, description, criteria)
    dao.create_task(task, subject)
    print(f"Завдання {task_name} для дисципліни {subject} успішно створене")

def check_task():
    print("Оберіть дисципліну(вкажіть назву):")
    subject = input()

    print("Оберіть завдання для перевірки(вкажіть назву):")
    task_name = input()

    print("Введіть шлях до файлу роботи:")
    task_path = input()

    print("Введіть ім'я мовної моделі, яку хочете використати:")
    llm_name = input()
    llm = llm_api(llm_name)
    if llm != None:
        task = dao.get_task_data(subject, task_name)
        llm.form_message(subject, task_path, task)
        llm.make_request()
        print(llm.get_response())
    else:
        print("Вказано не вірне ім'я моделі")

def exit_program():
    print("Завершення роботи програми")
    exit()

actions = {
    's': create_subject,
    't': create_task,
    'c': check_task,
    'q': exit_program
}

if len(os.listdir(store)) == 0:
    print("У базі ще немає дисциплін, створіть нову дисципліну, введіть ім'я:")
    subject_name = input()
    dao.create_subject(subject_name)
    print("Створіть нове завдання, введіть ім'я")
    task_name = input()
    print("Додайте опис завдання(вкажіть шлях до файлу)")
    description_path = input()
    desc_parser = work_parser(description_path)
    description = desc_parser.get_parsed_data()
    print("Вкажіть критерії оцінювання завдання(шлях до файлу): ")
    criteria_path = input()
    task_parser = work_parser(criteria_path)
    criteria = task_parser.get_parsed_data()
    task = Task(task_name, description, criteria)
    dao.create_task(task, subject_name)

while(True):
    print("Оберіть дію: s - створити дисципліну, t - створити завдання, c - перевірити завдання, q - зупинити роботу програми")
    choise = input()
    if choise not in actions:
        print(f"{choise} некоректна дія, оберіть правильну дію")
        continue
    action = actions[choise]
    action()
    
