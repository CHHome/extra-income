# todo 验证登录信息,生成token

from flask.ext import restful
from flask_restful import reqparse
from ..models import Users
import time
import hashlib

secretKey = 'JD98Dskw=23njQndW9D'
maxAge = 3600



class Login(restful.Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help='username is required', location='form')
        parser.add_argument('password', type=str, required=True, help='password is required', location='form')
        args = parser.parse_args()
        expires = str(time.time() + maxAge)
        user = Users.query.filter_by(username=args['username']).first()
        if user.password == args['password']:
            s = '%s-%s-%s-%s' % (user.id, user.password, expires, secretKey)
            print(s)
            tokenArr = [str(user.id), expires, hashlib.sha1(s.encode('utf-8')).hexdigest()]
            return '-'.join(tokenArr)
        return 'fail'


