from application import app,db
from application.models.user import User
from application.forms.login_form import LoginForm
from flask import Blueprint,render_template,flash,redirect,request,url_for
from flask_login import login_user, logout_user, login_required,current_user
from werkzeug.security import check_password_hash

from functools import wraps


auth = Blueprint('auth',__name__, template_folder='templates')


def guest_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect(url_for('inventory.admin_dashboard'))
        return f(*args, **kwargs)
    return decorated_function

@auth.route('/login', methods=['GET', 'POST'])
@guest_required
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password,form.password.data):
            if user.user_type == "admin":
                login_user(user)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('inventory.admin_dashboard'))
            else:
                flash('Login Unsuccessful. Please check email and password', 'danger')
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))