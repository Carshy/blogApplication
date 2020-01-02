import os
import secrets
from PIL import Image
from flask import current_app, url_for
from flask_mail import Message
from blogapp import mail

def save_picture (form_picture):
    random_hex = secrets.token_hex (8)
    _, f_ext = os.path.splitext (form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join (current_app.root_path, 'static/profile_pics', picture_fn)
    
    out_size = (125, 125)
    i = Image.open (form_picture)
    i.thumbnail (out_size)
    i.save (picture_path)
    
    return picture_fn

def send_reset_email (user):
    token = user.get_reset_token ()
    msg = Message ('Password Reset Request', sender = 'mussocollins@gmail.com', recipients=[user.email])
    msg.body = f'''To Reset your Password, Visit the Following Link:
{url_for ('users.reset_token', token=token, _external=True)}

If you did not make this Request Kindly Ignore this email and no changes will be made
'''
    mail.send (msg)
