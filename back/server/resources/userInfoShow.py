from flask.ext import restful
from flask_restful import reqparse
from flask.ext.restful import fields, marshal_with, marshal
from ..models import Users, OldProject
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
    'head_img': fields.String,
    'old_project_list': fields.List
}


class UserInfoShow(restful.Resource):
    # @marshal_with(resource_filed)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('token', type=str, required=True, help='token is required')
        args = parser.parse_args()
        tokenArr = args['token'].split('-')
        user = Users.query.filter_by(id=tokenArr[0]).first()
        responseData = user.to_dict()
        proList = list()
        for item in user.old_project.all():
            proList.append(item.to_dict())
        responseData['projectList'] = proList
        return responseData
