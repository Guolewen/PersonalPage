from flask import Flask
import os


def create_app(object_name):
    from .index.main_index import blueprint_index

    # Not completed yet   This should add administration page
    # from .admin import create_module as blueprint_admin .
    app = Flask(__name__)
    app.config.from_object(object_name)
    app.register_blueprint(blueprint_index)
    return app