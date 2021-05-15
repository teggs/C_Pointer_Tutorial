from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,ValidationError,BooleanField
from wtforms.validators import DataRequired, Length, Email,EqualTo
from app.modelss import User


class signupForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(min = 2,max = 20)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired(), Length(min = 2, max=20)])
    confirm = PasswordField('Repeat Password', validators = [DataRequired(),EqualTo('password')])
    style={'style': 'width:50%;background-color:orange'}
    submit = SubmitField("Sign up",render_kw = style)

    #validate the username
    def validate_username(selfself,username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError("Username is already taken,please choose another one.")
        if type(username) == int:
            raise ValidationError("Username name can not only the number")
        #if username == password:
        #    raise ValidationError("password can not same as the username ")

    #validate the email
    def validate_email(selfself,email):
        email = User.query.filter_by(email = email.data).first()
        if email:
            raise ValidationError("Email is already taken.")

class loginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(min = 2,max = 20)])
    password = PasswordField('Password', validators = [DataRequired(), Length(min =2, max=20)])
    remember = BooleanField('Remember')
    style = {'style': 'width:50%;background-color:orange'}
    submit = SubmitField("Login", render_kw=style)