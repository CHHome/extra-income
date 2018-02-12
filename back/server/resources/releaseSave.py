from flask.ext import restful
from flask_restful import reqparse
from flask.ext.restful import fields, marshal_with, marshal
from ..models import ReleasePro
from .. import db


class ReleaseSave(restful.Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('userId', type=int, required=True)
        parser.add_argument('id', type=int, required=False)
        parser.add_argument('projectName', type=str, required=True)
        parser.add_argument('firstType', type=str, required=True)
        parser.add_argument('secondType', type=str, required=True)
        parser.add_argument('describe', type=str, required=True)
        parser.add_argument('budget', type=int, required=True)
        parser.add_argument('company', type=str, required=False)
        parser.add_argument('cycle', type=str, required=True)
        args = parser.parse_args()
        if not args['id']:
            newProject = ReleasePro(args['userId'], args['projectName'], args['firstType'], args['secondType'],
                                    args['describe'], args['budget'], args['cycle'], args['company'])
            db.session.add(newProject)
            db.session.commit()
            return newProject.id
        else:
            newProject = ReleasePro.query.filter_by(id=args['id']).first()
            newProject.projectName = args['projectName']
            newProject.firstType = args['firstType']
            newProject.secondType =  args['secondType']
            newProject.describe = args['describe']
            newProject.budget = args['budget']
            newProject.cycle = args['cycle']
            newProject.company = args['company']
            db.session.commit()
            return newProject.id


