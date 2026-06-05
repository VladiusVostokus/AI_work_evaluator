import uuid

from llm_api.llm_api_factory import llm_api
from store_api.json_subject_dao import JSONSubjectDAO
from store_api.task_dto import Task
from work_file_parsers.parser_factory import work_parser
from classroom_api.build_classroom import build_classroom
import os

store = 'jsondb'
evaluation = 'evaluation'
dao = JSONSubjectDAO(store)
classroom_api = None

def create_subject():
    print("Введіть назву дисципліни:")
    subject = input()
    try:
        dao.create_subject(subject)
        print(f"Дисципліна {subject} успішно створена\n")
    except Exception as e:
        print(f"Помилка під час створення дисципліни {e}\n")

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
    description: str
    criteria: str
    while(not os.path.exists(description_path)):
        print(f"Файлу з описом {description_path} не існує, введіть інший шлях, або" \
               "q - щоб повернутися назад чи натисніть Enter, якщо не хочете міняти")
        description_path = input()
        if (description_path) == 'q': return
    desc_parser = work_parser(description_path)
    description = desc_parser.get_parsed_data()

    print("Додайте критерії оцінювання(вкажіть шлях до файлу):")
    criteria_path = input()
    while(not os.path.exists(criteria_path)):
        print(f"Файлу з критеріями {criteria_path} не існує, введіть інший шлях, або q - щоб повернутися назад")
        criteria_path = input()
        if (criteria_path) == 'q': return
    
    crit_parser = work_parser(criteria_path)
    criteria = crit_parser.get_parsed_data()

    task = Task(task_name, description, criteria)
    try:
        dao.create_task(task, subject)
        print(f"Завдання {task_name} для дисципліни {subject} успішно створене\n")
    except Exception as e:
        print(f"Помилка під час створення завдання {e}\n")
        return
    

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
    while(not os.path.exists(task_path)):
        print(f"Файлу із завданням {task_path} не існує, введіть інший шлях, або q - щоб повернутися назад")
        task_path = input()
        if (task_path) == 'q': return

    print("Введіть ім'я мовної моделі, яку хочете використати:")
    llm_name = input()
    llm = llm_api(llm_name)
    while llm == None:
        print("Вказано не вірне ім'я моделі, вкажіть іншу модель, або q - щоб повернутися назад")
        llm_name = input()
        if (llm_name) == 'q': return
        llm = llm_api(llm_name)

    try:
        task = dao.get_task_data(subject, task_name)
        llm.form_message(subject, task_path, task)
        llm.make_request()
        short_id = str(uuid.uuid4().fields[-1])[:5]
        llm_name = llm_name.replace(':','-')
        evaluation_path = f'{evaluation}/{subject} {task_name} {llm_name}-{short_id}.txt'
        evaluation_result = llm.get_response()
        print(evaluation_result + '\n')
        with open(evaluation_path, 'w', encoding='utf-8') as f:
            f.write(evaluation_result)
    except Exception as e:
        print(f"Помилка під час перевірки завдання {e}\n")

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
        print(f"Помилка під час перейменування дисципліни: {e}\n")

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
    while((not os.path.exists(new_descr_path)) and new_descr_path != ""):
        print(f"Файлу з описом {new_descr_path} не існує, введіть інший шлях, або" \
               "q - щоб повернутися назад чи натисніть Enter, якщо не хочете міняти")
        new_descr_path = input()
        if (new_descr_path) == 'q': return

    if new_descr_path != "":
        desc_parser = work_parser(new_descr_path)
        new_description = desc_parser.get_parsed_data()
    else: new_description = ''

    print("Вкажіть шлях до файлу нових критеріїв завдання, або натисніть Enter, якщо не хочете міняти")
    new_crit_path = input()
    while((not os.path.exists(new_crit_path)) and new_crit_path != ""):
        print(f"Файлу з критеріями {new_crit_path} не існує, введіть інший шлях, або" \
               "q - щоб повернутися назад чи натисніть Enter, якщо не хочете міняти")
        new_crit_path = input()
        if (new_crit_path) == 'q': return

    if new_crit_path != "":
        crit_parser = work_parser(new_crit_path)
        new_criteria = crit_parser.get_parsed_data()
    else: new_criteria = ''

    task = Task(new_name, new_description, new_criteria)
    try:
        dao.update_task(subject, task_name, task)
        print("Завдання успішно оновлене\n")
    except Exception as e:
        print(f"Помилка під час оновлення дисципліни: {e}\n")

def update_db(classroom=classroom_api):
    print("Оновлення бази додасть дисципліни і завдання, яких не було і може оновити завдання існуючих дисциплін\n"\
          "y - підтвердити оновлення\n" \
          "n - не оновлювати існуючі завдання, додати лише нові\n" \
          "q чи будь що інше, щоб відмінити дію")
    confirm = input()
    if confirm == 'q':
        return
    try:
        if classroom is None:
            classroom = build_classroom()
        data = classroom.get_all_tasks()
        if confirm == 'y':
            dao.fill_db(data)
        elif confirm == 'n':
            dao.fill_db(data, True)
        print("База даних успішно оновлена\n")
    except Exception as e:
         print(f"Помилка під час оновлення бази: {e}\n")
    
actions = {
    's': create_subject,
    't': create_task,
    'c': check_task,
    'q': exit_program,
    'rs': rename_subject,
    'ut': update_task,
    'udb': update_db,
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
    print("Ви успішно створили першу дисциліну та завдання!\n")

while(True):
    if not os.path.exists(evaluation):
        os.mkdir(evaluation)
    print("Оберіть дію:\n" \
    "s - створити дисципліну\n" \
    "t - створити завдання\n" \
    "c - перевірити завдання\n" \
    "rs - перейменувати дисципліну\n" \
    "ut - оновити завдання\n" \
    "q - зупинити роботу програми\n" \
    "udb - оновити локальну базу даних за допомогою Google Classroom"
    )
    choise = input()
    if choise not in actions:
        print(f"{choise} некоректна дія, оберіть правильну дію")
        continue
    action = actions[choise]
    action()
