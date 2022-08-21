from flask_restful import Resource, Api, reqparse
from .user import User
from .test import Test
from .signin import SignIn
from .login import Login
from .stream import Stream

import json

def API(app):
    api = Api(app)
    api.add_resource(User, '/user')
    api.add_resource(SignIn, '/signin')
    api.add_resource(Login, '/login')
    api.add_resource(Stream, '/stream')
    api.add_resource(Test, "/test")
    return api
