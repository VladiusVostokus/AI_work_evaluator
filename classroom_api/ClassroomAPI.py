import os
import io
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from store_api.task_dto import Task
from googleapiclient.http import MediaIoBaseDownload
from work_file_parsers.parser_factory import work_parser

class ClassroomAPI:
    def __init__(self, SCOPES: list, credentials: str, token_json: str):
        self.creds: Credentials = None
        self.servise = {}
        if os.path.exists(token_json):
            self.creds = Credentials.from_authorized_user_file(token_json, SCOPES)
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    credentials, SCOPES
                )
                self.creds = flow.run_local_server(port=0)
            with open("token.json", "w") as token:
                token.write(self.creds.to_json())

    def build_servise(self, servise_name: str, version: str):
        try:
            servise = build(servise_name, version, credentials=self.creds)
            self.servise[servise_name] = servise
        except Exception as e:
            print("Error while build servise", e)

    def get_servises(self):
        return self.servise
    
    def get_subjects(self):
        try:
            response = (self.servise['classroom'].courses()
                    .list(teacherId="me", courseStates=["ACTIVE"])
                    .execute()
            )
            courses = response.get("courses", [])
            return courses
        except HttpError as e:
            print(f"Error while get subjects: {e}")
    
    def __download_files(self, ids: dict):
        try:
            for id in ids:
                request = self.servise['drive'].files().get_media(fileId=id)
                file_handler = io.BytesIO()
                downloader = MediaIoBaseDownload(file_handler, request)
                done = False
                while not done:
                    done = downloader.next_chunk()
                    file_name = ids[id]
                    with open(f'{id}{file_name}', 'wb') as f:
                        f.write(file_handler.getvalue())
        except HttpError as e:
            print(f"Error while downloading files: {e}")

    def __delete_temp_files(self, ids: list):
        for id in ids:
            file_name = ids[id]
            os.remove(f'{id}{file_name}')
    
    def get_all_tasks(self):
        try:
            courses = self.get_subjects()
            result = {}
            for cousre in courses:
                course_id = cousre['id']
                result[cousre['name']] = []
                task_response = (self.servise['classroom'].courses()
                    .courseWork()
                    .list(courseId=course_id)
                    .execute()
                )
                tasks = task_response.get("courseWork", [])
                for t in tasks:
                    description = t.get('description','')
                    if 'materials' in t:
                        ids = {}
                        for material in t['materials']:
                            if 'driveFile' in material:
                                file_data = material['driveFile']['driveFile']
                                ids[file_data['id']] = file_data['title']
                        if len(ids) > 0:
                            self.__download_files(ids)
                            for id in ids:
                                file_name = ids[id]
                                parser = work_parser(f'{id}{file_name}')
                                data = parser.get_parsed_data()
                                description += '\n' + data
                            self.__delete_temp_files(ids)
                    task = Task(t['title'], description, '')
                    result[cousre['name']].append(task)
            return result
        except HttpError as e:
            print(f"Error while getting classroom tasks: {e}")
                        