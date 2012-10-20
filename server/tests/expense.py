from models import *
from base import TestApiBase

class ExpenseTest(TestApiBase):

    def setUp(self):

        TestApiBase.setUp(self)
        self.expense = self.create()["data"]

    def create(self):

        return self.get_json_from_post("/expense/", {"cost": 100, "name": "test", "user_id": self.user._id, "time": "test" })

    def _test_create(self):

        response = self.create()
        self.assertEquals(response["status"], "ok")

    def _test_get(self):

        response = self.get_json_from_get("/expense/%s/" % self.expense["_id"])
        self.assertEquals(response["name"], ["test"])
        self.assertEquals(response["cost"], ["100"])

    def _test_update(self):

        response = self.get_json_from_request("/expense/%s/" % self.expense["_id"], {"name": "new_value"}, method="put")
        self.assertEquals(response["status"], "ok")

        response = self.get_json_from_get("/expense/%s/" % self.expense["_id"])
        self.assertEquals(response["name"], "new_value")

    def _test_delete(self):

        self.new_expense = self.create()["data"]
        response = self.get_json_from_request("/expense/%s/" % self.new_expense["_id"], method="delete")
        self.assertEquals(response["status"], "ok")

        response = self.get_json_from_get("/expense/%s/" % self.new_expense["_id"])
        self.assertEquals(response["status"], "error")
