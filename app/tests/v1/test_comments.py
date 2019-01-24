from flask import json
from .base_test import BaseTest
from app.api.v1.models.comment_model import comments
from app.api.v1.models.question_model import questions

class TestComments(BaseTest):
    """ Testing for comments endpoints """

    def setUp(self):
        """ Initialize variables to be used for tests """

        super().setUp()

        self.meetup = {
            'topic' : 'AI meetup',
            'location' : 'Andela HQ, Nairobi',
            'happening_on' : '30/01/2019',
            'tags' : ['python', 'ai']
        }

        self.question = {
            'title' : 'Intro to AI',
            'body' : 'why you should care about ai?',
            'meetup_id' : 1
        }

        self.comment = {
            'body' : 'because ai is the future'
        }

        self.comment_2 = {
            'body' : 'actually ai is the present'
        }

        super().register()
        self.headers = {'Authorization': 'Bearer {}'.format(self.access_token)}

        self.client.post('/api/v1/meetups', json=self.meetup, headers=self.headers)
        self.client.post('/api/v1/questions', json=self.question, headers=self.headers)

    def tearDown(self):
        """ Destroy initialized variables """

        comments.clear()
        questions.clear()
        super().tearDown()

    def test_post_comment_question_not_posted(self):
        """ Test post comment to a question that hasn't been posted """

        res = self.client.post('/api/v1/questions/3/comments', headers=self.headers)
        data = res.get_json()

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['status'], 404)
        self.assertEqual(data['message'], 'Question not found')

    def test_post_comment_question_no_data(self):
        """ Test post comment without question data """

        res = self.client.post('/api/v1/questions/1/comments', headers=self.headers)
        data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'No data provided')

    def test_post_comment_question_empty_data(self):
        """ Test post comment with empty data """

        self.comment.clear()

        res = self.client.post('/api/v1/questions/1/comments', json=json.dumps(self.comment), headers=self.headers)
        data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'Invalid data. Please fill all required fields')

    def test_post_comment(self):
        """ Test post comment successfully """

        res = self.client.post('/api/v1/questions/1/comments', json=self.comment, headers=self.headers)
        data = res.get_json()

        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['status'], 201)
        self.assertEqual(data['message'], 'Comment posted successfully')

    def test_fetch_all_comments_question_not_posted(self):
        """ Test fetch all comments for question that doesn't exist """

        res = self.client.get('/api/v1/questions/5/comments')
        data = res.get_json()

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['status'], 404)
        self.assertEqual(data['message'], 'Question not found')

    def test_fetch_all_comments(self):
        """ Test fetch all comments for a question """
        
        self.client.post('/api/v1/questions/1/comments', json=self.comment, headers=self.headers)
        self.client.post('/api/v1/questions/1/comments', json=self.comment_2, headers=self.headers)

        res = self.client.get('/api/v1/questions/1/comments')
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status'], 200)
        self.assertEqual(len(data['data']), 2)
