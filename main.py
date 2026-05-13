from llm_api.llm_api_factory import llm_api
from store_api.json_subject_dao import JSONSubjectDAO
from store_api.task_dto import Task
from message_template_parts.sys_msg import task_description
from work_file_parsers.parser_factory import work_parser
import os

store = 'jsondb'
dao = JSONSubjectDAO(store)

if len(os.listdir(store)) == 0:
    print("Створіть нову дисципліну, введіть ім'я:")
    subject_name = input()
    dao.create_subject(subject_name)
    print("Створіть нове завдання, введіть ім'я")
    task_name = input()
    print("Опис дисципліни додано")
    description = task_description
    print("Вкажіть критерії оцінювання завдання(шлях до файлу): ")
    criteria_path = input()
    parser = work_parser(criteria_path)
    criteria = parser.get_parsed_data()
    task = Task(task_name, description, criteria)
    dao.create_task(task, subject_name)


print("Оберіть дисципліну(вкажіть назву):")
subject = input()

print("Введіть ім'я роботи для перевірки(шлях до файлу):")
task_path = input()

print("Введіть ім'я мовної моделі, яку хочете використати:")
llm_name = input()
llm = llm_api(llm_name)
if llm != None:
    llm.form_message(subject, task_path, task)
    llm.make_request()
    print(llm.get_response())
else:
    print("Вказано не вірне ім'я моделі")
