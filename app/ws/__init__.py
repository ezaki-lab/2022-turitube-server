"""
Socket.ioの名前空間を統合
"""

from .. import socketio
from .test import Test
from .stream import Stream

socketio.on_namespace(Test('/test'))
socketio.on_namespace(Stream('/stream'))