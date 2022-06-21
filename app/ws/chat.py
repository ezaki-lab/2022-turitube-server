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


    def on_text_update_request(self, data):
        self.text = data["text"]
        room = data["room_id"]
        print("a")

        # 全員向けに送信すると入力の途中でテキストエリアが変更されて日本語入力がうまくできない
        emit("text_update",
            {
                "text": self.text
            },
            broadcast=True,
            include_self=False,
            room=room
        )