from app import app

import unittest


class TestQAAPI(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client

    def test_valid_response(self):

        request = {"query": "What did the author do growing up?"}

        response = self.client().post("/answer", data=request)

        self.assertIsNotNone(response)
        self.assertTrue(len(str(response.data)) > 0)

    def test_invalid_response(self):
        request = {"query": ""}

        response = self.client().post("/answer", data=request)
        
        self.assertNotEqual(response.status_code, 200)
