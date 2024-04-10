from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'oasjdoajsodo21ojasodj' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

from application.routes.auth import auth
app.register_blueprint(auth)

from application.routes.ingredient import ingredient
app.register_blueprint(ingredient)

from application.routes.inventory import inventory
app.register_blueprint(inventory)


