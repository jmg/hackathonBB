from mongomodels.models import ValidatingStruct
from settings import BACKEND


class BaseModel(ValidatingStruct):
    
    __DOCUMENT_DB__ = BACKEND

    def validate(self):
        
        for field in getattr(self, "not_empty_fields", []):
            self.validate_not_empty(field)
