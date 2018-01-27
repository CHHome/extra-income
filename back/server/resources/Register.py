# todo 注册

from flask.ext import restful
from flask_restful import reqparse
from .. import db
from ..models import Users


class Register(restful.Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('phone', type=str, required=True, help='phone is required', location='form')
        parser.add_argument('username', type=str, required=True, help='username is required', location='form')
        parser.add_argument('password', type=str, required=True, help='password is required', location='form')
        args = parser.parse_args()
        user = Users(args['phone'], args['username'], args['password'])
        user.on_time = 33
        user.credit = 55
        user.quality = 44
        db.session.add(user)
        db.session.commit()
        return '1'

