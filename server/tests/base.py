import unittest
import json

from settings import BACKEND
import os
from app import app

from models import User, Tag


class TestApiBase(unittest.TestCase):

    def setUp(self):

        app.testing = True
        self.client = app.test_client()
        self.user = User(username="test", password="test", email="test@test.com")
        self.create_tags()
        self.user.save()
        self.docs = []

    def create_tags(self):
        Tag(name='saving').save()
        Tag(name='lalala').save()

    def get_json_from_post(self, url, data):
        return json.loads(self.client.post(url, data=data).data)

    def get_json_from_request(self, url, data={}, method="get"):
        return json.loads(getattr(self.client, method)(url, data=data).data)

    def get_json_from_get(self, url):
        return json.loads(self.client.get(url).data)

    def tearDown(self):
        for doc in self.docs:
            BACKEND.teardown(doc)

        if os.environ.get("API_ENV", None) is not None:
            BACKEND.clean()
