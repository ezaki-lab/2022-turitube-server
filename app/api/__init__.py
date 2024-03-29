from flask_restful import Resource, Api, reqparse
from .user import User
from .test import Test
from .signin import SignIn
from .login import Login
from .stream import Stream
from .stream_photo import StreamPhoto
from .achive import Achive
from .quest import Quest
from .items import Items
from .icon import Icon
from .books import Books
from .picture_book import PictureBook
from .room import Room
from .fish_detection import FishDetection
from .expression import Expression
from .diary import Diary
# user_name to user はprofileとかでいいと思います。
import json


def API(app):
    api = Api(app)
    api.add_resource(User, '/user')
    api.add_resource(SignIn, '/signin')
    api.add_resource(Login, '/login')
    api.add_resource(Items, "/items")
    api.add_resource(Achive, "/achive")
    api.add_resource(Quest, "/quest")
    api.add_resource(Icon, "/icon")
    api.add_resource(Books, "/books")
    api.add_resource(PictureBook, "/picture_book")
    api.add_resource(Diary, "/diary")
    api.add_resource(Room, "/room")
    api.add_resource(StreamPhoto, "/stream_photo")
    api.add_resource(FishDetection, "/fish_detection")
    api.add_resource(Expression, "/expression")
    api.add_resource(Stream, '/stream')
    
    api.add_resource(Test, "/test")
    return api
