from models.base import BaseModel
from models.user import User


class Config(BaseModel):

    not_empty_fields = []

    def validate(self):
        
        BaseModel.validate(self)
        self.validate_existance('user_id', User)
