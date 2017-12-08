
# 路由分发

from . import app,api
from .resources.hellotest import Hello
from .resources.user import Add



api.add_resource(Hello,'/')
api.add_resource(Add, '/user')
