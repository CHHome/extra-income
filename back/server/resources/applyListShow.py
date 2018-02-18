# todo 我的项目中查看我正在申请的项目
from flask.ext import restful
from flask_restful import reqparse
from ..models import  ReleasePro, ApplyPro
from .. import db


class ApplyListShow(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, help='id is required')  #applyId
        parser.add_argument('type', type=str, required=True, help='type is required')
        args = parser.parse_args()
        applyList = ApplyPro.query.filter_by(applyUserId=args['id'], status=args['type']).all()
        resultList = list()
        for item in applyList:
            project = item.releasePro
            project.releaseTime = project.releaseTime.strftime("%Y-%m-%d %H:%M:%S")
            resultList.append(project.trans_to_dict())
        return resultList