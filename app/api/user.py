from flask_restful import Resource, Api
from flask import Flask, abort, request, jsonify
from app.utils.db_conn import sql_connection
from app.utils.unique_generater import generate_id

import json

# ユーザー情報
class User(Resource):
    # user_idからユーザー情報を取得
    def get(self):
        user_id = request.args.get('user_id')
        sql_text = f"""SELECT `name`, DATE_FORMAT(`last_login`,'%Y年%m月%d日 %h時%i分') AS last_login, DATE_FORMAT(`create_date`, '%Y年%m月%d日') as create_date, `introduction`, `is_login` FROM `User` WHERE `user_id`='{user_id}'"""
        user_data = sql_connection(sql_text)
        return jsonify(user_data[0])

    # ユーザー登録
    def post(self):
        print(request.json)
        user_id = request.json['user_id']
        name = request.json['name']
        email = request.json['email']
        id = generate_id()
        sql_text = f"""INSERT INTO `User`(`id`, `user_id`, `email`, `name`) VALUES ('{id}', '{user_id}', '{email}', '{name}')"""
        sql_connection(sql_text)

        #正常に登録できたので、HTTP status=204(NO CONTENT)を返す
        return '', 204

    # ユーザー情報の更新
    def put(self):
        pass

    # ユーザーデータの削除(実装しない)
    def delete(self):
        pass