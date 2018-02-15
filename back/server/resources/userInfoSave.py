from flask.ext import restful
from flask_restful import reqparse
from ..models import User, OldProject
from .. import db
import os, base64
import json
import re


# upLoad_file = '/usr/code/extra-income/back/server/static/imgs/'
upLoad_file = '/home/ubuntu/code/extra-income/back/server/static/imgs/'


# def updateDate():

myList = [{'name': '322', 'pass': '9888'}, {'name': '989898', 'pass': '9888'}]


class UserInfoSave(restful.Resource):
    def post(self):
        print(myList)
        parser = reqparse.RequestParser()
        parser.add_argument('userName', type=str, required=False)
        parser.add_argument('headPic', type=str, required=False)
        parser.add_argument('age', type=int, required=False)
        parser.add_argument('goodAt', type=str, required=False)
        parser.add_argument('price', type=int, required=False)
        parser.add_argument('phone', type=str, required=False)
        parser.add_argument('profession', type=str, required=False)
        parser.add_argument('synopsis', type=str, required=False)
        parser.add_argument('email', type=str, required=False)
        parser.add_argument('token', type=str, required=True, help='token is required')
        parser.add_argument('projectList', type=str, required=False, action='append')
        args = parser.parse_args()
        tokenArr = args['token'].split('-')
        user = User.query.filter_by(id=tokenArr[0]).first()
        self.saveOldPro(args['projectList'], user.id)
        if args['headPic']:
            self.saveFile(args['headPic'], '', user)
        user.userName = args.userName
        user.age = args.age
        user.goodAt = args.goodAt
        user.price = args.price
        user.phone = args.phone
        user.email = args.email
        user.profession = args.profession
        user.synopsis = args.synopsis
        db.session.commit()
        return user.userName

    def saveOldPro(self, projectList, user_id):
        if projectList is None or len(projectList) == 0:
            return
        for i in projectList:
            proDict = json.loads(re.sub('\'', '\"', i))
            if 'id' in proDict:
                oldproject = OldProject.query.filter_by(id=proDict['id']).first()
                oldproject.proName = proDict['proName']
                oldproject.player = proDict['player']
                oldproject.industry = proDict['industry']
                oldproject.linkTo = proDict['linkTo']
                oldproject.describe = proDict['describe']

            else:
                oldproject = OldProject(user_id, proDict['proName'], proDict['player'], proDict['industry'])
                db.session.add(oldproject)
                db.session.commit()
                print(oldproject.id)
                oldproject.linkTo = proDict['linkTo']
                oldproject.describe = proDict['describe']
            if 'imgData' in proDict and proDict['imgData'] != '':
                self.saveFile(re.split(r';base64,', proDict['imgData'])[1], 'project/', oldproject)
            db.session.commit()

    def saveFile(self, baseStr, dir, obj):
        imgData = base64.b64decode(baseStr)
        file = open(upLoad_file+dir+str(obj.id) + '.jpg', 'wb')
        file.write(imgData)
        file.close()
        obj. headImg = dir + str(obj.id) + '.jpg'
