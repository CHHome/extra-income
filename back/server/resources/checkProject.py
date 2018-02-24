# todo 雇主验收项目
from flask.ext import restful
from flask_restful import reqparse
from ..models import ProOrder, ReleasePro, User
from .. import db


class CheckProject(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('orderId', type=int, required=True, help='orderId is required')
        parser.add_argument('type', type=str, required=True, help='type is required')
        parser.add_argument('credit', type=int, required=False)
        parser.add_argument('quality', type=int, required=False)
        parser.add_argument('onTime', type=int, required=False)
        parser.add_argument('evaluate', type=str, required=False)
        args = parser.parse_args()
        order = ProOrder.query.filter_by(id=args['orderId'], status='交付中').first()
        if args['type'] == 'yes':
            order.status = '已完成'
            employee = User.query.filter_by(id=order.employeeId).first()
            employer = User.query.filter_by(id=order.employerId).first()
            order.credit = args['credit']
            order.quality = args['quality']
            order.onTime = args['onTime']
            order.evaluate = args['evaluate']
            employee.credit = (order.credit + employee.credit)/2
            employee.quality = (order.quality + employee.quality)/2
            employee.onTime = (order.onTime + employee.onTime)/2
            employee.hasFinish += 1
            employee.totalScore = employee.credit + employee.quality + employee.onTime
            employer.employerScore = (employer.employerScore + order.employerScore)/2
            releasrPro = ReleasePro.query.filter_by(id=order.releaseId, status='进行中').first()
            releasrPro.status = '已完成'
            db.session.commit()
            return 10006
        else:
            order.status = '进行中'
            order.progress = 0
            order.completionTime = None
            order.employerEvaluate = None
            order.employerScore = 0
            # todo employerEvaluate
            db.session.commit()
            return 10005
            # order.