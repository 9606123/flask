from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from datetime import datetime

class User(db.Model):
    """
    Create an Users Table
    """
    __tablename__='user_info'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """
        Prevent password from being accessed
        """
        raise AttributeError('pass word is not readable attribute')

    @password.setter
    def password(self, password):
        # Set Password to a hashed password
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password 
        """
        return check_password_hash(self.password_hash, password)

    def to_json(self):
        result = {
            'id': self.id,
            'username': self.username,
            'is_admin': self.is_admin
        }
        return result

    def __repr__(self):
        return "<User: {}>".format(self.username)


class Blogs(db.Model):

    __tablename__ = 'blogs'
    
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100), unique=True)
    blogpic = db.Column(db.String(50))
    content = db.Column(db.Text)
    category = db.Column(db.String(50))
    hits = db.Column(db.Integer, default=0)
    author = db.Column(db.String(50))
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now)

    
    def __repr__(self):
        return "<blogs: {}>".format(self.name)

