from api.llm_api_factory import llm_api

print("Введіть ім'я роботи для перевірки:")
file = input()

print("Введіть ім'я мовної моделі, яку хочете використати:")
llm_name = input()
llm = llm_api(llm_name)
if llm != None:
    llm.form_message(file)
    llm.make_request()
    print(llm.get_response())
else:
    print("Вказано не вірне ім'я моделі")
