from api.llm_api_factory import llm_api

print("Введіть ім'я роботи для перевірки:")
file = input()

llm = llm_api("gemini-3-flash-preview")
llm.form_message(file)
llm.make_request()
print(llm.get_response())