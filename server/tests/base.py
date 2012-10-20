import unittest
import json

from settings import BACKEND
from app import app

from models import User


class TestApiBase(unittest.TestCase):

    def setUp(self):

        app.testing = True
        self.client = app.test_client()
        self.user = User(username="test", password="test", email="test@test.com")
        self.user.save()

    def get_json_from_post(self, url, data):
        return json.loads(self.client.post(url, data=data).data)

    def get_json_from_request(self, url, data={}, method="post"):
        return json.loads(getattr(self.client, method)(url, data=data).data)

    def get_json_from_get(self, url):
        return json.loads(self.client.get(url).data)

    def tearDown(self):
        BACKEND.clean()