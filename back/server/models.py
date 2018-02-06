from . import db
import time


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    userName = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(520), nullable=False)
    registerTime = db.Column(db.String(32), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    gender = db.Column(db.String(2), unique=False, nullable=True)
    age = db.Column(db.String(3), unique=False, nullable=True)
    goodAt = db.Column(db.String(520), nullable=True)
    onTime = db.Column(db.Integer, nullable=False)
    credit = db.Column(db.Integer, nullable=False)
    quality = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=True)
    hasFinish = db.Column(db.Integer, nullable=False)
    oldProject = db.relationship('OldProject', backref='user', lazy='dynamic')
    headImg = db.Column(db.String(120), unique=False, default='default_head.jpg')

    def __init__(self, phone, user_name, password, register_time=time.time(), on_time=0, credit=0, quality=0,
                 has_finish=0):
        self.userName = user_name
        self.password = password
        self.phone = phone
        self.registerTime = register_time
        self.onTime = on_time
        self.credit = credit
        self.quality = quality
        self.hasFinish = has_finish

    def __repr__(self):
        return '<Users %r>' % self.userName

    def to_dict(self):
        return {
            'id': self.id,
            'phone': self.phone,
            'userName': self.userName,
            'registerTime': self.registerTime,
            'email': self.email,
            'gender': self.gender,
            'age': self.age,
            'goodAt': self.goodAt,
            'onTime': self.onTime,
            'credit': self.credit,
            'quality': self.quality,
            'price': self.price,
            'hasFinish': self.hasFinish,
            'headImg': self.headImg,
        }

    def to_show(self):
        return {
            'userName': self.userName,
            'email': self.email,
            'gender': self.gender,
            'age': self.age,
            'goodAt': self.goodAt,
            'onTime': self.onTime,
            'credit': self.credit,
            'quality': self.quality,
            'price': self.price,
            'hasFinish': self.hasFinish,
            'headImg': self.headImg,
        }


class OldProject(db.Model):
    __tablename__ = 'oldproject'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), unique=False)
    proName = db.Column(db.String(30), unique=False, nullable=False)
    player = db.Column(db.String(20), unique=False, nullable=False)
    industry = db.Column(db.String(20), unique=False, nullable=False)
    headImg = db.Column(db.String(30), unique=False, default='project/default_pro.jpg')
    linkTo = db.Column(db.String(100), unique=False, default='')
    describe = db.Column(db.String(200), unique=False, default='')

    def __init__(self, user_id, pro_name, player, industry):
        self.proName = pro_name
        self.userId = user_id
        self.player = player
        self.industry = industry

    def __repr__(self):
        return '<OldProject %r>' % self.proName

    def to_dict(self):
        return{
            'id': self.id,
            'userId': self.userId,
            'proName': self.proName,
            'player': self.player,
            'industry': self.industry,
            'headImg': self.headImg,
            'linkTo': self.linkTo,
            'describe': self.describe
        }

# class Admin(db.Model):
#     __tablename__ = 'admins'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(320), unique=True)
#     password = db.Column(db.String(32), nullable=False)
#
#     def __repr__(self):
#         return '<User %r>' % self.username