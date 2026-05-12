from llm_api.gemini import Gemini

models = {
    "gemini-3-flash-preview": Gemini,
}

def llm_api(model_name):
    if model_name in models:
        model = models[model_name]
        return model(model_name)
    else:
        return None
