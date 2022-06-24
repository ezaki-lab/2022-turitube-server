"""
製作ソケット
"""

from flask import request
from flask_socketio import emit, join_room, leave_room, Namespace

class Chat(Namespace):
    def __init__(self, namespace):
        super().__init__(namespace)
        self.user_count = 0
        self.text = ""
        print("tes")

    def on_join(self, data):
        room = data["room_id"]
        print(room)
        join_room(room)
        emit("text_update",
        {
            "text": room
        },
        broadcast=True,
        include_self=True,
        room=room)

    def on_chat_update(self, data):
        text = data["text"]
        room = data["room_id"]
        screen_name = data["screen_name"]
        print("chat_update")

        emit("chat", 
            {
                "screen_name": screen_name,
                "text": text
            },
            broadcast=True,
            include_self=True,
            room=room
        )