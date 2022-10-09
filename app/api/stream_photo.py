from flask_restful import Resource, Api
from flask import Flask, abort, request, jsonify
from app.utils.db_conn import sql_connection
from app.lib.streamphoto import save_streamphoto_diary, get_streamphoto
import os
import json

def is_user_exist(user_id):
    sql_text = f"""SELECT `user_name` FROM `User` WHERE `user_id`='{user_id}'"""
    is_exist = sql_connection(sql_text)
    return is_exist

# 画像記録管理
# 記録内容 - 画像データ(ファイル形式で保存) 
class StreamPhoto(Resource):
    # 画像を記録する
    def post(self):
        # ルームidと各種設定、サムネイル画像を受け取る
        post_data = request.get_json()
        save_streamphoto_diary(post_data)

        # DBに置く
        return '', 204
    
    # 画像名を受け取る
    def get(self):
        user_id = request.args.get('user_id')
        room_id = request.args.get('room_id')
        print("a")
        if is_user_exist(user_id):
            img_data = get_streamphoto(user_id, room_id)
            return jsonify({
                "status": True,
                "comment": "success get img Name!",
                "img_data": img_data
            })

        # ユーザーが存在しなかったらエラーを返す
        else:
            return jsonify({
                "status": False,
                "comment": " your account doesn't exist!"
            })

