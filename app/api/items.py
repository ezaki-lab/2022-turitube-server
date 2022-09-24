from flask_restful import Resource, Api
from flask import Flask, abort, request, jsonify
from app.utils.db_conn import sql_connection
import json

# アイテム関連
class Items(Resource):
    # タイプに応じたアイテムを返す
    def get(self):
        user_id = request.args.get('user_id')
        _type = request.args.get('type')
        data = sql_connection(f"""SELECT `item_id`, `amount` FROM `Item` WHERE `user_id`='{user_id}' AND `type`='{_type}'""")
        return jsonify(data)

    