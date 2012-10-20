from mongomodels.models import ValidatingStruct
from settings import BACKEND


class BaseModel(ValidatingStruct):
    __DOCUMENT_DB__ = BACKEND
