from flask import Flask, redirect, url_for, send_from_directory, Blueprint
from flask import render_template


blueprint_index = Blueprint('index', __name__, template_folder='templates', static_folder='static')

@blueprint_index.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html')

@blueprint_index.route('/download_cv', methods=["GET", "POST"])
def download_cv():
    return send_from_directory('static', 'guolewen.pdf')

