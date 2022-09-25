from flask_restful import Resource, Api
from flask import Flask, abort, request, jsonify
from app.lib.picture_book import PictureBookManager
import json

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


    