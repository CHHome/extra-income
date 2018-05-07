from flask.ext import restful
from flask_restful import reqparse
from ..models import Admin, User, Appeal, ProOrder, ReleasePro ,UpdateList, Turnover
from .. import db


class AdminLogin(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='name is required')
        parser.add_argument('password', type=str, required=True, help='password is required')
        args = parser.parse_args()
        admin = Admin.query.filter_by(adminName=args['name']).first()
        if admin.password == args['password']:
            return 100001
        else:
            return 100002


class ShowUsers(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, required=True, help='page is required')
        parser.add_argument('sort', type=str, required=True, help='sore is required')
        args = parser.parse_args()
        totalPage = len(User.query.order_by(db.asc(User.id)).all())
        if args.sort == 'id':
            userList = User.query.order_by(db.asc(User.id)).limit(3).offset((args['page']-1)*3).all()
        if args.sort == 'totalScore':
            userList = User.query.order_by(db.asc(User.totalScore)).limit(3).offset((args['page']-1)*3).all()
        if args.sort == 'employerScore':
            userList = User.query.order_by(db.asc(User.employerScore)).limit(3).offset((args['page']-1)*3).all()
        resultList = list()
        for item in userList:
            item = item.trans_to_dict()
            item['registerTime'] = item['registerTime'].strftime("%Y-%m-%d %H:%M:%S")
            resultList.append(item)
        result = dict()
        result['totalPage'] = totalPage
        result['resultList'] = resultList
        return result


class HandleUser(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, help='id is required')
        parser.add_argument('type', type=str, required=True, help='type is required')
        args = parser.parse_args()
        user = User.query.filter_by(id=args['id']).first()
        if args['type'] == 'lock':
            user.status = '冻结'
        else:
            user.status = '正常'
        db.session.commit()
        return 100001


class ShowAppeals(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, required=True, help='page is required')
        parser.add_argument('type', type=str, required=True, help='type is required')
        args = parser.parse_args()
        appealList = Appeal.query.filter_by(status=args['type']).order_by(db.asc(Appeal.id)).limit(3).offset((args['page']-1)*3).all()
        totalPage = len(Appeal.query.filter_by(status=args['type']).all())
        resultList = list()
        for item in appealList:
            item = item.trans_to_dict()
            complainant = User.query.filter_by(id=item['complainantId']).first()
            complainant = complainant.trans_to_dict()
            complainant['registerTime'] = complainant['registerTime'].strftime("%Y-%m-%d %H:%M:%S")
            defendanter = User.query.filter_by(id=item['defendanterId']).first()
            defendanter = defendanter.trans_to_dict()
            defendanter['registerTime'] = defendanter['registerTime'].strftime("%Y-%m-%d %H:%M:%S")
            item['beginTime'] = item['beginTime'].strftime("%Y-%m-%d %H:%M:%S")
            proOrder = ProOrder.query.filter_by(id=item['orderId']).first()
            if item['complainantId'] == proOrder.employerId:
                item['complainantRole'] = '雇主'
                item['defendanterRole'] = '专家'
            else:
                item['defendanterRole'] = '雇主'
                item['complainantRole'] = '专家'
            proOrder.beginTime = proOrder.beginTime.strftime("%Y-%m-%d %H:%M:%S")
            proOrder.deadlineTime = proOrder.deadlineTime.strftime("%Y-%m-%d %H:%M:%S")
            if proOrder.completionTime is not None:
                proOrder.completionTime = proOrder.completionTime.strftime("%Y-%m-%d %H:%M:%S")
            releasePro = ReleasePro.query.filter_by(id=proOrder.releaseId).first()
            releasePro.releaseTime = releasePro.releaseTime.strftime("%Y-%m-%d %H:%M:%S")
            releasePro = releasePro.trans_to_dict()
            updateLists = proOrder.updateList.all()
            resultUpdateList = list()
            for value in updateLists:
                value.updateTime = value.updateTime.strftime("%Y-%m-%d %H:%M:%S")
                value = value.trans_to_dict()
                resultUpdateList.append(value)
            proOrder = proOrder.trans_to_dict()
            item['complainant'] = complainant
            item['defendanter'] = defendanter
            item['proOrder'] = proOrder
            item['releasePro'] = releasePro
            item['updateLists'] = resultUpdateList
            if item['endTime'] is not None:
                item['endTime'] = item['endTime'].strftime("%Y-%m-%d %H:%M:%S")
            resultList.append(item)
        result = dict()
        result['resultList'] = resultList
        result['totalPage'] = totalPage
        return result


class Submit(restful.Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, help='id is required')
        parser.add_argument('winner', type=int, required=True, help='winner is required')
        parser.add_argument('damages', type=int, required=True, help='type is required')
        args = parser.parse_args()
        appeal = Appeal.query.filter_by(id=args['id']).first()
        appeal.damages = args.damages
        appeal.winner = args.winner
        proOrder = ProOrder.query.filter_by(id=appeal.orderId).first()
        releasePro = ReleasePro.query.filter_by(id=proOrder.releaseId).first()
        if proOrder.employerId != args.winner:
            proOrder.employerDep -= args.damages
            proOrder.employeeDep += args.damages
            self.money(proOrder.employeeId, proOrder.employerId, proOrder.employeeDep, proOrder.employerDep, args.damages)
        else:
            proOrder.employeeDep -= args.damages
            proOrder.employerDep += args.damages
            self.money(proOrder.employerId, proOrder.employeeId, proOrder.employerDep, proOrder.employeeDep, args.damages)
        proOrder.employeeDep = 0
        proOrder.employerDep = 0
        proOrder.status = '申诉完成'
        releasePro.status = '已完成'
        appeal.status = '已处理'
        db.session.commit()

    def money(self, winnerID, loserID, winnerDep, loserDep, damages):
        winner = User.query.filter_by(id=winnerID).first()
        loser = User.query.filter_by(id=loserID).first()
        winner.balance += winnerDep
        loser.balance += loserDep
        winner.deposit -= winnerDep
        loser.deposit -= loserDep
        turnover1 = Turnover(winnerID, '申诉(+余额)', damages, winner.balance, winner.deposit)
        turnover2 = Turnover(loserID, '申诉(+余额)', -damages, loser.balance, loser.deposit)
        db.session.add(turnover1)
        db.session.add(turnover2)
        db.session.commit()




