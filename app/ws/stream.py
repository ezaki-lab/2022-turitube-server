from xml.etree.ElementInclude import include
from flask import request
from flask_socketio import emit, join_room, leave_room, Namespace
from app.utils.db_conn import sql_connection
import json

"""
self.stream
{
    room_id:{
        room_setting:{
            ...
        }
        "users":[
            {
                "username": "kosakae256",
                "screen_name": "小坂",
                "avater_pattern": [0,0,0,0,0],
                "pos_x": 0.2,
                "pos_y": 0.2 
            },
            {
                ...
            }
        ]
    }
}
"""

class Stream(Namespace):
    def __init__(self, namespace):
        super().__init__(namespace)
        self.user_count = 0
        self.text = ""
        self.stream = {"sid":{}}

    # room生成時に実行
    def init_stream_room(self, room):
        self.stream[room] = {}
        self.stream[room]["users"] = []
        self.stream[room]["room_setting"] = {}

    # room情報更新時に実行
    # 対象のroomにroomデータ送信とDBに反映
    def update_room(self, room):
        # room情報更新
        emit("update_room",
        self.stream[room],
        broadcast=True,
        include_self=True,
        room=room)
        self.reflection_room_of_db(room)

    # room情報をDBに反映
    def reflection_room_of_db(self, room):
        room_id = room
        is_open = self.stream[room]["is_open"]
        room_setting = json.dumps(self.stream[room]["room_setting"], ensure_ascii=False)
        users = json.dumps(self.stream[room]["users"], ensure_ascii=False)
        sql_text = f"""UPDATE `Stream` SET `is_open`={is_open}, `room_setting`='{room_setting}', `users`='{users}' WHERE `room_id`='{room_id}'"""
        sql_connection(sql_text)

    def delete_room(self, room):
        self.stream[room]["is_open"] = False
        self.reflection_room_of_db(room)
        del self.stream[room]

    # 切断時a
    def on_disconnect(self):
        print("切断", request.sid)
        sid = request.sid
        target_room = self.stream["sid"][sid]["room"]
        # room内のユーザーを削除する
        deleted_index = 0
        del self.stream["sid"][sid]

        # 2回実行されるのでエラーを吐くが気にしてはいけない
        try:
            for i, users in enumerate(self.stream[target_room]["users"]):
                if users["sid"] == sid:
                    del self.stream[target_room]["users"][i]
                    deleted_index = i
            
            # 部屋内のユーザーが0人になったらdb更新後、部屋を削除する
            if self.stream[target_room]["users"] == []:
                self.delete_room(target_room)
            
            # リーダーが退出したとき、部屋を削除+emitで通知
            else:
                if deleted_index == 0:
                    self.delete_room(target_room)
                    emit("deleted_room", 
                    broadcast=True,
                    include_self=True,
                    room=target_room)
                else:
                    self.update_room(target_room)
        except KeyError:
            pass

    # ルーム参加(作成込み)時の処理(DBにはすでに反映されている)
    def on_join(self, data):
        print("接続", request.sid)
        room = data["room_id"]
        sid = request.sid
        user_name = data["user_name"]
        screen_name = data["screen_name"]
        avatar = data["avatar"]
        host = False

        # ルームが無ければ作成する
        if not room in self.stream.keys():
            self.init_stream_room(room)
            host = True
            room_setting = json.loads(sql_connection(f"""SELECT `room_setting` FROM `Stream` WHERE `room_id`='{room}'""")[0]["room_setting"])
            self.stream[room]["room_setting"] = room_setting
            # これはAPI側でやる処理
            # sql_connection(f"""INSERT INTO `Stream`(`room_id`) VALUES ('{room}')""")
        
        self.stream["sid"][sid] = {"room": room, "user_name": user_name}
        self.stream[room]["users"].append({
            "sid": sid,
            "peer_id": "?",
            "user_name": user_name,
            "screen_name": screen_name,
            "pos_x": 0,
            "pos_y": 0,
            "cam": False,
            "mic": False,
            "is_host": host,
            "is_streamer": host, # ホストは始めから配信者扱い、ホスト以外はリスナー扱い
            "is_loading": True,
            "avatar":avatar
        })
        
        self.stream[room]["is_open"] = True

        join_room(room)

        # チャットに送信
        emit("text_update",
        {
            "text": room
        },
        broadcast=True,
        include_self=True,
        room=room)

        emit("init_user_setting", 
        {
            "is_host": host,
            "is_streamer": host
        })

        # room情報更新
        self.update_room(room)

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
    
    # セキュリティが必要ならuser_idを使うこと
    def on_update_user(self, data):
        room = data["room_id"]
        user_stream = data["user"]
        for i, users in enumerate(self.stream[room]["users"]):
            if users["sid"] == data["user"]["sid"]:
                self.stream[room]["users"][i] = user_stream
        
        self.update_room(room)
        
