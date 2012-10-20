from base import BaseModel


class User(BaseModel):
    
    __PRIMARY_KEY__ = 'username'

    not_empty_fields = ['username', 'password', 'email']