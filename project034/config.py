import os
from flask_sqlalchemy import make_url
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "sdkHHKGYITfjlqjluio23uaasdf42903"
    
    @staticmethod
    def init_app(app):
        pass

class LocalConfig(Config):
    SECRET_KEY = "sdkfjlasdf%$^%^&qjluio23asdfu42903"
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:123456@127.0.0.1/blogsdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

config = {
    'local': LocalConfig,
    'default': LocalConfig,
}
