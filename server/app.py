from flask import Flask
app = Flask(__name__)

app.config.update(
    SECRET_KEY='fhdjhfsdjkfhjksdf'
)

from api import *

if __name__ == "__main__":

    app.run(debug=True)