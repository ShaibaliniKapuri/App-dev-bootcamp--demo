from flask import Flask
from website.model import db, User, Post
from website.config import DevelopmentConfig
from flask_login import LoginManager

def create_admin_user():
    admin_email = 'admin@example.com'
    admin_password = 'admin123'
    if not User.query.filter_by(email=admin_email).first():
        admin = User(username='admin', email=admin_email, role='admin')
        admin.set_password(admin_password)
        db.session.add(admin)
        db.session.commit()
        print("Admin user created!")

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    with app.app_context():
        db.create_all()
        create_admin_user()
        import website.views
        import website.auth

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)
    # Load user for Flask-Login
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))



    return app

my_app = create_app()

if __name__ == "__main__":
    my_app.run(debug = True)