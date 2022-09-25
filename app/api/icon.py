from flask_restful import Resource, Api
from flask import Flask, abort, request, jsonify
from app.utils.db_conn import sql_connection
from app.lib.quest import QuestManager
import json
from app.utils.unique_generater import generate_id
from app.utils.save_b64img import save_b64img

class Icon(Resource):
    # アイコンを変更
    def put(self):
        post_data = request.get_json()
        user_id = post_data["user_id"]
        base64img = post_data["base64img"]
        if base64img:
            # 画像名(extension含む)
            img_name = generate_id(64) + "." + base64img.split(";")[0][11:]
            save_b64img(base64img, savepath="icon/", img_name=img_name)
            sql_connection(f"""UPDATE `User` SET `icon`='{img_name}' WHERE `user_id`='{user_id}'""")

        return jsonify({
                "status": True,
                "comment": f"success register icon",
                "img_name": img_name
            })


    