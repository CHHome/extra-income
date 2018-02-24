# todo 项目更新进度
from flask.ext import restful
from flask_restful import reqparse
from ..models import ProOrder, User
from .. import db
import datetime


class UpdateProgress(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('orderId', type=int, required=True, help='orderId is required')
        parser.add_argument('value', type=int, required=True, help='value is required')
        parser.add_argument('type', type=str, required=False)
        parser.add_argument('score', type=int, required=False)
        parser.add_argument('employerEvaluate', type=str, required=False)
        args = parser.parse_args()
        order = ProOrder.query.filter_by(id=args['orderId'], status='进行中').first()
        order.progress = args['value']
        db.session.commit()
        if args.type is None:
            return 10003
        else:
            order.status = '交付中'
            order.employerScore = args['score']
            order.employerEvaluate = args['employerEvaluate']
            order.completionTime = datetime.datetime.now()
            db.session.commit()
            return 10004

