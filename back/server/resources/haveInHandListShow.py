# todo 我的项目中进行时订单
from flask.ext import restful
from flask_restful import reqparse
from flask.ext.restful import fields, marshal_with, marshal
from ..models import ProOrder, ApplyPro, ReleasePro
from .. import db
import datetime


class HaveInHandListShow(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True) # todo  用户id
        parser.add_argument('type', type=str, required=True, help='type is required')
        args = parser.parse_args()
        proOrderList = ProOrder.query.filter_by(employerId=args['id'], status=args['type']).all()
        proOrderList.extend(ProOrder.query.filter_by(employeeId=args['id'], status=args['type']).all())
        proOrderList = sorted(proOrderList, key=lambda e: e.beginTime)
        releaseList = list()
        resultList = list()
        for item in proOrderList:
            releaseList.append(ReleasePro.query.filter_by(id=item.releaseId, status=args['type']).first())
        for item in releaseList:
            item.releaseTime = item.releaseTime.strftime("%Y-%m-%d %H:%M:%S")
            resultList.append(item.trans_to_dict())
        return resultList
