# todo 项目申请，将新的申请加入数据库applypro中，已经申请过的返回重复码

from flask.ext import restful
from flask_restful import reqparse
from ..models import ApplyPro, User, ReleasePro
from .. import db


class AddApply(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('ReleaseProId', type=int, required=True, help='ReleaseProId is required')
        parser.add_argument('applyUserId', type=int, required=True, help='applyUserId is required')
        args = parser.parse_args()
        user = User.query.filter_by(id=args['applyUserId']).first()
        releasePro = ReleasePro.query.filter_by(id=args['ReleaseProId']).first()
        if user.balance < releasePro.budget:
            return 100002
        applyItem = ApplyPro.query.filter_by(ReleaseProId=args['ReleaseProId'], applyUserId=args['applyUserId']).first()
        if applyItem is None:
            applyPro = ApplyPro(args['ReleaseProId'], args['applyUserId'])
            db.session.add(applyPro)
            db.session.commit()
            return 100001
        else:
            return 110001
