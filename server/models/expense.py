from models.base import BaseModel
from models.user import User


class Expense(BaseModel):

    def validate(self):
        self.validate_not_empty('cost')
        self.validate_not_empty('name')
        self.validate_not_empty('time')
        self.validate_existance('user_id', User)
