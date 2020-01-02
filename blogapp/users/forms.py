
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from blogapp.models import User 

class RegistrationForm (FlaskForm):
    username = StringField ('Username',
                validators = [DataRequired (), Length (min=4, max=20)])
    email = StringField ('Email',
                validators=[DataRequired (), Email ()])
    password = PasswordField ('Password',
                validators = [DataRequired (), Length (min=8, max=16)])
    confirm_password = PasswordField ('Confirm Password',
                validators = [DataRequired (), EqualTo ('password')])
    submit = SubmitField ('Sign Up')

    def validate_username (self, username):
        user = User.query.filter_by (username=username.data).first ()
        if user:
            raise ValidationError ('This Username Already exists, Please choose Another one!')
    
    def validate_email (self, email):
        user = User.query.filter_by (email=email.data).first ()
        if user:
            raise ValidationError ('This Email Already exists, Please choose Another one!')

class LoginForm (FlaskForm):
    
    email = StringField ('Email',
                validators=[DataRequired (), Email ()])
    password = PasswordField ('Password',
                validators = [DataRequired (), Length (min=8, max=16)])
    remember = BooleanField ('Remember Me')
    submit = SubmitField ('Login')

class UpdateAccountForm (FlaskForm):
    username = StringField ('Username',
                validators = [DataRequired (), Length (min=4, max=20)])
    email = StringField ('Email',
                validators=[DataRequired (), Email ()])
    picture = FileField ('Update Profile Picture', validators = [FileAllowed (['jpeg', 'jpg', 'png', 'jfif'])])
    
    submit = SubmitField ('Update')

    def validate_username (self, username):
        if username.data != current_user.username:
            user = User.query.filter_by (username=username.data).first ()
            if user:
                raise ValidationError ('This Username Already exists, Please choose Another one!')
    
    def validate_email (self, email):
        if email.data != current_user.email:
            user = User.query.filter_by (email=email.data).first ()
            if user:
                raise ValidationError ('This Email Already exists, Please choose Another one!')

class RequestResetForm (FlaskForm):
    email = StringField ('Email',
                validators=[DataRequired (), Email ()])
    submit = SubmitField ('Request Reset Password')

    def validate_email (self, email):
        user = User.query.filter_by (email=email.data).first ()
        if user is None:
            raise ValidationError ('There is no Account with that Email. Please register First!')

class ResetPasswordForm (FlaskForm):
    password = PasswordField ('Password',
                validators = [DataRequired (), Length (min=8, max=16)])
    confirm_password = PasswordField ('Confirm Password',
                validators = [DataRequired (), EqualTo ('password')])
    submit = SubmitField ('Reset Password')