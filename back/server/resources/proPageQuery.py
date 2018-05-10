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
        parser.add_argument('keyWord', type=str, required=False)
        args = parser.parse_args()
        print(args['index'], args['type'], args['keyWord'])
        resultList = list()
        if args['type'] == '全部':
            if args['keyWord'] is None:
                queryResult = ReleasePro.query.filter(ReleasePro.status == '招募中') \
                    .order_by(db.desc(ReleasePro.budget)).limit(args['index'] * 2)
            else:
                queryResult = ReleasePro.query.filter(ReleasePro.status == '招募中') \
                    .filter(ReleasePro.projectName.like('%' + args['keyWord'] + '%')) \
                    .order_by(db.desc(ReleasePro.budget)).limit(args['index'] * 2)

        else:
            if args['keyWord'] is None:
                queryResult = ReleasePro.query\
                    .filter(ReleasePro.firstType == args['type']) \
                    .filter(ReleasePro.status == '招募中') \
                    .order_by(db.desc(ReleasePro.budget)).limit(args['index'] * 2)
            else:
                queryResult = ReleasePro.query \
                    .filter(ReleasePro.firstType == args['type']) \
                    .filter(ReleasePro.status == '招募中') \
                    .filter(ReleasePro.projectName.like('%' + args['keyWord'] + '%')) \
                    .order_by(db.desc(ReleasePro.budget)).limit(args['index'] * 2)
        for item in queryResult:
            item.releaseTime = item.releaseTime.strftime("%Y-%m-%d %H:%M:%S")
            resultList.append(item.trans_to_dict())
        return resultList



