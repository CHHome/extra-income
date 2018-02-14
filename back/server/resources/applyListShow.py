# todo 我的项目中查看我正在申请的项目
from flask.ext import restful
from flask_restful import reqparse
from ..models import  ReleasePro, ApplyPro
from .. import db


class ApplyListShow(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('applyUserId', type=int, required=True, help='id is required')
        args = parser.parse_args()
        applyList = ApplyPro.query.filter_by(applyUserId=args['applyUserId'], status='申请中').all()
        resultList = list()
        for item in applyList:
            resultList.append(item.releasePro.trans_to_dict())
        return resultList