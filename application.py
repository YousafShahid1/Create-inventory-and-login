from application import app,db
from config.admin import Admin



if __name__ == "__main__":
   
    app.app_context().push()
    db.create_all()
    Admin.create_admin()
    app.run(debug=True)


