from xml.etree.ElementInclude import include
from flask import request
from flask_socketio import emit, join_room, leave_room, Namespace
from app.utils.db_conn import sql_connection
import json

# sidで管理すると面倒なことになるので使わない
# user_nameで管理する

class Stream(Namespace):
    def __init__(self, namespace):
        super().__init__(namespace)
        self.streams = {}

    # 全体にmultiStream情報を送信
    def update_stream(self, room_id):
        emit("update_stream", self.streams[room_id],
             room=room_id,
             broadcast=True,
             include_self=True)

    # 再接続
    def reconnect(self, data):
        join_room(data["room_id"])

    # 接続時の処理
    def on_join(self, data):
        room = data["room_id"]
        user_name = data["user_name"]
        user_type = data["user_type"]  # streamer, listener
        sql_connection(f"""UPDATE `Room` SET {user_type}={user_type}+1, `count`=count+1 WHERE `room_id`='{room}'""")
        join_room(room)
        is_host = False

        # 部屋がなければ作成
        if not room in self.streams.keys():
            is_host = True
            self.streams[room] = {
                "streamer": {
                    user_name: {
                        "is_host": is_host,
                        "camera": False,
                        "audio": False,
                        "face": 0
                    }
                },
                "listener": [],
                "displayPeer": ""
            }
            emit("host",
                room=room,
                broadcast=False,
                include_self=True)

        if room in self.streams.keys() and (not user_name in self.streams[room]["streamer"].keys()):
            # 配信者参加
            if user_type == "streamer":
                self.streams[room]["streamer"][user_name] = {
                    "is_host": is_host,
                    "camera": False,
                    "audio": False,
                    "face": 0
                }
            
            # 視聴者参加
            else:
                self.streams[room]["listener"].append(user_name)

        # 参加通知用
        emit("join", {
            'user_name': user_name,
            'user_type': user_type
        },  room=room,
            broadcast=True,
            include_self=True)
        self.update_stream(room)
        
    # 退出時の処理
    def on_leave(self, data):
        user_name = data["user_name"]
        room = data["room_id"]
        user_type = data["user_type"]
        myPeer = data["myPeer"]
        remotePeer = data["remotePeer"]
        
        # 部屋が存在しなければ何もしない
        if room in self.streams.keys():

            # ビデオつけたまま抜けるとバグるので削除する
            if myPeer == remotePeer:
                emit("camera_off", {
                    "user_name": user_name,
                    "peer_id": myPeer
                },
                room=room,
                broadcast=True,
                include_self=True)
            
            # dbのユーザーを減らす
            sql_connection(
                f"""UPDATE `Room` SET {user_type}={user_type} - 1 WHERE `room_id`='{room}'""")
            
            is_host = False
            if user_type == "streamer":
                is_host = self.streams[room]["streamer"][user_name]["is_host"]
                del self.streams[room]["streamer"][user_name]
            else:
                if user_name in self.streams[room]["listener"]:
                    self.streams[room]["listener"].remove(user_name)

            # ホストが退出したとき部屋を削除する
            if is_host:
                del self.streams[room]
                emit("delete_room",
                    room=room,
                    broadcast=True,
                    include_self=True)
                sql_connection(
                    f"""UPDATE `Room` SET `is_open`=0, `end_datetime`=NOW() WHERE `room_id`='{room}'""")

            # ホスト以外の時は部屋を更新する
            else:
                emit("leave", {
                    "user_name": user_name,
                    "user_type": user_type,
                },  room=room,
                    broadcast=True,
                    include_self=True)
                self.update_stream(room)

    # 誰がカメラオンにしたか
    def on_camera(self, data):
        room = data["room_id"]
        peer_id = data["peer_id"]
        enable = data["enable"]
        user_name = data["user_name"]

        # オンならこっち
        if enable:
            emit("camera_on", {
                "user_name": user_name,
                "peer_id": peer_id
            },
            room=room,
            broadcast=True,
            include_self=True)

        # オフならこっち
        else:
            emit("camera_off", {
                "user_name": user_name,
                "peer_id": peer_id
            },
            room=room,
            broadcast=True,
            include_self=True)
    
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
    def on_update_user(self, data):
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