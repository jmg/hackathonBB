from utils import *
from mongomodels.models.exceptions import ValidationException, NotFoundException

def save(entity_class, request, entity_id=None):
    
    if entity_id is not None:
        entity = entity_class.get(_id=entity_id)
        entity.__dict__.update(**request.form)
    else:
        entity = entity_class(**request.form)

    try:
        _, saved = entity.save()
    except ValidationException, e:
        return response_error()
    
    return response_success(params={'data': entity.json})

def get(entity_class, id):
    
    try:
        entity = entity_class.get(_id=id)
    except NotFoundException, e:
        return response_error()

    return entity.json_string

def delete(entity_class, id):
    
    try:
        entity = entity_class.get(_id=id)
        entity.delete()
    except NotFoundException, e:
        return response_error()

    return response_success()
    