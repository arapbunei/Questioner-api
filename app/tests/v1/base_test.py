import unittest
from app import create_app
from app.api.v1.models.user_model import users

class BaseTest(unittest.TestCase):
    """ Base class for Tests """

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

        self.super_user = {
            'firstname' : 'Bobley',
            'lastname' : 'Swagger',
            'othername' : 'lee',
            'username' : 'bobleeswagger',
            'email' : 'boblee@gmail.com',
            'password' : '5h00t3r',
            'phone_number' : '0700000000'
        }

    def tearDown(self):
        self.app = None
        users.clear()

    def register(self):
        """ to sign up user and get access token """
        
        res = self.client.post('/api/v1/register', json=self.super_user)
        data = res.get_json()

        self.access_token = data['access_token']
        self.refresh_token = data['refresh_token']
