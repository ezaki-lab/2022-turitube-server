from flask_restful import Resource, Api, reqparse
from .user import User
from .test import Test
from .signin import SignIn
from .login import Login
from .stream import Stream
from .stream_photo import StreamPhoto
from .achive import Achive
from .quest import Quest
from .speacies_detection import Speacies

import json

def API(app):
    api = Api(app)
    api.add_resource(User, '/user')
    api.add_resource(SignIn, '/signin')
    api.add_resource(Login, '/login')
    api.add_resource(Stream, '/stream')
    api.add_resource(StreamPhoto, "/stream_photo")
    api.add_resource(Achive, "/achive")
    api.add_resource(Quest, "/quest")
    api.add_resource(Speacies, "/speacies")
    api.add_resource(Test, "/test")
    return api
