from flask_restful import Resource, Api
from flask import Flask, abort, request, jsonify
from app.utils.db_conn import sql_connection
from app.utils.save_b64img import save_b64img
from feat import Detector
import json
from app.utils.unique_generater import generate_id
import os
import random

face_model = "retinaface"
landmark_model = "mobilenet"
au_model = "logistic"
emotion_model = "resmasknet"
detector = Detector(
    face_model=face_model,
    landmark_model=landmark_model,
    emotion_model=emotion_model
)

folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../static/img/')

class Expression(Resource):
    def post(self):
        # デモ用
        return jsonify({
          "detect": False,
          "face_id": random.randint(0, 3),
          "score": 0.6
        })
    
        # 本来の動作
        try:
            data = request.get_json()
            base64img = data["base64img"]
            if len(base64img) > 1000:
                img_name = generate_id(64) + "." + base64img.split(";")[0][11:]
                save_b64img(base64img, savepath="expression/", img_name=img_name)
                imgpath = folder_path + "expression/" + img_name
                face_id_list = {
                  "surprise":0,
                  "neutral": 1,
                  "sad": 2,
                  "anger": 1,
                  "disgust": 2,
                  "fear": 2,
                  "happiness": 3,
                }
                try:
                    image_prediction = detector.detect_image(imgpath)
                except:
                    print("uoooo")
                    # os.remove(imgpath)
                    return jsonify({
                      "detect": False,
                      "face_id": 0,
                      "score": 0
                    })
                os.remove(imgpath)
                tag = image_prediction.emotions.idxmax(axis=1)[0]
                score = image_prediction.emotions.max(axis=1)[0]

                return jsonify({
                  "detect": True,
                  "face_id": face_id_list[tag],
                  "score": float(score)
                })
            else:
                return jsonify({
                    "detect": False,
                    "face_id": 0,
                    "score": 0
                  })

        except:
            return jsonify({
              "detect": False,
              "face_id": 0,
              "score": 0
            })
