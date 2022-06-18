from flask_restful import Resource, Api
from .user import User
from .test import Test

def API(app):
    api = Api(app)
    api.add_resource(User, '/user')
    api.add_resource(Test, "/test")
    return api
