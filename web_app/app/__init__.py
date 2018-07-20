from flask import Flask
from flask_moment import Moment


def create_app(config=None):
    app = Flask(__name__)

    if config is not None:
        app.config.from_object(config)

    Moment(app)

    from .aws.views import aws
    app.register_blueprint(aws, url_prefix='/')


    return app
