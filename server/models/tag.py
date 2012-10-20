from models.base import BaseModel


class Tag(BaseModel):

    not_empty_fields = ["name"]
