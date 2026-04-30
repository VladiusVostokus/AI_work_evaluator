from api.gemini import Gemini

models = {
    "gemini-3-flash-preview": Gemini,
}

def llm_api(model_name):
    model = models[model_name]
    return model(model_name)
