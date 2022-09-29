from flask_restful import Resource, Api
from flask import Flask, abort, request, jsonify
from app.utils.db_conn import sql_connection
from app.utils.unique_generater import generate_id

import json

# ユーザー情報
class User(Resource):
    # user_idからユーザーデータを全取得する。またはuser_nameからわかるユーザーデータを取得する。
    def get(self):
        user_id = request.args.get('user_id')
        # user_id(本人)
        if user_id:
            sql_text = f"""SELECT `user_id`, `user_name`, `screen_name`, `icon`, `introduction`, `point`, `exp`, `lv`, `title` FROM `User` WHERE `user_id`='{user_id}'"""
            data = sql_connection(sql_text)[0]
            sql_text = f"""SELECT `hat`, `head`, `body`, `waist`, `fishing_rod` FROM `Avatar` WHERE `user_id`='{user_id}'"""
            avatar = sql_connection(sql_text)[0]
            data["avatar"] = avatar 
            return jsonify(data)
        # user_name(他人)
        else:
            user_name = request.args.get('user_name')
            sql_text = f"""SELECT `user_name`, `screen_name`, `icon`, `introduction`, `exp`, `lv`, `title` FROM `User` WHERE `user_name`='{user_name}'"""
            data = sql_connection(sql_text)[0]
            sql_text = f"""SELECT `hat`, `head`, `body`, `waist`, `fishing_rod` FROM `Avatar` WHERE `user_name`='{user_name}'"""
            avatar = sql_connection(sql_text)[0]
            data["avatar"] = avatar 
            return jsonify(data)


    # ユーザー情報の更新
    def put(self):
        user_data = request.get_json()
        user_id = user_data["user_id"]
        screen_name = user_data["screen_name"]
        icon = user_data["icon"]
        introduction = user_data["introduction"]
        title = user_data["title"]
        avatar_hat = user_data["avatar"]["hat"]
        avatar_head = user_data["avatar"]["head"]
        avatar_body = user_data["avatar"]["body"]
        avatar_waist = user_data["avatar"]["waist"]
        avatar_fishing_rod = user_data["avatar"]["fishing_rod"]
        sql_connection(f"""UPDATE `User` SET `screen_name`='{screen_name}', `icon`='{icon}', `introduction`='{introduction}', `title`='{title}' WHERE `user_id`='{user_id}'""")
        sql_connection(f"""UPDATE `Avatar` SET `hat`='{avatar_hat}', `head`='{avatar_head}', `body`='{avatar_body}', `waist`='{avatar_waist}', `fishing_rod`='{avatar_fishing_rod}' WHERE `user_id`='{user_id}'""")

    # ユーザーデータの削除、作らないかも
    def delete(self):
        pass