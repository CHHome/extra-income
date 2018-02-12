from . import db
import time


def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


db.Model.trans_to_dict = to_dict


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
    totalScore =  db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=True)
    hasFinish = db.Column(db.Integer, nullable=False)
    oldProject = db.relationship('OldProject', backref='user', lazy='dynamic')
    release = db.relationship('ReleasePro', backref='employer', lazy='dynamic')
    headImg = db.Column(db.String(120), unique=False, default='default_head.jpg')
    profession = db.Column(db.String(10), unique=False, default='')
    synopsis = db.Column(db.String(15), unique=False, default='')

    def __init__(self, phone, user_name, password, register_time=time.time(), on_time=0, credit=0, quality=0,
                 total_score=0, has_finish=0):
        self.userName = user_name
        self.password = password
        self.phone = phone
        self.registerTime = register_time
        self.onTime = on_time
        self.credit = credit
        self.quality = quality
        self.hasFinish = has_finish
        self.totalScore = total_score

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
            'profession': self.profession,
            'synopsis': self.synopsis

        }

    def to_show(self):
        return {
            'id': self.id,
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
            'profession': self.profession,
            'synopsis': self.synopsis
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


class ReleasePro(db.Model):
    __tablename__ = 'releasepro'
    id = db.Column(db.Integer, primary_key=True)
    employerId = db.Column(db.Integer, db.ForeignKey('user.id'), unique=False)
    apply = db.relationship('ApplyPro', backref='releasePro', lazy='dynamic')
    projectName = db.Column(db.String(30), nullable=False)
    firstType = db.Column(db.String(10), nullable=False)
    secondType = db.Column(db.String(10), nullable=False)
    describe = db.Column(db.String(500), nullable=False)
    budget = db.Column(db.Integer, nullable=False)
    cycle = db.Column(db.Integer, nullable=False)
    company = db.Column(db.String(30), nullable=True)
    status = db.Column(db.String(10), default='招募中')
    releaseTime = db.Column(db.String(32), nullable=False)
    applyAmount = db.Column(db.Integer, default=0)
    browse = db.Column(db.Integer, default=0)

    def __init__(self, employer_id, project_name, first_type, second_type, describe, budget, cycle, company, release_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())):
        self.employerId = employer_id
        self.projectName = project_name
        self.firstType = first_type
        self.secondType = second_type
        self.describe = describe
        self.budget = budget
        self.cycle = cycle
        self.company = company
        self.releaseTime = release_time

    def __repr__(self):
        return '<Release %r>' % self.projectName


# class Admin(db.Model):
#     __tablename__ = 'admins'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(320), unique=True)
#     password = db.Column(db.String(32), nullable=False)
#
#     def __repr__(self):
#         return '<User %r>' % self.username

class ApplyPro(db.Model):
    __tablename__ = 'applypro'
    id = db.Column(db.Integer, primary_key=True)
    ReleaseProId = db.Column(db.Integer, db.ForeignKey('releasepro.id'), unique=False)
    applyUserId = db.Column(db.Integer)
    status = db.Column(db.String(10), default='申请中')
    applyTime = db.Column(db.String(32), nullable=False)

    def __init__(self, release_pro_id, apply_user_id, apply_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())):
        self.ReleaseProId = release_pro_id
        self.applyUserId = apply_user_id
        self.applyTime = apply_time

    def __repr__(self):
        return '<Applypro %r>' % self.ReleaseProId
