"""
Flask server for the pictures microservice
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """
    Home route for the pictures microservice
    """
    return "Hello"
