from flask_restful import Resource, Api
from flask import Flask, abort, request, jsonify
from app.utils.db_conn import sql_connection
from app.lib.detection.speacies_detection import SpeaciesDetectionManager
from app.lib.save_streamphoto import save_streamphoto
import json

# 魚種判別関連
class Speacies(Resource):
    def __init__(self):
        self.manager = SpeaciesDetectionManager()

    # 魚種判別します
    def post(self):
        # ルームidと各種設定、サムネイル画像を受け取る
        post_data = request.get_json()
        room_id = post_data["room_id"]
        user_id = post_data["user_id"]
        user_name = post_data["user_name"]
        lat = post_data["lat"]
        lng = post_data["lng"]
        base64img = post_data["base64img"]
        """
        result
        {
            id: int,
            name: str
        }
        """
        result = self.manager.detect()
        if not result["id"]:
            result["status"] = 404
            return jsonify(
                result
            )

        # 推論結果が存在したら画像を保存
        save_streamphoto(post_data)
        # クエストと実績の進捗を進める
        # 進捗が進んだデータを受け取る
        result["quest_progress"] = []
        result["achive_progress"] = []
        result["status"] = 200
        return jsonify(
            result
        )
