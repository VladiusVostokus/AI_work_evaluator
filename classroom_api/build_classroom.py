from classroom_api.ClassroomAPI import ClassroomAPI


def build_classroom():
    SCOPES = ["https://www.googleapis.com/auth/classroom.courses.readonly", 
            "https://www.googleapis.com/auth/classroom.coursework.students",
            "https://www.googleapis.com/auth/drive.readonly"
        ]
    credentials = "credentials.json"
    token = "token.json"
    api = ClassroomAPI(SCOPES, credentials, token)
    api.build_servise('classroom', 'v1')
    api.build_servise('drive', 'v3')
    return api