from llm_api.gemini import Gemini
from llm_api.mistral import MistralAi

models = {
    "gemini-3-flash-preview": Gemini,
    "mistral-medium-latest": MistralAi,
    "mistral-large-latest": MistralAi,
}

def llm_api(model_name):
    if model_name in models:
        model = models[model_name]
        return model(model_name)
    else:
        return None
