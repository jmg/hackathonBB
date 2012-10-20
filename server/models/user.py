from base import BaseModel


class User(BaseModel):
    __PRIMARY_KEY__ = 'username'

    def validate(self):
        
        for field in ['username', 'password', 'email']:
            self.validate_not_empty(field)