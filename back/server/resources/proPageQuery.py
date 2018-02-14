# todo 主页更多项目中的分页查询
from flask.ext import restful
from flask_restful import reqparse
from ..models import ReleasePro
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
            queryResult = ReleasePro.query.filter_by(status='招募中').order_by(db.desc(ReleasePro.budget)).limit(2).offset((args['index']-1)*2)

        else:
            queryResult = ReleasePro.query.filter_by(firstType=args['type'], status='招募中').order_by(db.desc(ReleasePro.budget)).limit(2).offset((args['index']-1)*2)
        for item in queryResult:
            resultList.append(item.trans_to_dict())
        return resultList



