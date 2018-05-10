# todo 验证登录信息,生成token

from flask.ext import restful
from flask_restful import reqparse
from ..models import User
import time
import hashlib

secretKey = 'JD98Dskw=23njQndW9D'
maxAge = 3600



class Login(restful.Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('userName', type=str, required=True, help='user name is required', location='form')
        parser.add_argument('password', type=str, required=True, help='password is required', location='form')
        args = parser.parse_args()
        expires = str(time.time() + maxAge)
        user = User.query.filter_by(userName=args['userName']).first()
        if user is not None and user.password == args['password']:
            s = '%s-%s-%s-%s' % (user.id, user.password, expires, secretKey)
            print(s)
            tokenArr = [str(user.id), expires, hashlib.sha1(s.encode('utf-8')).hexdigest()]
            return '-'.join(tokenArr)
        return 'fail'


