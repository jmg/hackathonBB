from models.base import BaseModel
from models.movement import Movement


class Tag(BaseModel):

    not_empty_fields = ["name"]

    def validate(self):
        
        BaseModel.validate(self)
        self.validate_existance('movement_id', Movement)
