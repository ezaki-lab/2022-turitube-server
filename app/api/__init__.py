from flask_restful import Resource, Api, reqparse
from .user import User
from .test import Test

import json

def API(app):
    api = Api(app)
    api.add_resource(User, '/user')
    api.add_resource(Test, "/test")
    return api
