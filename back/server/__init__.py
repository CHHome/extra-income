# 初始化app，restful api

from flask import Flask
from flask.ext import restful
from flask_sqlalchemy import SQLAlchemy
from flask_cors import *


app = Flask(__name__)
CORS(app, supports_credentials=True)   # todo 允许跨域
api = restful.Api(app)
app.config.from_object('config')
db = SQLAlchemy(app)



from . import views, models






