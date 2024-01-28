import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
 
app = Flask (__name__)
app.config['SECRET_KEY'] = 'acd98960cc7d85c17eca36fe4a4636e9'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///site.db'
db = SQLAlchemy(app) 
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'
# app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'mankudevserver@gmail.com'
app.config['MAIL_PASSWORD'] = 'ihjl zxhx kbfp wyxl'
mail = Mail(app)



from server import routes