from flask_restful import Resource, Api
from flask import Flask, abort, request, jsonify
import json
from app.utils.db_conn import sql_connection

# 配信部屋管理
class Room(Resource):
    # 配信部屋を手に入れる
    def get(self):
        data = sql_connection("""SELECT * FROM `Room` WHERE `is_open`=1""")
        return jsonify(data)
    
    # 配信開始
    def post(self):
        post_data = request.get_json()
        user_name = post_data["user_name"]
        room_id = post_data["room_id"]
        setting = post_data["setting"]
        base64img = post_data["base64img"]
        # サムネイルに画像が無かった時用のファイル名
        img_name = "thumbnail.png"
        if base64img:
            # 画像名(extension含む)
            img_name = generate_id(64) + "." + base64img.split(";")[0][11:]
            save_b64img(base64img, savepath="thumbnail/", img_name=img_name)

        print(post_data)
        
        sql_text = f"""INSERT INTO `Room`(`room_id`, `title`, `tag`, `host_name`, `max_streamer`, `max_listener`, `thumbnail`) VALUES ('{room_id}', '{setting["title"]}', '{setting["tag"]}', '{user_name}', '{setting["max_streamer"]}', '{setting["max_listener"]}', '{img_name}')"""
        sql_connection(sql_text)

        return '', 204


    