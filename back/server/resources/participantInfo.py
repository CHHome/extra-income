# todo 项目订单信息中显示参与者信息
from flask.ext import restful
from flask_restful import reqparse
from flask.ext.restful import fields, marshal_with, marshal
from ..models import User, ReleasePro
from .. import db


class ParticipantInfo(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('employerId', type=int, required=True, help='id is required')
        parser.add_argument('employeeId', type=int, required=True, help='id is required')
        args = parser.parse_args()
        employer = User.query.filter_by(id=args['employerId']).first()
        employee = User.query.filter_by(id=args['employeeId']).first()
        employerDict = self.change(employer)
        employeeDict = self.change(employee)
        result = dict()
        result['employee'] = employeeDict
        result['employer'] = employerDict
        return result

    def change(self, obj):
        myDict = dict()
        myDict['userId'] = obj.id
        myDict['headImg'] = obj.headImg
        myDict['userName'] = obj.userName
        myDict['email'] = obj.email
        myDict['phone'] = obj.phone
        myDict['profession'] = obj.profession
        return myDict