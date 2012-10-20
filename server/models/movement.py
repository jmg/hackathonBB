from models.base import BaseModel


class Movement(BaseModel):

    not_empty_fields = ["cost", "name", 'time']