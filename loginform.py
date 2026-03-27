from flask_wtf import FlaskForm
from wtforms import RadioField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

class Logindetails(FlaskForm):
    username = StringField(label = "", validators=[DataRequired()]) # cinopypaste ko naalng para mabilis
    password = PasswordField(label = "", validators=[DataRequired()])
    submit = SubmitField("Login")