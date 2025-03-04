class Config:
    
    SECRET_KEY = 'your_secret_key_here'

    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    
    LOGIN_VIEW = 'login'  

class DevelopmentConfig(Config):
    DEBUG = True  

