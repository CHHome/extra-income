# todo 验证登录信息,生成token

from flask.ext import restful
from flask.ext.restful import reqparse
import time
import base64
import hmac


class Login(restful.Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help='username is required', location='form')
        parser.add_argument('password', type=str,required=True,help='password is required', location='form')
        parser.add_argument('tokenKey', type=str, required=True, help='token_key', location='form')
        args = parser.parse_args()
        token = self.create_token(args['tokenKey'])
        return token


    def create_token(self, key, expire=3600):
        ts_str = str(time.time() + expire)
        ts_byte = ts_str.encode("utf-8")
        sha1_tshexstr = hmac.new(key.encode("utf-8"), ts_byte, 'sha1').hexdigest()
        token = ts_str + ':' + sha1_tshexstr
        b64_token = base64.urlsafe_b64encode(token.encode("utf-8"))
        return b64_token.decode("utf-8")

