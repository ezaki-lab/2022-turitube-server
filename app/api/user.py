from re import S
from xml.etree.ElementTree import iselement
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
        user_id = request.args.get('user_id')
        name = request.args.get('name')
        ident_id = generate_id()

        # exist check
        sql_text = f"""SELECT `user_id` FROM `User` WHERE `user_id`='{user_id}'"""
        is_exist = sql_connection(sql_text)
        if not is_exist:
            sql_text = f"""INSERT INTO `User`(`id`, `user_id`, `name`) VALUES ('{ident_id}', '{user_id}', '{name}')"""
            sql_connection(sql_text)

            #正常に登録できたら204
            return jsonify({
                "status": True,
                "comment": "success create account!",
                "ident_id": ident_id,
                "user_id": user_id,
                "name": name
            })
        
        else:
            return jsonify({
                "status": False,
                "comment": "already existed!"
            })

    # ユーザー情報の更新
    def put(self):
        pass

    # ユーザーデータの削除(実装しない)
    def delete(self):
        pass