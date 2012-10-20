from models import *
from base import TestApiBase

class ExpenseTest(TestApiBase):

    def test_crud(self):

        response = self.get_json_from_post("/expense/", {"cost": 100, "name": "test", "user_id": self.user._id })
        self.assertEquals(response["status"], "ok")

        response = self.get_json_from_get("/expense/1/")
        self.assertEquals(response["data"]["name"], "test")
        self.assertEquals(response["data"]["password"], "test")

        response = get_json_from_request("/expense/1/", {"name": "new_value"}, method="put")
        self.assertEquals(response["status"], "ok")

        response = self.get_json_from_get("/expense/1/")
        self.assertEquals(response["data"]["name"], "new_value")

        response = self.get_json_from_request("/expense/1/", method="delete")
        self.assertEquals(response["status"], "ok")
