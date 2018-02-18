# todo 生成项目订单
from flask.ext import restful
from flask_restful import reqparse
from flask.ext.restful import fields, marshal_with, marshal
from ..models import ProOrder, ApplyPro, ReleasePro
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
        self.changeStatus(args['releaseId'], args['applyId'])
        proOrder = ProOrder(args['applyId'],  args['employerId'], args['employeeId'],  args['releaseId'], datetime.datetime.now() + datetime.timedelta(days=60))
        db.session.add(proOrder)
        db.session.commit()

    def changeStatus(self, release_id, apply_id):
        releasePro = ReleasePro.query.filter_by(id=release_id, status='招募中').first()
        releasePro.status = '进行中'
        applyList = releasePro.apply.all()
        print(applyList)
        for item in applyList:
            if item.id != apply_id:
                item.status = '已回绝'
            else:
                item.status = '已同意'