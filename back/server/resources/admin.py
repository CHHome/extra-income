from flask.ext import restful
from flask_restful import reqparse
from ..models import Admin, User
from .. import db


class AdminLogin(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='name is required')
        parser.add_argument('password', type=str, required=True, help='password is required')
        args = parser.parse_args()
        admin = Admin.query.filter_by(adminName=args['name']).first()
        if admin.password == args['password']:
            return 100001
        else:
            return 100002


class ShowUsers(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, required=True, help='page is required')
        parser.add_argument('sort', type=str, required=True, help='sore is required')
        args = parser.parse_args()
        totalPage = len(User.query.order_by(db.asc(User.id)).all())
        if args.sort == 'id':
            userList = User.query.order_by(db.asc(User.id)).limit(3).offset((args['page']-1)*3).all()
        if args.sort == 'totalScore':
            userList = User.query.order_by(db.asc(User.totalScore)).limit(3).offset((args['page']-1)*3).all()
        if args.sort == 'employerScore':
            userList = User.query.order_by(db.asc(User.employerScore)).limit(3).offset((args['page']-1)*3).all()
        resultList = list()
        for item in userList:
            item = item.trans_to_dict()
            item['registerTime'] = item['registerTime'].strftime("%Y-%m-%d %H:%M:%S")
            resultList.append(item)
        result = dict()
        result['totalPage'] = totalPage
        result['resultList'] = resultList
        return result


class HandleUser(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, help='id is required')
        parser.add_argument('type', type=str, required=True, help='type is required')
        args = parser.parse_args()
        user = User.query.filter_by(id=args['id']).first()
        if args['type'] == 'lock':
            user.status = '冻结'
        else:
            user.status = '正常'
        db.session.commit()
        return 100001