from flask import Flask
from environment_variables import *
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "XXXXXXXXXX"
    app.config['RECAPTCHA_PUBLIC_KEY'] = "XXXXXXXXXXX"
    app.config['RECAPTCHA_PRIVATE_KEY'] = "XXXXXXXXXXX"
    from .views import views

    app.register_blueprint(views,url_prefix = '/')
    return app