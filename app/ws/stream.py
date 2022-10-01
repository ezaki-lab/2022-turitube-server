from xml.etree.ElementInclude import include
from flask import request
from flask_socketio import emit, join_room, leave_room, Namespace
from app.utils.db_conn import sql_connection
import json

class Stream(Namespace):
    def __init__(self, namespace):
        super().__init__(namespace)
        self.streams = {}
        self.users = {}

    def update_stream(self, room_id):
        emit("update_stream", self.streams[room_id],
        room=room_id,
        broadcast=True,
        include_self=True)
    
    def set_user(self, data):
        sid = request.sid
        self.users[sid] = {
            "user_name": data["user_name"],
            "user_type": data["user_type"],
            "room_id": data["room_id"]
        }

    def remove_user(self):
        sid = request.sid
        del self.users[sid]

    def pop_user(self):
        sid = request.sid
        data = self.users[sid]
        del self.users[sid]
        return data
    
    # 部屋入室時
    def on_join(self, data):
        room = data["room_id"]
        user_name = data["user_name"]
        user_type = data["user_type"] # streamer, listener
        self.set_user(data)
        sql_connection(f"""UPDATE `Room` SET {user_type}={user_type} + 1 WHERE `room_id`='{room}'""")

        # 部屋がなければ作成
        if not room in self.streams.keys():
            self.streams[room] = {
                "streamer": {
                    user_name:{
                    "is_host": True,
                    "camera": False,
                    "audio": False,
                    "face": 0
                }  
                }, 
                "listener": []
            }

        
        # 再読み込み対策
        if user_name in self.streams[room]["listener"]:
            self.streams[room]["listener"].remove(user_name)

        if room in self.streams.keys() and (not user_name in self.streams[room]["streamer"].keys()):
            if user_type=="streamer":
                self.streams[room]["streamer"][user_name] = {
                    "is_host": False,
                    "camera": False,
                    "audio": False,
                    "face": 0
                }  
                
            else:
                self.streams[room]["listener"].append(user_name)
        
        join_room(room)
        emit("join", {
            'user_name': user_name,
            'user_type': user_type
        })
        self.update_stream(room)
    
    # 部屋退室時
    def on_disconnect(self):
        print(request.sid + " disconnect")
        data = self.pop_user()
        user_name = data["user_name"]
        room = data["room_id"]
        user_type = data["user_type"]

        sql_connection(f"""UPDATE `Room` SET {user_type}={user_type} - 1 WHERE `room_id`='{room}'""")

        is_host = False
        if user_type=="streamer":
            is_host = self.streams[room]["streamer"][user_name]["is_host"]
            del self.streams[room]["streamer"][user_name]
        else:
            if user_name in self.streams[room]["listener"]:
                self.streams[room]["listener"].remove(user_name)
        
        # ホストが退出したとき部屋を削除するk
        if is_host:
            del self.streams[room]
            emit("delete_room", room=room)
            sql_connection(f"""UPDATE `Room` SET `is_open`=0 WHERE `room_id`='{room}'""")

        # ホスト以外の時は部屋を更新する
        else:
            emit("leave", {
                "room": self.streams[room],
                "user_type": user_type
            })
            self.update_stream(room)

    # チャット送信時
    def on_chat(self, data):
        room = data["room_id"]
        user_name = data["user_name"]
        text = data["text"]
        emit("chat", {
            "user_name": user_name,
            "text": text
        },
        room=room,
        broadcast=True,
        include_self=True)

    # 配信者の情報を更新する
    def on_update_user(self,data):
        room = data["room_id"]
        user_name = data["user_name"]
        user_type = data["user_type"]
        if user_type == "streamer":
            for key in self.streams[room]["streamer"]:
                self.streams[room]["streamer"][key]["camera"] = False
            self.streams[room]["streamer"][user_name]["camera"] = data["user"]["camera"]
            self.streams[room]["streamer"][user_name]["audio"] = data["user"]["audio"]
            self.streams[room]["streamer"][user_name]["face"] = data["user"]["face"]
            self.update_stream(room)

    def on_video(self, data):
        room = data["room_id"]
        peer_id = data["peer_id"]
        emit("video", {
            "peer_id": peer_id
        },
        room=room,
        broadcast=True,
        include_self=True)
        
