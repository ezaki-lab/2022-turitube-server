from flask_restful import Resource, Api
from flask import Flask, abort, request, jsonify
from app.utils.db_conn import sql_connection
from app.lib.save_streamphoto import save_streamphoto
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
        save_streamphoto(post_data)

        # DBに置く
        return '', 204

    # 画像名を受け取る
    def get(self):
        user_id = request.args.get('user_id')
        if is_user_exist(user_id):
            # 画像名取得
            sql_text = f"""SELECT `img_name` FROM `StreamPhoto` WHERE `user_id`='{user_id}' AND `is_sent`=false"""
            img_name_list = sql_connection(sql_text)
            # 取得したis_sentを全てtrueにして再度取得しないようにする(デバッグ用に今は切る)
            '''
            sql_text = f"""UPDATE `StreamPhoto` SET `is_sent`=true WHERE `user_id`='{user_id}' AND `is_sent`=false"""
            sql_connection(sql_text)
            '''
            return jsonify({
                "status": True,
                "comment": "success get img Name!",
                "img_name_list": img_name_list,
            })

        # ユーザーが存在しなかったらエラーを返す
        else:
            return jsonify({
                "status": False,
                "comment": " your account doesn't exist!"
            })

