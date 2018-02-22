# todo 项目更新进度
from flask.ext import restful
from flask_restful import reqparse
from flask.ext.restful import fields, marshal_with, marshal
from ..models import ProOrder
from .. import db


class UpdateProgress(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('orderId', type=int, required=True, help='orderId is required')
        parser.add_argument('value', type=int, required=True, help='value is required')
        parser.add_argument('type', type=str, required=False, help='value is required')
        args = parser.parse_args()
        order = ProOrder.query.filter_by(id=args['orderId']).first()
        order.progress = args['value']
        db.session.commit()
        print(args.type)
        if args.type is None:
            return 10003
        else:
            order.status = '交付中'
            db.session.commit()
            return 10004

