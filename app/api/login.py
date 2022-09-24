from flask_restful import Resource, Api
from flask import Flask, abort, request, jsonify
from app.utils.db_conn import sql_connection
import json

# id準拠のユーザー存在判定
def is_user_exist(user_id):
    sql_text = f"""SELECT `user_name` FROM `User` WHERE `user_id`='{user_id}'"""
    is_exist = sql_connection(sql_text)
    return is_exist

# ログインAPI - userIdを基にログインできるかを判定して、ログインできるならstatus: trueを返す
# signInとは別物
class Login(Resource):
    # ユーザーログイン
    def get(self):
        user_id = request.args.get('user_id')
        # ユーザーが存在したらログインするための情報を返す
        if is_user_exist(user_id):
            return jsonify({
                "status": True,
                "comment": "success login account!",
            })

        # ユーザーが存在しなかったらエラーを返す
        else:
            return jsonify({
                "status": False,
                "comment": " your account doesn't exist!"
            })

    