from flask.ext import restful
from flask import render_template



class Hello(restful.Resource):
    def get(self):
        return 'dffdff'
