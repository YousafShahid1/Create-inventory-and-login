from application import db
from application.models.user import User
from werkzeug.security import generate_password_hash



class Admin:
    def create_admin():
        admin = User.query.filter_by(user_type = "admin").first()
        
        if admin:
            print("Admin Already Exist")
            return False
        else:
            admin = User(email="theadmin@gmail.com",password=generate_password_hash("Admin"),user_type="admin")
            db.session.add(admin)
            db.session.commit()
           
            print("Admin Created Successfully")
            return True




