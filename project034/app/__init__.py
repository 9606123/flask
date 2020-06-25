from flask import Flask, redirect, url_for, render_template
from config import config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy(use_native_unicode='utf8')

def create_app(config_name):
    app = Flask(__name__)
    try:
        app.config.from_object(config[config_name])
        config[config_name].init_app(app)
    except Exception as e:
        print('config {}'.format(app.config))
        print(e)
   
    bootstrap=Bootstrap(app)
    db.init_app(app)

    # @app.route("/")
    # def index():
    #     # return render_template('index.html')
    #     return redirect(url_for("blogs.index"))

    from .blogs import blogs as blogs_blueprint
    app.register_blueprint(blogs_blueprint, url_prefix='/')

    from .auth import account as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/account')

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    return app
