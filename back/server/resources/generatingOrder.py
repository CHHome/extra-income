# todo 生成项目订单
from flask.ext import restful
from flask_restful import reqparse
from flask.ext.restful import fields, marshal_with, marshal
from ..models import ProOrder, User, ReleasePro, Turnover
from .. import db
import datetime


class GeneratingOrder(restful.Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('applyId', type=int, required=True)
        parser.add_argument('employerId', type=int, required=True)
        parser.add_argument('employeeId', type=int, required=True)
        parser.add_argument('releaseId', type=int, required=True)
        parser.add_argument('cycle', type=int, required=True)
        args = parser.parse_args()
        releasePro = ReleasePro.query.filter_by(id=args['releaseId'], status='招募中').first()
        self.changeStatus(args['applyId'], releasePro, args['employeeId'])
        proOrder = ProOrder(args['applyId'],  args['employerId'], args['employeeId'],  args['releaseId'], datetime.datetime.now() + datetime.timedelta(days=args['cycle']))
        proOrder.employerDep = releasePro.budget
        proOrder.employeeDep = releasePro.budget
        db.session.add(proOrder)
        db.session.commit()
        return 10008

    def changeStatus(self, apply_id, releasePro, employeeId):
        releasePro.status = '进行中'
        enployer = User.query.filter_by(id=releasePro.employerId).first()
        enployee = User.query.filter_by(id=employeeId).first()
        enployee.balance -= releasePro.budget
        enployee.deposit += releasePro.budget
        enployer.employeeNum += 1
        employeeTurnover = Turnover(employeeId, '缴纳押金(-余额)', -releasePro.budget, enployee.balance, enployee.deposit)
        db.session.add(employeeTurnover)
        db.session.commit()
        applyList = releasePro.apply.all()
        for item in applyList:
            if item.id != apply_id:
                item.status = '已回绝'
            else:
                item.status = '已同意'