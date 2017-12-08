from flask.ext import restful
from flask.ext.restful import fields, marshal_with
from flask.ext.restful import reqparse


resource_filed = {
    'username':     fields.String,
    'age':      fields.Integer
}
class AddUser(object):
    def __init__(self, username, age, sex):
        self.username = username
        self.age = age
        self.sex = sex
        self.status = 'active'

class Add(restful.Resource):
    @marshal_with(resource_filed)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, help='Rate cannot be converted')
        parser.add_argument('age', type=int)
        parser.add_argument('sex', type=str)
        args = parser.parse_args()
        user = AddUser(args['username'], args['age'], args['sex'])
        return user
