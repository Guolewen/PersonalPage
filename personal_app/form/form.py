from lib.flask_wtf import FlaskForm
from lib.wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from lib.wtforms.validators import InputRequired, Email, length


class ContactForm(FlaskForm):
    name = StringField("Your Name", validators=[InputRequired("Please enter your name"), length(max=150)])
    title = StringField("Title", validators=[length(max=100)])
    email = StringField("Your E-mail", validators=[Email("Please enter correct E-mail address"), length(max=100)])
    content = TextAreaField("Contents", validators=[length(max=100)])