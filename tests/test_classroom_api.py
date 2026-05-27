import unittest
from classroom_api.ClassroomAPI import ClassroomAPI

class TestClassromAPI(unittest.TestCase):
    def test_constructor(self):
        SCOPES = ["https://www.googleapis.com/auth/classroom.courses.readonly"]
        credentials = "credentials.json"
        token = "token.json"
        self.assertIsNotNone(ClassroomAPI(SCOPES, credentials, token))

if __name__ == '__main__':
    unittest.main()
