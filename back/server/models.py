from . import db
import time
import datetime


def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


db.Model.trans_to_dict = to_dict


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    userName = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(520), nullable=False)
    registerTime = db.Column(db.DateTime,  default=datetime.datetime.now())
    email = db.Column(db.String(120), unique=True, nullable=True)
    gender = db.Column(db.String(2), unique=False, nullable=True)
    age = db.Column(db.String(3), unique=False, nullable=True)
    goodAt = db.Column(db.String(520), nullable=True)
    onTime = db.Column(db.Integer, default=100)
    credit = db.Column(db.Integer, default=100)
    quality = db.Column(db.Integer, default=100)
    totalScore =  db.Column(db.Integer, default=300)
    price = db.Column(db.Integer, nullable=True)
    hasFinish = db.Column(db.Integer, nullable=False)
    oldProject = db.relationship('OldProject', backref='user', lazy='dynamic')
    release = db.relationship('ReleasePro', backref='employer', lazy='dynamic')
    apply = db.relationship('ApplyPro', backref='applyUser', lazy='dynamic')
    turnover = db.relationship('Turnover', backref='user', lazy='dynamic')
    headImg = db.Column(db.String(120), unique=False, default='default_head.jpg')
    profession = db.Column(db.String(10), unique=False, default='')
    synopsis = db.Column(db.String(15), unique=False, default='')
    employeeNum = db.Column(db.Integer, default=0)   # todo 当雇主次数
    notAppraised = db.Column(db.Integer, default=0)   # todo 未评价订单数
    status = db.Column(db.String(10), default='正常')   # todo 帐号状态
    BreachOfContract = db.Column(db.Integer, default=0)  # todo 违约次数
    employerScore = db.Column(db.Integer, default=100)
    balance = db.Column(db.Integer, default=0)
    deposit = db.Column(db.Integer, default=0)

    def __init__(self, phone, user_name, password, has_finish=0):
        self.userName = user_name
        self.password = password
        self.phone = phone
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
    releaseTime = db.Column(db.DateTime, default=datetime.datetime.now())
    applyAmount = db.Column(db.Integer, default=0)
    browse = db.Column(db.Integer, default=0)

    def __init__(self, employer_id, project_name, first_type, second_type, describe, budget, cycle, company):
        self.employerId = employer_id
        self.projectName = project_name
        self.firstType = first_type
        self.secondType = second_type
        self.describe = describe
        self.budget = budget
        self.cycle = cycle
        self.company = company

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
    ReleaseProId = db.Column(db.Integer, db.ForeignKey('releasepro.id'))
    applyUserId = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(db.String(10), default='申请中')
    applyTime = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, release_pro_id, apply_user_id):
        self.ReleaseProId = release_pro_id
        self.applyUserId = apply_user_id

    def __repr__(self):
        return '<Applypro %r>' % self.ReleaseProId


class ProOrder(db.Model):
    __tablename__ = 'proorder'
    id = db.Column(db.Integer, primary_key=True)
    applyId = db.Column(db.Integer)
    updateList = db.relationship('UpdateList', backref='proOrder', lazy='dynamic')
    employerId = db.Column(db.Integer)
    employeeId = db.Column(db.Integer)
    releaseId = db.Column(db.Integer)
    beginTime = db.Column(db.DateTime, default=datetime.datetime.now())
    deadlineTime = db.Column(db.DateTime, nullable=False)
    completionTime = db.Column(db.DateTime, nullable=True)
    progress = db.Column(db.Integer, default=0)
    credit = db.Column(db.Integer, default=0)
    quality = db.Column(db.Integer, default=0)
    onTime = db.Column(db.Integer, default=0)
    employerScore = db.Column(db.Integer, default=0)
    status = db.Column(db.String(10), default='进行中')
    evaluate = db.Column(db.String(200), nullable=True)  # todo 评价
    employerEvaluate = db.Column(db.String(200), nullable=True)  # todo 评价
    employerDep = db.Column(db.Integer, nullable=False)
    employeeDep = db.Column(db.Integer, nullable=False)

    def __init__(self, apply_id, employer_id, employee_id, release_id, deadline_time):
        self.applyId = apply_id
        self.employerId = employer_id
        self.employeeId = employee_id
        self.releaseId = release_id
        self.deadlineTime = deadline_time

    def __repr__(self):
        return '<ProOrder %r>' % self.id


class UpdateList(db.Model):
    __tablename__ = 'updatelist'
    id = db.Column(db.Integer, primary_key=True)
    orderId = db.Column(db.Integer, db.ForeignKey('proorder.id'))
    title = db.Column(db.String(12), nullable=False)
    desc = db.Column(db.String(30), nullable=False)
    fileDir = db.Column(db.String(200), default='')
    progress = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(10), default='pending')
    updateTime = db.Column(db.DateTime, default=datetime.datetime.now())
    rejectReason = db.Column(db.String(200), default='')

    def __init__(self, title, desc, progress, order_id):
        self.title = title
        self.desc = desc
        self.progress = progress
        self.orderId = order_id

    def __repr__(self):
        return '<updatelist %r>' % self.id


class Turnover(db.Model):
    __tablename__ = 'turnover'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    time = db.Column(db.DateTime, default=datetime.datetime.now())
    type = db.Column(db.String(10), nullable=False)
    quota = db.Column(db.Integer, nullable=False)
    balance = db.Column(db.Integer, nullable=False)
    deposit = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id, type, quota, balance, deposit):
        self.userId = user_id
        self.type = type
        self.quota = quota
        self.balance = balance
        self.deposit = deposit
        self.time = datetime.datetime.now()

    def __repr__(self):
        return '<turnover %r>' % self.type


class Appeal(db.Model):
    __tablename__ = 'appeal'
    id = db.Column(db.Integer, primary_key=True)
    complainantId = db.Column(db.Integer, nullable=False)
    defendanterId = db.Column(db.Integer, nullable=False)
    orderId = db.Column(db.Integer, nullable=False)
    reason = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(10), default='处理中')
    damages = db.Column(db.Integer, nullable=True)
    beginTime = db.Column(db.DateTime, default=datetime.datetime.now())
    endTime = db.Column(db.DateTime, nullable=True)
    winner = db.Column(db.Integer, nullable=True)

    def __init__(self, Complainant_id, defendanter_id, order_id, reason):
        self.complainantId = Complainant_id
        self.defendanterId = defendanter_id
        self.orderId = order_id
        self.reason = reason

    def __repr__(self):
        return '<appeal %r>' % self.id



class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    adminName = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(520), nullable=False)

    def __init__(self, admin_Name, password):
        self.adminName = admin_Name
        self.password = password


    def __repr__(self):
        return '<admin %r>' % self.id
