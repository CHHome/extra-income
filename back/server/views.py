
# 路由分发


from . import api
from .resources.Recommend import Recommend
from .resources.Register import Register
from .resources.addApply import AddApply
from .resources.applyListShow import ApplyListShow
from .resources.applyUserList import ApplyUserList
from .resources.checkProject import CheckProject
from .resources.generatingOrder import GeneratingOrder
from .resources.haveInHandListShow import HaveInHandListShow
from .resources.hellotest import Hello
from .resources.increase import Increase
from .resources.login import Login
from .resources.myProjectData import MyProjectData
from .resources.participantInfo import ParticipantInfo
from .resources.proPageQuery import ProPageQuery
from .resources.releaseSave import ReleaseSave
from .resources.showBase import ShowBase
from .resources.showOrderData import ShowOrderData
from .resources.showReleasePro import ShowReleasePro
from .resources.tokenCheck import TokenCheck
from .resources.user import Add
from .resources.userInfoSave import UserInfoSave
from .resources.userInfoShow import UserInfoShow
from .resources.update import Update, ShowList, Hangdle, CreateAppeal
from .resources.account import ShowAccountInfo, Recharge
from .resources.updateProgress import UpdateProgress
from .resources.admin import AdminLogin, ShowUsers, HandleUser, ShowAppeals, Submit, changeAdv, HandlePro, ShowPro

api.add_resource(Hello, '/')
api.add_resource(Add, '/user')
api.add_resource(Login, '/login')
api.add_resource(Register, '/register')
api.add_resource(TokenCheck, '/tokenCheck')
api.add_resource(UserInfoSave, '/userInfoSave')
api.add_resource(UserInfoShow, '/userInfoShow')
api.add_resource(ReleaseSave, '/releaseSave')
api.add_resource(ShowReleasePro, '/showReleasePro')
api.add_resource(Recommend, '/recommend')
api.add_resource(ShowBase, '/showBase')
api.add_resource(MyProjectData, '/myProjectData')
api.add_resource(ProPageQuery, '/proPageQuery')
api.add_resource(AddApply, '/addApply')
api.add_resource(ApplyListShow, '/applyListShow')
api.add_resource(ApplyUserList, '/applyUserList')
api.add_resource(GeneratingOrder, '/generatingOrder')
api.add_resource(HaveInHandListShow, '/haveInHandListShow')
api.add_resource(ShowOrderData, '/showOrderData')
api.add_resource(ParticipantInfo, '/participantInfo')
api.add_resource(Update, '/updateProgress')
api.add_resource(ShowList, '/showUpdateList')
api.add_resource(Hangdle, '/updateHandle')
api.add_resource(CheckProject, '/checkProject')
api.add_resource(Increase, '/increase')
api.add_resource(ShowAccountInfo, '/showAccountInfo')
api.add_resource(Recharge, '/recharge')
api.add_resource(UpdateProgress, '/employeeEvaluate')
api.add_resource(CreateAppeal, '/sendAppeal')
api.add_resource(AdminLogin, '/adminLogin')
api.add_resource(ShowUsers, '/showUsers')
api.add_resource(HandleUser, '/handleUser')
api.add_resource(ShowAppeals, '/showAppeals')
api.add_resource(Submit, '/handleAppeal')
api.add_resource(changeAdv, '/changeAdv')
api.add_resource(HandlePro, '/handlePro')
api.add_resource(ShowPro, '/showPro')













