from flask import Flask
import os


def create_app(object_name):
    from .homepage.main_index import blueprint_index
    from .form.form import blueprint_form
    # Not completed yet   This should add administration page
    # from .admin import create_module as blueprint_admin .
    app = Flask(__name__)
    app.config.from_object(object_name)
    app.register_blueprint(blueprint_index)
    app.register_blueprint(blueprint_form)
    app.jinja_env.filters['zip'] = zip
    return app