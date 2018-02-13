from flask.ext import restful
from flask_restful import reqparse
from flask.ext.restful import fields, marshal_with, marshal
from ..models import User, ReleasePro
from .. import db


class MyProjectData(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, help='id is required')
        parser.add_argument('type', type=str, required=False)
        args = parser.parse_args()
        print(args['id'], args['type'])
        if args['type'] == 'releasing':
            return self.getReleasing(args['id'])

    def getReleasing(self, id):
        resultList = list()
        result = ReleasePro.query.filter_by(employerId=id, status='招募中').all()
        for item in result:
            resultList.append(item.trans_to_dict())
        return resultList
