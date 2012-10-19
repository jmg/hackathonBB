import requests
import simplejson as json

class Client(object):

    BASE_URL = "https://www.buxfer.com/api"

    def __init__(self, user, password):

        self.user = user
        self.password = password
        self.login()

    def login(self):

        login_url = self.get_login_url()
        data = self.get_response(login_url)
        self.token = data["token"]

    def get_login_url(self):

        return self.BASE_URL + "/login.json?userid=" + self.user + "&password=" + self.password

    def get_response(self, url):

        response = requests.get(url)
        data = json.loads(response.text)
        data = data["response"]
        if data["status"] != "OK":
            raise Exception(str(data))

        return data

    def get(self, name):

        url = "%s/%s.json?token=%s" % (self.BASE_URL, name, self.token)
        return self.get_response(url)