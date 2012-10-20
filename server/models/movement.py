from models.base import BaseModel
from models.user import User

class Movement(BaseModel):

    not_empty_fields = ["cost", "name", 'time']

    def validate(self):
        super(Movement, self).validate()
        self.validate_existance('user_id', User)
