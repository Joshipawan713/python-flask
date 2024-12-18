from flask import Flask
from .views import main

def create_app():
    app = Flask(__name__)
    app.secret_key = 'Flask_Secret_Key'
    app.register_blueprint(main)
    return app