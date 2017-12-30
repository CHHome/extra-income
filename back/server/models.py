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


class UserInfo(db.Model):
    __tablename__ = 'userInfo'
    id = db.Column(db.Integer, primary_key=True)
    good_at = db.Column(db.String(64), nullable=False)
    on_time = db.Column(db.Integer, nullable=False)
    credit = db.Column(db.Integer, nullable=False)
    quality = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    has_finish = db.Column(db.Integer, nullable=False)

    def __init__(self, id, good_at='', on_time=0, quality=0, price=0, has_finish=0, credit=0):
        self.id = id
        self.good_at = good_at
        self.on_time = on_time
        self.credit = credit
        self.quality = quality
        self.price = price
        self.has_finish = has_finish

    def __repr__(self):
        return '<userInfo %r>' % self.id


# class Admin(db.Model):
#     __tablename__ = 'admins'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(320), unique=True)
#     password = db.Column(db.String(32), nullable=False)
#
#     def __repr__(self):
#         return '<User %r>' % self.username