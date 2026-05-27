import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class ClassroomAPI:
    def __init__(self, SCOPES: list, credentials: str, token_json: str):
        self.creds: Credentials
        self.servise = {}
        if os.path.exists(token_json):
            creds = Credentials.from_authorized_user_file(token_json, SCOPES)
            self.creds = creds
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
                self.creds = creds
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    credentials, SCOPES
                )
                creds = flow.run_local_server(port=0)
                self.creds = creds
            with open("token.json", "w") as token:
                token.write(creds.to_json())

    def build_servise(self, servise_name: str, version: str):
        servise = build(servise_name, version, credentials=self.creds)
        self.servise[servise_name] = servise

    def get_servises(self):
        return self.servise
    

