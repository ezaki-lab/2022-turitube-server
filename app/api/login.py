from re import S
from xml.etree.ElementTree import iselement
from flask_restful import Resource, Api
from flask import Flask, abort, request, jsonify
from app.utils.db_conn import sql_connection
import json

# id準拠のユーザー存在判定
def is_user_exist(user_id):
    sql_text = f"""SELECT `user_name` FROM `User` WHERE `user_id`='{user_id}'"""
    is_exist = sql_connection(sql_text)
    return is_exist

# ログインAPI - userIdを基にログインできるかを判定して、ログインできるならuser_nameとscreen_nameを返す
# signInとは別物
class Login(Resource):
    # ユーザーログイン
    def get(self):
        user_id = request.args.get('user_id')
        # ユーザーが存在したらログインするための情報を返す
        if is_user_exist(user_id):
            sql_text = f"""SELECT `user_id`, `user_name`, `screen_name`, `avatar` FROM `User` WHERE `user_id`='{user_id}'"""
            user_data = sql_connection(sql_text)
            return jsonify({
                "status": True,
                "comment": "success login account!",
                "user_id": user_data[0]["user_id"],
                "user_name": user_data[0]["user_name"],
                "screen_name": user_data[0]["screen_name"],
                "avatar": json.loads(user_data[0]["avatar"])
            })

        # ユーザーが存在しなかったらエラーを返す
        else:
            return jsonify({
                "status": False,
                "comment": " your account doesn't exist!"
            })

    