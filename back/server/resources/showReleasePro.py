from flask.ext import restful
from flask_restful import reqparse
from flask.ext.restful import fields, marshal_with, marshal
from ..models import User, ReleasePro

resource_filed = {
    'id': fields.Integer,
    'employerId': fields.Integer,
    'projectName': fields.String,
    'firstType': fields.String,
    'secondType': fields.String,
    'describe': fields.String,
    'budget': fields.Integer,
    'cycle': fields.String,
    'company': fields.String,
    'status': fields.String,
    'releaseTime': fields.String,
    'applyAmount': fields.Integer,
    'browse': fields.Integer
}


class ShowReleasePro(restful.Resource):
    @marshal_with(resource_filed)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, help='id is required')
        args = parser.parse_args()
        releasePro = ReleasePro.query.filter_by(id=args['id']).first()
        return releasePro