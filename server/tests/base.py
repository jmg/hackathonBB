import unittest
import json

from settings import BACKEND

class TestChatBase(unittest.TestCase):

    def get_json_from_post(self, url, data):
            return json.loads(self.client.post(url, data=data).data)

    def get_json_from_get(self, url):
        return json.loads(self.client.get(url).data)

    def tearDown(self):
        BACKEND.clean()
