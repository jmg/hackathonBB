from app import app

from models import *
from utils import *
import crud

def get_resource_class(resource):

    return globals().get(resource.capitalize())

@app.route("/<resource>/", methods=["POST"])
def create_entity(resource):

    resource_class = get_resource_class(resource)
    return crud.save(resource_class, request)

@app.route("/<resource>/<entity_id>/", methods=["GET"])
def get_entity(resource, entity_id):

    resource_class = get_resource_class(resource)
    return crud.get(resource_class, entity_id)

@app.route("/<resource>/<entity_id>/", methods=["PUT"])
def update_entity(resource, entity_id):

    resource_class = get_resource_class(resource)
    return crud.save(resource_class, request, entity_id=entity_id)

@app.route("/<resource>/<entity_id>/", methods=["DELETE"])
def delete_entity(resource, entity_id):

    resource_class = get_resource_class(resource)
    return crud.delete(resource_class, entity_id)

@app.route("/report/progress/<user_id>/", methods=["GET"])
def progress(user_id):
    try:
        return response_success(data=User.get(_id=user_id).progress())
    except:
        return response_error()

@app.route("/report/expenses/<user_id>/", methods=["GET"])
def expenses_by_user(user_id):
    try:
        return response_success(data=Expense.all_json(user_id=user_id))
    except:
        return response_error()

@app.route("/report/expenses/<user_id>/<tag>/", methods=["GET"])
def expenses_by_tag(user_id, tag):
    try:
        tag_id = Tag.get(name=tag)['_id']
        return response_success(data=Expense.all_json(user_id=user_id, tag_id=tag_id))
    except:
        return response_error()


@app.route("/tags/", methods=["GET"])
def tags():
    return response_success(data=Tag.all_json())
