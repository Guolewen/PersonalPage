from flask import Flask, redirect, url_for, send_from_directory
from flask import render_template
import os
from flask_wtf import Form
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, length


class ContactForm(Form):
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


