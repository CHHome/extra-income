# todo 雇主查看申请项目的人，获取申请人更详细隐私信息
from flask.ext import restful
from flask_restful import reqparse
from ..models import  User, ApplyPro
from .. import db


class ApplyUserList(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('releaseProId', type=int, required=True, help='ReleaseProId is required')
        args = parser.parse_args()
        applyList = ApplyPro.query.filter_by(ReleaseProId=args['releaseProId'], status='申请中').all()
        resultList = list()
        for applyItem in applyList:
            user = User.query.filter_by(id=applyItem.applyUserId).first()
            user.registerTime = user.registerTime.strftime("%Y-%m-%d %H:%M:%S")
            resultList.append(user.trans_to_dict())
        return resultList