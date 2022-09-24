from flask_restful import Resource, Api
from flask import Flask, abort, request, jsonify
from app.utils.db_conn import sql_connection
from app.utils.unique_generater import generate_id

import json


def is_user_exist(user_name):
    sql_text = f"""SELECT `user_name` FROM `User` WHERE `user_name`='{user_name}'"""
    is_exist = sql_connection(sql_text)
    return is_exist

# ユーザー登録時の初期化処理
def initial_user(user_id, user_name):
    print("a")
    # ユーザーを登録
    sql_text = f"""INSERT INTO `User`(`user_id`, `user_name`) VALUES ('{user_id}', '{user_name}')"""
    sql_connection(sql_text)

    # ユーザーのアバター初期値を登録
    sql_text = f"""INSERT INTO `Avatar`(`user_id`, `user_name`) VALUES ('{user_id}', '{user_name}')"""
    sql_connection(sql_text)

    # ユーザーの所持アイテムを登録、初期状態ではナンバー000、タイトル釣りチューブ、アバターの基本装備全15種を所持
    sql_text = f"""INSERT INTO `Item`(`user_id`, `user_name`, `item_id`, `amount`, `type`) VALUES ('{user_id}', '{user_name}', '000', 1, 'title')"""
    sql_connection(sql_text)

    # アバター
    item_ids = ["100", "101", "102", "200", "201", "202", "300", "301", "302", "400", "401", "402", "500", "501", "502"]
    types = ["hat", "hat", "hat", "head", "head", "head", "body", "body", "body", "waist", "waist", "waist", "fishing_rod", "fishing_rod", "fishing_rod"]
    sql_text = f"""INSERT INTO `Item`(`user_id`, `user_name`, `item_id`, `amount`, `type`) VALUES """
    for i, item_id in enumerate(item_ids):
        sql_text = sql_text + f"""('{user_id}', '{user_name}', '{item_id}', 1, 'avatar_{types[i]}')"""
        if item_id == "502":
            sql_text = sql_text + ";"
        else:
            sql_text = sql_text + ","
    sql_connection(sql_text)

# サインイン管理用API
class SignIn(Resource):
    # ユーザーログイン
    def get(self):
        user_name = request.args.get('user_name')
        # ユーザーが存在したらログインするための情報+status trueを返す

        if is_user_exist(user_name):
            sql_text = f"""SELECT `user_id` FROM `User` WHERE `user_name`='{user_name}'"""
            user_data = sql_connection(sql_text)
            return jsonify({
                "status": True,
                "comment": "success login account!",
                "user_id": user_data[0]["user_id"],
            })

        # ユーザーが存在しなかったらstatus falseを返す
        else:
            return jsonify({
                "status": False,
                "comment": " your account doesn't exist!"
            })

    # ユーザー登録

    def post(self):
        user_name = request.get_json()["user_name"]
        user_id = generate_id()

        # ユーザーが存在しなかったら作成
        if not is_user_exist(user_name):
            initial_user(user_id, user_name)

            # 正常に登録できたらログインするための情報+status trueを返す
            return jsonify({
                "status": True,
                "comment": "success create account!",
                "user_id": user_id,
            })

        # ユーザーが存在したらstatus falseを返す
        else:
            return jsonify({
                "status": False,
                "comment": "already existed!"
            })

    # ユーザー情報の更新 使ってないしUserの方でやったほうがいいのでそっちでやる
    def put(self):
        post_data = request.get_json()
        sql_text = f"""UPDATE `User` SET `user_name`='{post_data["user_name"]}', `screen_name`='{post_data["screen_name"]}', `avatar`='{json.dumps(post_data["avatar"], ensure_ascii=False)}' WHERE `user_id`='{post_data["user_id"]}'"""
        sql_connection(sql_text)
