
# 路由分发

from . import app,api
from .resources.hellotest import Hello
from .resources.user import Add
from .resources.login import Login
from .resources.tokenCheck import TokenCheck
from .resources.Register import Register


api.add_resource(Hello, '/')
api.add_resource(Add, '/user')
api.add_resource(Login, '/login')
api.add_resource(Register, '/register')
api.add_resource(TokenCheck, '/tokenCheck')


