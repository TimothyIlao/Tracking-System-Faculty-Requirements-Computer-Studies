from flask_wtf import FlaskForm
from wtforms import EmailField,RadioField,StringField,PasswordField,TextAreaField,SelectField,IntegerField,SubmitField
from wtforms.validators import ValidationError, DataRequired

class trackingsystem(FlaskForm):
    username = StringField(label = "Username:", validators=[DataRequired()]) # naglalaman din ng error fill text basta may data required
    password = PasswordField(label = "Password:", validators=[DataRequired()]) # naglalaman to ng error fill text
    email = EmailField(label = "email")
    gender = RadioField(label = "Select Gender:", choices=["Male", "Female"])
    birth_year = SelectField("Year", choices=[("", "YYYY")]+[(str(y), str(y)) for y in range(1945, 2026)])
    birth_month = SelectField("Month", choices=[("", "MM")]+[(str(m), str(m)) for m in range(1, 13)])
    birth_day = SelectField("Day", choices=[("", "DD")]+[(str(d), str(d)) for d in range(1, 32)])
    submit = SubmitField("Register")