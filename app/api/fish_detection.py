from flask_restful import Resource, Api
from flask import Flask, abort, request, jsonify
import json
from app.lib.streamphoto import save_streamphoto_book
from app.lib.fish_detection import FishDetectionManager
from app.utils.base64_to_img import base64_to_img
from app.utils.img_to_base64 import img_to_base64
from app.utils.unique_generater import generate_id

fishDetectionManager = FishDetectionManager()

counter = {}

class FishDetection(Resource):
    def __init__(self):
        self.classes = ["", "take", "madai", "kasago", "aji", "", "haze", "", "kawahagi", "saba","burakkubasu", "bera", "unagi", "sake", "tanago", "kurodai", "kisu", "buri"]
        """
        {
            user_id:{
                id: 13,
                count: 0
            }
        }
        """

    def post(self):
        data = request.get_json()
        base64img = data["base64img"]
        user_id = data["user_id"]
        img = base64_to_img(base64img)
        class_id, cutout_img = fishDetectionManager.detect(img)
        # 新規作成
        if not user_id in counter.keys():
            counter[user_id] = {
                "id": class_id,
                "count": 0
            }


        # 推論無し
        if class_id==0:
            del counter[user_id]
            return jsonify({
                "detecting": False,
                "detected": False
            })

        # 前の推論と同じなら
        elif counter[user_id]["id"]==class_id:
            counter[user_id]["count"] += 1

        # 前の推論と違うIDなら
        else:
            counter[user_id]["count"] = 1
            counter[user_id]["id"] = class_id
        
        # 推論完了。切り出し画像を保存する
        if counter[user_id]["count"] == 5:
            data["img"] = cutout_img
            save_streamphoto_book(data, class_id)
            del counter[user_id]
            return jsonify({
                "detecting": True,
                "detected": True,
                "class_id": str(class_id),
                "name": self.classes[class_id]
            })

        # 現在の識別状況を返す
        return jsonify({
                "detecting": True,
                "detected": False,
                "count": counter[user_id]["count"],
                "class_id": str(class_id),
                "name": self.classes[class_id],
            })




    