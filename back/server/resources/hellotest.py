from flask.ext import restful



class Hello(restful.Resource):
    def get(self):
        return {'hello': 'world'}