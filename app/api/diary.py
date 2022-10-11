from re import S
from flask_restful import Resource, Api
from flask import Flask, abort, request, jsonify
import json
from app.utils.db_conn import sql_connection
from app.utils.unique_generater import generate_id

class Diary(Resource):
    # 日誌登録
    def post(self):
        post_data = request.get_json()
        title = post_data["title"]
        user_id = post_data["user_id"]
        user_name = post_data["user_name"]
        data = post_data["data"]
        diary_id = generate_id(32)
        locus = json.dumps(data["locus"], ensure_ascii=False)
        sql_connection(f"""INSERT INTO `Diary` (`user_id`, `user_name`, `diary_id`, `is_locked`, `title`, `date`) VALUES ('{user_id}', '{user_name}', '{diary_id}', 1, '{title}', '{data["date"]}')""")
        sql_connection(f"""INSERT INTO `DiaryContent` (`diary_id`, `date`, `fishes`, `place_name`, `group_name`, `user_count`, `timer`, `locus`) VALUES ('{diary_id}', '{data["date"]}', '{data["fishes"]}', '{data["place"]}', '{data["group_name"]}', '{data["entered"]}', '{data["time"]}', '{locus}')""")
        for image_name in data["imgs"]:
            sql_connection(f"""INSERT INTO `DiaryPhoto` (`diary_id`, `img_name`) VALUES ('{diary_id}', '{image_name}')""")
            sql_connection(f"""UPDATE `Diary` SET `thumbnail`='{image_name}' WHERE `diary_id`='{diary_id}'""")

    # 日誌を取得
    def get(self):
        user_id = request.args.get('user_id')

        # 日誌リストを取得
        if user_id:
            data = sql_connection(f"""SELECT `diary_id`, `title`, `date`, `thumbnail` FROM `Diary` WHERE `user_id`='{user_id}' ORDER BY `datetime` DESC""")
            return jsonify(data)

        # 日誌本体を取得
        else:
            diary_id = request.args.get('diary_id')
            data = sql_connection(f"""SELECT * FROM `DiaryContent` WHERE `diary_id`='{diary_id}'""")[0]
            data["locus"] = json.loads(data["locus"])
            imgs = sql_connection(f"""SELECT img_name FROM `DiaryPhoto` WHERE `diary_id`='{diary_id}'""")
            return jsonify({
                "data": data,
                "imgList": imgs
            })
