from flask.ext import restful
from flask_restful import reqparse
from server.models import UpdateList,  ProOrder, Turnover, User, ReleasePro
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
        # file = open(upLoad_file + args['file'].filename,  'wb')
        # args['file'].save(upLoad_file + args['file'].filename)
        # updateList = UpdateList(args['title'], args['desc'], args['progress'])

    def saveFile(self, fileStorage, model, folder, filename):
        dir = upLoad_file + folder + str(model.id) + '-' + filename
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


class Hangdle(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('updateId', type=int, required=True)
        parser.add_argument('agress', type=int, required=True)
        parser.add_argument('reason', type=str, required=False)
        args = parser.parse_args()
        updateList = UpdateList.query.filter_by(id=args['updateId'], status='pending').first()
        proOrder = updateList.proOrder
        if args['agress'] == 1:
            updateList.status = 'accept'
            employer = User.query.filter_by(id=proOrder.employerId).first()
            employee = User.query.filter_by(id=proOrder.employeeId).first()
            releasePro = ReleasePro.query.filter_by(id=proOrder.releaseId).first()
            size = (updateList.progress - proOrder.progress) * releasePro.budget/100

            proOrder.employerDep -= size
            employer.deposit -= size
            employerTurnover = Turnover(employer.id, '支付薪酬(-押金)', -size, employer.balance, employer.deposit)

            proOrder.employeeDep -= size
            employee.deposit -= size
            employee.balance += 2 * size * 0.9
            employeeTurnover = Turnover(employee.id, '项目薪酬(+余额)', 2 * size * 0.9, employee.balance, employee.deposit)

            db.session.add(employerTurnover)
            db.session.add(employeeTurnover)
            db.session.commit()
            proOrder.progress = updateList.progress
            if proOrder.progress == 100:
                proOrder.status = '已完成'
        else:
            updateList.status = 'reject'
            updateList.rejectReason = args['reason']

        db.session.commit()



