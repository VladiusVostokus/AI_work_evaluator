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
5. Install [Ollama]([url](https://ollama.com/download)) if you are going to use local models
6. Setup api keys for models you are going to use(Google, [Mistral]([url](https://docs.mistral.ai/getting-started/quickstarts/studio/activate-and-generate-api-key))) and save API keys to .env as GEM_API and MISTR_API
7. Set up [Google Workspace API]([url](https://developers.google.com/workspace/classroom/quickstart/python))
8. Set these scopes in Data Access
```bash
https://www.googleapis.com/auth/classroom.courses.readonly
https://www.googleapis.com/auth/classroom.coursework.students
https://www.googleapis.com/auth/drive.readonly
```
9. Save credentials.json and token.json in root of the project
10. Launch main.py(after first usage if updating DB via classroom, there will be page in browser that will ask some access to google services

