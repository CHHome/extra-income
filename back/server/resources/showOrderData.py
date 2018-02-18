# todo ,订单页面中订单信息获取
from flask.ext import restful
from flask_restful import reqparse
from flask.ext.restful import fields, marshal_with, marshal
from ..models import ProOrder, ReleasePro


class ShowOrderData(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('orderId', type=int, required=True, help='orderId is required')
        args = parser.parse_args()
        proOrder = ProOrder.query.filter_by(releaseId=args['orderId']).first()
        if proOrder is not None:
            proOrder.beginTime = proOrder.beginTime.strftime("%Y-%m-%d %H:%M:%S")
            proOrder.deadlineTime = proOrder.deadlineTime.strftime("%Y-%m-%d %H:%M:%S")
            return proOrder.trans_to_dict()