from models.base import BaseModel
from models.user import User


class Expectation(BaseModel):

    not_empty_fields = ['cost', 'description']
    __PRIMARY_KEY__ = 'user_id'

    def validate(self):
        super(Expectation, self).validate()
        self.validate_existance('user_id', User)
