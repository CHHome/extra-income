from flask.ext import restful
from flask_restful import reqparse
from server.models import UpdateList,  ProOrder
from server import db
import os, base64
import json
import re
import werkzeug

upLoad_file = '/usr/code/extra-income/back/server/static/'


class Update(restful.Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True, location='form')
        parser.add_argument('desc', type=str, required=True, location='form')
        parser.add_argument('releaseId', type=int, required=True, location='form')
        parser.add_argument('progress', type=int, required=True, location='form')
        parser.add_argument('file', type=werkzeug.datastructures.FileStorage, required=True, location='files')
        args = parser.parse_args()
        print(args['title'], args['desc'], args['progress'], args['file'].filename, args['releaseId'])
        proOrder = ProOrder.query.filter_by(releaseId=args['releaseId']).first()
        print(proOrder)
        if proOrder is not None:
            updateList = UpdateList(args['title'], args['desc'], args['progress'], proOrder.id)
            db.session.add(updateList)
            db.session.commit()
            self.saveFile(args['file'], updateList, 'updateFile/', args['file'].filename)
        print(args['title'], args['desc'], args['progress'], args['file'].filename)
        # file = open(upLoad_file + args['file'].filename,  'wb')
        # args['file'].save(upLoad_file + args['file'].filename)
        # updateList = UpdateList(args['title'], args['desc'], args['progress'])

    def saveFile(self, fileStorage, model, folder, filename):
        print(model)
        dir = upLoad_file + folder + str(model.id) + '-' + filename
        print(dir)
        open(dir, 'wb')
        fileStorage.save(dir)
        model.fileDir = folder + str(model.id) + '-' + filename
        db.session.commit()


class ShowList(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('releaseId', type=int, required=True)
        args = parser.parse_args()
        proOrder = ProOrder.query.filter_by(releaseId=args['releaseId']).first()
        updateLists = proOrder.updateList.all()
        resultList = list()
        for item in updateLists:
            item.updateTime = item.updateTime.strftime("%Y-%m-%d %H:%M:%S")
            item = item.trans_to_dict()
            resultList.append(item)
        return resultList



