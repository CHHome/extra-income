
# todo 验证登录状态是否有效

from flask.ext import restful
from flask.ext.restful import reqparse
import time
import base64
import hmac


class TokenCheck(restful.Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('token', type=str, required=True, help='username is required', location='form')
        parser.add_argument('tokenKey', type=str,required=True,help='password is required', location='form')
        args = parser.parse_args()
        return self.certify_token(args['tokenKey'], args['token'])

    def certify_token(self, key, token):
        token_str = base64.urlsafe_b64decode(token).decode('utf-8')
        token_list = token_str.split(':')
        if len(token_list) != 2:
            return False
        ts_str = token_list[0]
        if float(ts_str) < time.time():
            return False
        known_sha1_tsstr = token_list[1]
        sha1 = hmac.new(key.encode("utf-8"), ts_str.encode('utf-8'), 'sha1')
        calc_sha1_tsstr = sha1.hexdigest()
        if calc_sha1_tsstr != known_sha1_tsstr:
            return False
        return True