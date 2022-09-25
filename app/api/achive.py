from flask_restful import Resource, Api
from flask import Flask, abort, request, jsonify
from app.utils.db_conn import sql_connection
from app.lib.achive import AchiveManager
import json

achiveManager = AchiveManager()

class Achive(Resource):
    # 進捗の状態を取得する
    def get(self):
        user_id = request.args.get('user_id')
        achiveManager.register_progress(user_id)
        achive_progresses = achiveManager.get_achive_progress(user_id)
        return jsonify(
            achive_progresses
        )


    