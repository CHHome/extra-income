# todo 项目更新进度
from flask.ext import restful
from flask_restful import reqparse
from ..models import User, Turnover
from .. import db
import datetime


class ShowAccountInfo(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('userId', type=int, required=True, help='userId is required')
        args = parser.parse_args()
        user = User.query.filter_by(id=args['userId']).first()
        turnovers = user.turnover.order_by(db.desc(Turnover.time)).all()
        result = dict()
        turnoverList = list()
        result['balance'] = user.balance
        result['deposit'] = user.deposit
        for item in turnovers:
            item.time = item.time.strftime("%Y-%m-%d %H:%M:%S")
            turnoverList.append(item.trans_to_dict())
        result['turnoverList'] = turnoverList
        return result


class Recharge(restful.Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('userId', type=int, required=True, help='userId is required')
        parser.add_argument('quota', type=int, required=True, help='quota is required')
        args = parser.parse_args()
        user = User.query.filter_by(id=args['userId']).first()
        user.balance += args['quota']
        db.session.commit()
        turnover = Turnover(user.id, '充值(+余额)', args['quota'], user.balance, user.deposit)
        db.session.add(turnover)
        db.session.commit()
        return 'success'
