from re import S
from xml.etree.ElementTree import iselement
from flask_restful import Resource, Api
from flask import Flask, abort, request, jsonify
from app.utils.db_conn import sql_connection
from app.utils.unique_generater import generate_id

import json

def is_user_exist(user_name):
    sql_text = f"""SELECT `user_name` FROM `User` WHERE `user_name`='{user_name}'"""
    is_exist = sql_connection(sql_text)
    return is_exist

# サインイン管理用API
class SignIn(Resource):
    # ユーザーログイン
    def get(self):
        user_name = request.args.get('user_name')
        # ユーザーが存在したらログインするための情報を返す

        if is_user_exist(user_name):
            sql_text = f"""SELECT `user_id`, `user_name`, `screen_name` FROM `User` WHERE `user_name`='{user_name}'"""
            user_data = sql_connection(sql_text)
            return jsonify({
                "status": True,
                "comment": "success login account!",
                "user_id": user_data[0]["user_id"],
                "user_name": user_data[0]["user_name"],
                "screen_name": user_data[0]["screen_name"],
            })

        # ユーザーが存在しなかったらエラーを返す
        else:
            return jsonify({
                "status": False,
                "comment": " your account doesn't exist!"
            })

        
    # ユーザー登録
    def post(self):
        user_name = request.get_json()["user_name"]
        screen_name = request.get_json()["screen_name"]
        user_id = generate_id()

        # ユーザーが存在しなかったら作成
        if not is_user_exist(user_name):
            sql_text = f"""INSERT INTO `User`(`user_id`, `user_name`, `screen_name`) VALUES ('{user_id}', '{user_name}', '{screen_name}')"""
            sql_connection(sql_text)

            #正常に登録できたら204
            return jsonify({
                "status": True,
                "comment": "success create account!",
                "user_id": user_id,
                "user_name": user_name,
                "screen_name": screen_name
            })

        # ユーザーが存在したらエラーを返す
        else:
            return jsonify({
                "status": False,
                "comment": "already existed!"
            })
    