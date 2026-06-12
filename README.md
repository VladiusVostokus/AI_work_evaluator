# AI work evaluator(or LLM work evaluator)

## Prerequisites
- Python 3.14 or newer
- Ollama(in case of using local models for evaluations)

## How to start
1. Clone this repo
2. Set up virtual environment
For linux
```bash
python3 -m venv env
source ./env/bin/activate
```
For windows
```bash
python3 -m venv env
.\venv\Scripts\activate.bat
```
4. Install dependencies using this in root directory of the project
```bash
pip install -r requirements.txt
```
5. Install [Ollama](https://ollama.com/download) if you are going to use local models
6. Setup api keys for models you are going to use([Google](https://ai.google.dev/gemini-api/docs/quickstart), [Mistral](https://docs.mistral.ai/getting-started/quickstarts/studio/activate-and-generate-api-key) and save API keys to .env as GEM_API and MISTR_API
7. Set up [Google Workspace API](https://developers.google.com/workspace/classroom/quickstart/python)
8. Set these scopes in Data Access
```bash
https://www.googleapis.com/auth/classroom.courses.readonly
https://www.googleapis.com/auth/classroom.coursework.students
https://www.googleapis.com/auth/drive.readonly
```
9. Save credentials.json and token.json in root of the project

## Usage
1. Launch main.py(after first updating DB via classroom, there will be page in browser that will ask some access to google services)
2. Navigate using CLI, programm will write a message in console about which symbols type to do some action on programm
3. For descriptions and criterias use .docx or .pdf files(you need to pass file paths when programm asks). Warning: there are some problems with pdf files, so if you want to use them, it is better to use files with simpler content because sometimes programm doesn't always correcly get text blocks and tables from pdf document(I'll try to fix this)

## Tests
Code is tested automatically by github actions, to run all test use in console:
```bash
python -m unittest discover ./tests
```

To run some specific test, use this in console:
```bash
python -m unittest .\tests\test_some_gile.py
```
    
## Add new models
For now, MistralAPI, GoogleAPI and Ollama are available, so you can add any model from this API's.
To do it, go to file [```llm_api_factory.py```](https://github.com/VladiusVostokus/AI_work_evaluator/blob/main/llm_api/llm_api_factory.py) to dictionary ```models```. Add record for this dict "model-name": LLMAPIClass. If some llm is from MistralAPI, instead of LLMAPIClass add MistralAi etc.
