from flask.ext import restful
from flask_restful import reqparse
from flask.ext.restful import fields, marshal_with
from ..models import Users
import json

resource_filed = {
    'id': fields.Integer,
    'phone': fields.String,
    'username': fields.String,
    'register_time': fields.String,
    'email': fields.String,
    'gender': fields.String,
    'age': fields.Integer,
    'good_at': fields.String,
    'on_time': fields.Integer,
    'credit': fields.Integer,
    'quality': fields.Integer,
    'price': fields.Integer,
    'has_finish': fields.Integer,
    'head_img': fields.String
    # 'list': fields.List
}


class UserInfoShow(restful.Resource):
    @marshal_with(resource_filed)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('token', type=str, required=True, help='token is required')
        args = parser.parse_args()
        tokenArr = args['token'].split('-')
        user = Users.query.filter_by(id=tokenArr[0]).first()
        return user