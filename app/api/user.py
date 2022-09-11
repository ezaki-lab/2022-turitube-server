from flask_restful import Resource, Api
from flask import Flask, abort, request, jsonify
from app.utils.db_conn import sql_connection
from app.utils.unique_generater import generate_id

import json

# ユーザー情報
class User(Resource):
    # 
    def get(self):
        user_id = request.args.get('user_id')
        sql_text = f"""SELECT `name`, DATE_FORMAT(`last_login`,'%Y年%m月%d日 %h時%i分') AS last_login, DATE_FORMAT(`create_date`, '%Y年%m月%d日') as create_date, `introduction`, `is_login` FROM `User` WHERE `user_id`='{user_id}'"""
        user_data = sql_connection(sql_text)
        return jsonify(user_data[0])

    # ユーザー登録
    def post(self):
        user_name = request.args.get('user_name')
        screen_name = request.args.get('screen_name')
        user_id = generate_id()

        # exist check
        sql_text = f"""SELECT `user_id` FROM `User` WHERE `user_name`='{user_name}'"""
        is_exist = sql_connection(sql_text)
        # ユーザー登録するよ
        if not is_exist:
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
        
        else:
            return jsonify({
                "status": False,
                "comment": "already existed!"
            })

    # ユーザーデータの削除(実装しない)
    def delete(self):
        pass