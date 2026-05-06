import unittest
from api.gemini import Gemini
from api.llm_api_factory import llm_api

class TestParserFactory(unittest.TestCase):
    def test_gemini(self):
        model_name = 'gemini-3-flash-preview'
        model = llm_api(model_name)
        self.assertEqual(type(model), Gemini)

if __name__ == '__main__':
    unittest.main()