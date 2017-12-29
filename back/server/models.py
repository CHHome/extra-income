from . import db
import time


class Users(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(520), nullable=False)
    register_time = db.Column(db.String(32), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    gender = db.Column(db.String(2), unique=False, nullable=True)
    age = db.Column(db.String(3), unique=False, nullable=True)

    def __init__(self, phone, username, password, register_time=time.time()):
        self.username = username
        self.password = password
        self.phone = phone
        self.register_time = register_time

    def __repr__(self):
        return '<User %r>' % self.username



#
# class Admin(db.Model):
#     __tablename__ = 'admins'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(320), unique=True)
#     password = db.Column(db.String(32), nullable=False)
#
#     def __repr__(self):
#         return '<User %r>' % self.username