try:
    import simplejson as json
except ImportError:
    import json

from functools import wraps
from flask import request, Response

def check_auth(username, password):
    return True

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

def response_error(params={}):

    params["status"] = "error"
    return json.dumps(params)

def response_success(params={}):

    params["status"] = "ok"
    return json.dumps(params)

def json_response(params={}, success=True):
    
    if success:
        return response_success(params=params)
    return response_error(params=params)
