from flask.ext import restful
from flask_restful import reqparse
from flask.ext.restful import fields, marshal_with, marshal
from ..models import User, ReleasePro
from .. import db


class Recommend(restful.Resource):
    def get(self):
        employees = User.query.order_by(db.desc(User.totalScore)).limit(8).all()
        releasePro = ReleasePro.query.filter_by(status='招募中').order_by(db.desc(ReleasePro.budget)).limit(8).all()
        result = dict()
        employeeList = list()
        releaseProList = list()
        result['employeeList'] = employeeList
        result['releaseProList'] = releaseProList
        for item in employees:
            item.registerTime = item.registerTime.strftime("%Y-%m-%d %H:%M:%S")
            employeeList.append(item.trans_to_dict())
        for item in releasePro:
            item.releaseTime = item.releaseTime.strftime("%Y-%m-%d %H:%M:%S")
            releaseProList.append(item.trans_to_dict())
        return result