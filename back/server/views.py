
# 路由分发

from . import app,api
from .resources.hellotest import Hello
from .resources.user import Add
from .resources.login import Login
from .resources.userInfoSave import UserInfoSave
from .resources.userInfoShow import UserInfoShow
from .resources.tokenCheck import TokenCheck
from .resources.Register import Register
from .resources.releaseSave import ReleaseSave
from .resources.showReleasePro import ShowReleasePro



api.add_resource(Hello, '/')
api.add_resource(Add, '/user')
api.add_resource(Login, '/login')
api.add_resource(Register, '/register')
api.add_resource(TokenCheck, '/tokenCheck')
api.add_resource(UserInfoSave, '/userInfoSave')
api.add_resource(UserInfoShow, '/userInfoShow')
api.add_resource(ReleaseSave, '/releaseSave')
api.add_resource(ShowReleasePro, '/showReleasePro')



