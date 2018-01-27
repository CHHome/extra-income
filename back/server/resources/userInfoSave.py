from flask.ext import restful
from flask_restful import reqparse
from ..models import Users
from .. import db
import os, base64


upLoad_file = '/usr/code/extra-income/back/server/static/imgs/'

# def updateDate():



class UserInfoSave(restful.Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=False)
        parser.add_argument('headPic', type=str, required=False)
        parser.add_argument('age', type=int, required=False)
        parser.add_argument('good_at', type=str, required=False)
        parser.add_argument('price', type=int, required=False)
        parser.add_argument('phone', type=str, required=False)
        parser.add_argument('email', type=str, required=False)
        parser.add_argument('token', type=str, required=True, help='token is required')
        args = parser.parse_args()
        tokenArr = args['token'].split('-')
        user = Users.query.filter_by(id=tokenArr[0]).first()
        if(args['headPic']):
            self.saveFile(args['headPic'], user)
        user.username = args.username
        user.age = args.age
        user.good_at = args.good_at
        user.price = args.price
        user.phone = args.phone
        user.email = args.email
        db.session.commit()
        return user.username

    def saveFile(self, baseStr, user):
        print(baseStr)
        imgData = base64.b64decode(baseStr)
        file = open(upLoad_file+str(user.id) + '.jpg', 'wb')
        file.write(imgData)
        file.close()
        user.head_img = str(user.id) + '.jpg'