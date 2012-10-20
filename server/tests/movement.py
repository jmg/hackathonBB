from models import *
from base import TestApiBase

class MovementTest(TestApiBase):
    movement_type = None

    def setUp(self):

        TestApiBase.setUp(self)
        self.movement = self.create()["data"]
        self.docs = ['expense', 'income', 'user', 'tag']

    def create(self):
        return self.get_json_from_post("/%s/" % (self.movement_type,), {"cost": 100, "name": "test", "user_id": self.user._id, "time": "test", "tag_id": Tag.get(name='saving')['_id'] })

    def test_create(self):

        response = self.create()
        self.assertEquals(response["status"], "ok")

    def test_get(self):

        response = self.get_json_from_get("/%s/%s/" % (self.movement_type, self.movement["_id"]))
        self.assertEquals(response["name"], "test")
        self.assertEquals(response["cost"], "100")

    def test_update(self):

        response = self.get_json_from_request("/%s/%s/" % (self.movement_type, self.movement["_id"]), {"name": "new_value"}, method="put")
        self.assertEquals(response["status"], "ok")

        response = self.get_json_from_get("/%s/%s/" % (self.movement_type, self.movement["_id"]))
        self.assertEquals(response["name"], "new_value")

    def test_delete(self):

        self.new_movement = self.create()["data"]
        response = self.get_json_from_request("/%s/%s/" % (self.movement_type, self.new_movement["_id"]), method="delete")
        self.assertEquals(response["status"], "ok")

        response = self.get_json_from_get("/%s/%s/" % (self.movement_type, self.new_movement["_id"]))
        self.assertEquals(response["status"], "error")

class ExpenseTest(MovementTest):
    movement_type = 'expense'

class IncomeTest(MovementTest):
    movement_type = 'income'
