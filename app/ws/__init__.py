"""
Socket.ioの名前空間を統合
"""

from .. import socketio
from .test import Test
from .chat import Chat

socketio.on_namespace(Test('/test'))
socketio.on_namespace(Chat('/chat'))