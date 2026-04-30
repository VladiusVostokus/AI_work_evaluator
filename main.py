from api.gemini import Gemini

print("Введіть ім'я роботи для перевірки:")
file = input()

gemini = Gemini("gemini-3-flash-preview")
gemini.form_message(file)
gemini.make_request()
print(gemini.get_response())