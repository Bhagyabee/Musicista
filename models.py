from musicista import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    location = db.Column(db.String(10000))
    live = db.Column(db.String(10))
    event = db.Column(db.String(10000))

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    phone_no = db.Column(db.Integer)
    email = db.Column(db.String(150))
    message = db.Column(db.String(10000))
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    book = db.relationship('Book')