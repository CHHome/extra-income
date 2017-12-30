from flask.ext import restful
from flask_restful import reqparse
from ..models import UserInfo


class UserInfoSave(restful.Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=False, location='form')
        parser.add_argument('age', type=int, required=False, location='form')
        parser.add_argument('goodAt', type=int, required=False, location='form')
        parser.add_argument('price', type=int, required=False, location='form')
        args = parser.parse_args()
        return 'access'