from flask_restful import Resource, Api
from flask import Flask, abort, request, jsonify
from app.utils.db_conn import sql_connection
from app.lib.quest import QuestManager
import json

questManager = QuestManager()

class Quest(Resource):
    # クエストの状態を取得する
    def get(self):
        user_id = request.args.get('user_id')
        # 進捗がデータ上存在しない場合progressを0として作成
        questManager.register_progress(user_id)
        # 現在のクエスト内容、進捗を取得
        quest_progresses= questManager.get_quest_progress(user_id)
        ordered_quest_id = questManager.get_order(user_id)
        return jsonify(
            {
                "quests" : quest_progresses,
                "ordered_quest_id": ordered_quest_id
            }
        )
    
    # クエストの受注
    def put(self):
        post_data = request.get_json()
        user_id = post_data["user_id"]
        quest_id = post_data["quest_id"]
        # 受注
        questManager.order_quest(user_id, quest_id)
        return jsonify({
                "status": True,
                "comment": f"success order quest {quest_id}",
                "quest_id": quest_id
            })


    