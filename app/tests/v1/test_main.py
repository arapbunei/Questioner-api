import unittest

from app import create_app

class MainTest(unittest.TestCase):
    """ Main(base) class for the tests"""

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

    def tearDown(self):
        self.app = None
