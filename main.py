from flask import Flask, redirect, url_for, send_from_directory
from flask import render_template
import os
import lib.click
from lib.flask_wtf import FlaskForm
from lib.wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from lib.wtforms.validators import InputRequired, Email, length


class ContactForm(FlaskForm):
    name = StringField("Your Name", validators=[InputRequired("Please enter your name"), length(max=150)])
    title = StringField("Title", validators=[length(max=100)])
    email = StringField("Your E-mail", validators=[Email("Please enter correct E-mail address"), length(max=100)])
    content = TextAreaField("Contents", validators=[length(max=100)])


app = Flask(__name__)
app.config ['SECRET_KEY'] = os.urandom(24)

# I add a text


@app.route('/', methods=["GET", "POST"])
def hello_world():
    form = ContactForm()
    if form.validate_on_submit():
        print("validated")
        return render_template('index.html', form=form)
    return render_template('index.html', form=form)

@app.route('/send_mail', methods=["GET", "POST"])
def email():
    return


@app.route('/download_cv', methods=["GET", "POST"])
def download_cv():
    return send_from_directory('static', 'guolewen.pdf')


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)