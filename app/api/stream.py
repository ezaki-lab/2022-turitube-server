from flask_restful import Resource, Api
from flask import Flask, abort, request, jsonify
from app.utils.db_conn import sql_connection
from app.utils.save_b64img import save_b64img
from app.utils.unique_generater import generate_id
import os
import json

# 配信管理
class Stream(Resource):
    # 配信スタート時
    def post(self):
        # ルームidと各種設定、サムネイル画像を受け取る
        post_data = request.get_json()
        room_id = post_data["room_id"]
        setting = json.dumps(post_data["setting"], ensure_ascii=False)
        base64img = post_data["base64img"]
        # サムネイルに画像が無かった時用のファイル名
        img_name = "thumbnail.png"
        if base64img:
            # 画像名(extension含む)
            img_name = generate_id(64) + "." + base64img.split(";")[0][11:]
            save_b64img(base64img, savepath="thumbnail/", img_name=img_name)
        
        sql_text = f"""INSERT INTO `Stream`(`room_id`, `room_setting`, `thumbnail`) VALUES ('{room_id}', '{setting}', '{img_name}')"""
        sql_connection(sql_text)
        # DBに置く
        return '', 204
    
    # 配信情報を受け取る
    def get(self):
        sql_text = f"""SELECT room_id, room_setting, users, thumbnail FROM `Stream` WHERE `is_open`=1"""
        result = sql_connection(sql_text)
        for i in range(len(result)):
            result[i]['users'] = json.loads(result[i]['users'])
            result[i]['room_setting'] = json.loads(result[i]['room_setting'])
            result[i]['room_setting']['tag'] = list(map(str, result[i]['room_setting']['tag'].split(" ")))

        return jsonify(result)





