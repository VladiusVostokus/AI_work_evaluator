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
    try:
        dao.create_subject(subject)
        print(f"Дисципліна {subject} успішно створена\n")
    except Exception as e:
        print(f"Помилка під час створення дисципліни {e}")

def create_task():
    print("Оберіть дисципліну(вкажіть назву):")
    subject = input()
    while (not dao.is_subject_exist(subject)):
        print(f"Дисципліни {subject} не існує, введіть іншу назву, або q - щоб повернутися назад")
        subject = input()
        if (subject == 'q'): return

    print("Введіть ім'я завдання(вкажіть назву):")
    task_name = input()
    while (dao.is_task_exist(subject, task_name)):
        print(f"Завдання {task_name} вже існує, введіть іншу назву, або q - щоб повернутися назад")
        task_name = input()
        if (task_name == 'q'): return
    print("Додайте опис завдання(вкажіть шлях до файлу):")
    description_path = input()
    desc_parser = work_parser(description_path)
    description = desc_parser.get_parsed_data()

    print("Додайте критерії оцінювання(вкажіть шлях до файлу):")
    criteria_path = input()
    crit_parser = work_parser(criteria_path)
    criteria = crit_parser.get_parsed_data()

    task = Task(task_name, description, criteria)
    try:
        dao.create_task(task, subject)
        print(f"Завдання {task_name} для дисципліни {subject} успішно створене\n")
    except Exception as e:
        print(f"Помилка під час створення завдання {e}")
    

def check_task():
    print("Оберіть дисципліну(вкажіть назву):")
    subject = input()
    while (not dao.is_subject_exist(subject)):
        print(f"Дисципліни {subject} не існує, введіть іншу назву, або q - щоб повернутися назад")
        subject = input()
        if (subject == 'q'): return

    print("Оберіть завдання для перевірки(вкажіть назву):")
    task_name = input()
    while (not dao.is_task_exist(subject, task_name)):
        print(f"Завдання {task_name} не існує, введіть іншу назву, або q - щоб повернутися назад")
        task_name = input()
        if (task_name == 'q'): return

    print("Введіть шлях до файлу роботи:")
    task_path = input()

    print("Введіть ім'я мовної моделі, яку хочете використати:")
    llm_name = input()
    llm = llm_api(llm_name)
    if llm != None:
        try:
            task = dao.get_task_data(subject, task_name)
            llm.form_message(subject, task_path, task)
            llm.make_request()
            print(llm.get_response())
        except Exception as e:
            print(f"Помилка під час перевірки завдання {e}")
    else:
        print("Вказано не вірне ім'я моделі")

def exit_program():
    print("Завершення роботи програми")
    exit()

def rename_subject():
    print('Введіть назву дисципліни, яку хочете оновити')
    old_name = input()
    while (not dao.is_subject_exist(old_name)):
        print(f"Дисципліни {old_name} не існує, введіть іншу назву, або q - щоб повернутися назад")
        old_name = input()
        if (old_name == 'q'): return
    print('Введіть нову назву дисципліни')
    new_name = input()
    try:
        dao.rename_subject(old_name, new_name)
        print(f"Дисципліну {old_name} перейменовано в {new_name}\n")
    except Exception as e:
        print(f"Помилка під час перейменування дисципліни: {e}")

def update_task():
    print("Введіть ім'я дисципліни:")
    subject = input()
    while (not dao.is_subject_exist(subject)):
        print(f"Дисципліни {subject} не існує, введіть іншу назву, або q - щоб повернутися назад")
        subject = input()
        if (subject == 'q'): return

    print("Оберіть завдання, яке хочете оновити (вкажіть назву):")
    task_name = input()
    while (not dao.is_task_exist(subject, task_name)):
        print(f"Завдання {task_name} не існує, введіть іншу назву, або q - щоб повернутися назад")
        task_name = input()
        if (task_name == 'q'): return

    print("Введіть нове ім'я завдання, або натисніть Enter, якщо не хочете міняти назву")
    new_name = input()
    print("Вкажіть шлях до файлу нового опису завдання, або натисніть Enter, якщо не хочете міняти")
    new_descr_path = input()
    if new_descr_path != "":
        desc_parser = work_parser(new_descr_path)
        new_description = desc_parser.get_parsed_data()
    else: new_description = ''

    print("Вкажіть шлях до файлу нових критеріїв завдання, або натисніть Enter, якщо не хочете міняти")
    new_crit_path = input()
    if new_crit_path != "":
        crit_parser = work_parser(new_crit_path)
        new_criteria = crit_parser.get_parsed_data()
    else: new_criteria = ''

    task = Task(new_name, new_description, new_criteria)
    try:
        dao.update_task(subject, task_name, task)
        print("Завдання успішно оновлене\n")
    except Exception as e:
        print(f"Помилка під час оновлення дисципліни: {e}")
    

actions = {
    's': create_subject,
    't': create_task,
    'c': check_task,
    'q': exit_program,
    'rs': rename_subject,
    'ut': update_task,
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
    print("Оберіть дію:\n" \
    "s - створити дисципліну\n" \
    "t - створити завдання\n" \
    "c - перевірити завдання\n" \
    "rs - перейменувати дисципліну\n" \
    "ut - оновити завдання\n" \
    "q - зупинити роботу програми")
    choise = input()
    if choise not in actions:
        print(f"{choise} некоректна дія, оберіть правильну дію")
        continue
    action = actions[choise]
    action()
    
