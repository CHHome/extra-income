from flask.ext import restful
from flask_restful import reqparse
from flask.ext.restful import fields, marshal_with, marshal
from ..models import User, OldProject
import json

# resource_filed = {
#     'id': fields.Integer,
#     'phone': fields.String,
#     'username': fields.String,
#     'register_time': fields.String,
#     'email': fields.String,
#     'gender': fields.String,
#     'age': fields.Integer,
#     'good_at': fields.String,
#     'on_time': fields.Integer,
#     'credit': fields.Integer,
#     'quality': fields.Integer,
#     'price': fields.Integer,
#     'has_finish': fields.Integer,
#     'head_img': fields.String,
#     'old_project_list': fields.List
# }


class UserInfoShow(restful.Resource):
    # @marshal_with(resource_filed)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, help='id is required')
        parser.add_argument('type', type=str, required=False)
        args = parser.parse_args()
        id = args['id']
        user = User.query.filter_by(id=id).first()
        if args['type'] is None:
            responseData = user.to_dict()
        else:
            responseData = user.to_show()
        proList = list()
        for item in user.oldProject.all():
            proList.append(item.to_dict())
        responseData['projectList'] = proList
        return responseData
