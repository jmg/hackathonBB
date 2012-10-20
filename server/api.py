from app import app

from flask import request

from mongomodels.models.exceptions import NotFoundException
from models import *
from utils import *
import crud

def get_resource_class(resource):

    return globals().get(resource.capitalize())

@app.route("/<resource>/", methods=["GET"])
def list_entity(resource):

    resource_class = get_resource_class(resource)
    return response_success(params={"data":crud.all(resource_class, request=request)})

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

@app.route("/account/create/", methods=["POST"])
def create_account():

    username = request.form.get("username")
    password = request.form.get("password")

    user = User(username=username, password=password)
    user.save()

    set_user(user)
    return response_success()

@app.route("/expectation/", methods=["GET"])
def get_expectation():
    try:
        return response_success(data=Expectation.get(user_id=get_user()['_id']).json)
    except:
        return response_error()

@app.route("/expectation/", methods=["POST", "PUT"])
def create_or_update_expectation():
    try:
        try:
            expectation = Expectation.get(user_id=get_user()['_id'])
            expectation.__dict__.update(**clean_data(request.form))
        except NotFoundException:
            expectation = Expectation(user_id=get_user()['_id'], **clean_data(request.form))

        expectation.save()
        return response_success(data=expectation.json)
    except:
        return response_error()

@app.route("/login/", methods=["POST"])
def login():

    username = request.form.get("username")
    password = request.form.get("password")

    try:
        user = User.get(username=username, password=password)
    except NotFoundException:
        user = User(username=username, password=password)
        user.save()

    set_user(user)
    return response_success()

@app.route("/password/change/", methods=["POST"])
def change_password():

    user = get_user()
    user.password = request.form.get("password")
    user.save()
    return response_success()

@app.route("/report/progress/", methods=["GET"])
def progress():
    try:
        return response_success(data=User.get(_id=get_user()['_id']).progress())
    except:
        return response_error()

@app.route("/report/expenses/", methods=["GET"])
def expenses_by_user():
    try:
        return crud.all("expense")
    except:
        return response_error()

@app.route("/report/expenses/<tag>/", methods=["GET"])
def expenses_by_tag(tag):
    try:
        tag_id = Tag.get(name=tag)['_id']
        return response_success(data=crud.all("expense", tag_id=tag_id))
    except:
        return response_error()

@app.route("/report/expenses/top/", methods=["GET"])
def top_expenses():
    try:
        return response_success(data=Expense.top(user_id=get_user()['_id']))
    except:
        return response_error()

@app.route("/report/expenses/top/<tag>/", methods=["GET"])
def top_expenses_for(tag):
    try:
        return response_success(data=Expense.top(tag=tag, user_id=get_user()['_id']))
    except:
        return response_error()

@app.route("/report/incomes/", methods=["GET"])
def incomes_by_user():
    try:
        return crud.all("income")
    except:
        return response_error()

@app.route("/tags/", methods=["GET"])
def tags():
    return response_success(data=Tag.all_json())
