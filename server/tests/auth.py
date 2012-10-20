from models import *
from base import TestApiBase

class AuthTest(TestApiBase):

    def setUp(self):

        TestApiBase.setUp(self)

    def create_user(self):
        pass

    def test_auth(self):

        response = self.get_json_from_post("/login/", {"username": "test", "password": "test"})
        self.assertEquals(response["status"], "ok")     

    def test_already_registered_user(self):

        data = {"username": "test", "password": "test"}
        user = User(**data)
        user.save()

        response = self.get_json_from_post("/login/", data)
        self.assertEquals(response["status"], "ok")     

    def test_password(self):

        response = self.get_json_from_post("/login/", {"username": "test", "password": "test"})
        response = self.get_json_from_post("/password/change/", {"password": "test"})
        self.assertEquals(response["status"], "ok")        