from  query import answer_query

import unittest

class TestQuestionAnswerAgent(unittest.TestCase):
    def test_valid_response(self):
        
        response = answer_query("What did the author do growing up?")
        
        self.assertIsNotNone(response)
        self.assertTrue(len(str(response)) > 0)
        
    def test_invalid_response(self):
        response = answer_query("")
        self.assertIsNone(response)
        
if __name__ == "__main__":
    unittest.main()
