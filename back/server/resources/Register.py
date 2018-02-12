# todo 注册

from flask.ext import restful
from flask_restful import reqparse
from .. import db
from ..models import User
import random


class Register(restful.Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('phone', type=str, required=True, help='phone is required', location='form')
        parser.add_argument('userName', type=str, required=True, help='user Name is required', location='form')
        parser.add_argument('password', type=str, required=True, help='password is required', location='form')
        args = parser.parse_args()
        user = User(args['phone'], args['userName'], args['password'])
        user.onTime = random.randint(60, 100)
        user.credit = random.randint(60, 100)
        user.quality = random.randint(60, 100)
        user.totalScore = user.onTime + user.credit + user.quality
        db.session.add(user)
        db.session.commit()
        return '1'

