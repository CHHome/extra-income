# todo 增加浏览次数/申请数
from flask.ext import restful
from flask_restful import reqparse
from ..models import  ReleasePro
from .. import db


class Increase(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('releaseId', type=int, required=True, help='releaseId is required')
        parser.add_argument('type', type=str, required=False)
        args = parser.parse_args()
        releasePro = ReleasePro.query.filter_by(id=args['releaseId'], status='招募中').first()
        if args['type'] == 'browse':
            releasePro.browse = releasePro.browse + 1
        else:
            releasePro.applyAmount = releasePro.applyAmount + 1
        db.session.commit()
        return 10007