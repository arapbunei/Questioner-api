import unittest
import json
from app import create_app

class TestQuestions(unittest.TestCase):
    def setUp(self):
        self.app = create_app
        self.client = self.app.test_client()

        self.question1 ={
            "title" : "Tests"
        }
        self.question2 ={
            "title" : "Tests",
            "question" : "What are tests"
        }
    """ Destroy all tests"""
    def tearDown(self):
        self.app.testing = False
        self.app = None

    def test_development_environment(self):
        self.assertTrue(create_app.config['DEBUG'] is True)
        self.assertFalse(create_app is None)

    # test json data 
    def test_json_data(self):
        response = self.client.post('api/v1/meetup/1/question')
        result = json.loads(response.data)
        self.assertEqual(result["message"],"Only input of Application/JSON expected")
        self.assertEqual(response.status_code, 400)

    # Test for empty fields
    def test_submit_empty_questions_fields(self):
        response = self.client.post('api/v1/meetup/1/question',data=json.dumps(self.question1),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],"Please enter a question and it's title")

    # Test for valid input
    def test_submit_valid_questions_fields(self):
        response = self.client.post('api/v1/meetup/1/question',data=json.dumps(self.question2),content_type="application/json")
        result = json.loads(response.data)
        self.assertTrue(result["data"])

    

    # upvote 
    def test_upvotesvotes(self):
        response = self.client.post('api/v1/meetup/1/question',data=json.dumps(self.question2),content_type="application/json")
        response = self.client.put('api/v1/questions/1/upvote')
        self.assertEqual(response.status_code, 200)

    # downvote 
    def test_downvotes(self):
        response = self.client.post('api/v1/meetup/1/question',data=json.dumps(self.question2),content_type="application/json")
        response = self.client.put('api/v1/questions/1/downvote')
        self.assertEqual(response.status_code, 200)

