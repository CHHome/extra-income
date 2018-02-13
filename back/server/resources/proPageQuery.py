from flask.ext import restful
from flask_restful import reqparse
from flask.ext.restful import fields, marshal_with, marshal
from ..models import User, ReleasePro
from .. import db


class ProPageQuery(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('index', type=int, required=True, help='id is required')
        parser.add_argument('type', type=str, required=True, help='type is required')
        args = parser.parse_args()
        print(args['index'], args['type'])
        resultList = list()
        if args['type'] == '全部':
            queryResult = ReleasePro.query.order_by(db.desc(ReleasePro.budget)).limit(2).offset((args['index']-1)*2)
            for item in queryResult:
                resultList.append(item.trans_to_dict())
            return resultList
