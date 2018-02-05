
# todo 验证登录状态是否有效

from flask.ext import restful
from flask_restful import reqparse
from ..models import User
import hashlib
import time
import base64
import hmac

secretKey = 'JD98Dskw=23njQndW9D'
maxAge = 10


class TokenCheck(restful.Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('token', type=str, required=True, help='token is required', location='form')
        args = parser.parse_args()
        tokenArr = args['token'].split('-')
        user = User.query.filter_by(id=tokenArr[0]).first()
        print(round(time.time(), 5), '-', round(float(tokenArr[1]), 5))
        if time.time() < float(tokenArr[1]):
            s = '%s-%s-%s-%s' % (user.id, user.password, tokenArr[1], secretKey)
            if hashlib.sha1(s.encode('utf-8')).hexdigest() == tokenArr[2]:
                return 1
        else:
            return 0

