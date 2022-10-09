from flask_restful import Resource, Api
from flask import Flask, abort, request, jsonify
from app.lib.picture_book import PictureBookManager
import json

from app.utils.db_conn import sql_connection

pictureBookManager = PictureBookManager()

class PictureBook(Resource):
    # 図鑑情報をゲット(全ての魚)
    def get(self):
        user_id = request.args.get('user_id')
        fish_id = request.args.get('fish_id')
        book = pictureBookManager.get(user_id, fish_id)

        return jsonify({
                "status": True,
                "comment": f"success register icon",
                "book": book
            })
    # 図鑑に記録
    def post(self):
        post_data = request.get_json()
        data = post_data["data"]
        user_id = post_data["user_id"]
        user_name = post_data["user_name"]
        for d in data:
            sql_connection(f"""INSERT INTO `PictureBook`(`user_id`, `user_name`, `fish_id`, `img_name`, `datetime`, `place_name`, `size`) VALUES ('{user_id}', '{user_name}', '{d["fish_id"]}', '{d["img_name"]}', '{d["datetime"]}', '{d["place_name"]}', '{d["size"]}')""")


    