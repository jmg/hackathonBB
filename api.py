from app import app
import simplejson as json

def json_response(dict):

    return json.dumps(dict)

@app.route("/")
def budgets():
    
    client = Client("jmg.utn@hotmail.com", "python")
    return json_response(client.get("budgets"))
