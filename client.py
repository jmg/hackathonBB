import requests
import simplejson as json


class Client(object):

    BASE_URL = "https://www.buxfer.com/api"
    LOGIN_URL = "%s/login.json" % BASE_URL

    def __init__(self, user, password):

        self.user = {"userid": user, "password": password }
        self.login()

    def login(self):

        data = self.get_response(self.LOGIN_URL, self.user)
        self.token = data["token"]

    def get_response(self, url, params={}):

        response = requests.get(url, params=params)
        data = json.loads(response.text)
        data = data["response"]
        if data["status"] != "OK":
            raise Exception(str(data))

        return data

    def get(self, name, params={}):

        params["token"] = self.token

        url = "%s/%s.json" % (self.BASE_URL, name)
        return self.get_response(url, params)