from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField,BooleanField
from wtforms.validators import DataRequired, Length, Email,EqualTo
#from app.modelss         import User

class signupForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(min = 2,max = 20)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired(), Length(min = 2, max=20)])
    confirm = PasswordField('Repeat Password', validators = [DataRequired(),EqualTo('password')])
    submit = SubmitField(('Register'))

 #   def validate_username(self, username):

 #       user = User.query.filter_by(username = username.data).first()

 #      if user is not None:
 #           raise ValidationError(_("username is taken. roll again."))

  #  def validate_email(self, email):

  #      user = User.query.filter_by(email = email.data).first()

  #      if user is not None:
        #    raise ValidationError(_("this email is already in our system"))

class loginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(min = 6,max = 20)])
    password = PasswordField('Password', validators = [DataRequired(), Length(min = 8, max=20)])
    #remember_me = BooleanField(('remember me'))
    submit = SubmitField('Log in')
