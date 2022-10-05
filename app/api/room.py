from flask_restful import Resource, Api
from flask import Flask, abort, request, jsonify
import json
from app.utils.db_conn import sql_connection
from app.utils.unique_generater import generate_id
from app.utils.save_b64img import save_b64img
import datetime
import pytz

def get_h_m_s(td):
    m, s = divmod(td.total_seconds(), 60)
    h, m = divmod(m, 60)
    return h, m, s

# 配信部屋管理
class Room(Resource):
    # 配信部屋を手に入れる
    def get(self):
        room_id = request.args.get('room_id')
        if room_id:
            dt1 = datetime.datetime.now()
            data = sql_connection(f"""SELECT `title`, `tag`, `host_name`, `thumbnail`, count, DATE_FORMAT(`start_datetime`, '%Y-%m-%d %H:%i:%s') as 'start_datetime' FROM `Room` WHERE `room_id`='{room_id}'""")[0]
            dt2 = datetime.datetime.strptime(data["start_datetime"], '%Y-%m-%d %H:%M:%S')
            data["time"] = f"{int((get_h_m_s(dt1-dt2)[0]))}時間{int((get_h_m_s(dt1-dt2)[1]))}分{int((get_h_m_s(dt1-dt2)[2]))}秒"
            return jsonify(data)
        data = sql_connection("""SELECT * FROM `Room` WHERE `is_open`=1""")
        return jsonify(data)
    
    # 配信開始
    def post(self):
        post_data = request.get_json()
        user_name = post_data["user_name"]
        room_id = post_data["room_id"]
        setting = post_data["setting"]
        base64img = post_data["base64img"]
        # サムネイルに画像が無かった時用のファイル名
        img_name = "thumbnail.png"
        if base64img:
            # 画像名(extension含む)
            img_name = generate_id(64) + "." + base64img.split(";")[0][11:]
            save_b64img(base64img, savepath="thumbnail/", img_name=img_name)
        
        sql_text = f"""INSERT INTO `Room`(`room_id`, `title`, `tag`, `host_name`, `max_streamer`, `max_listener`, `thumbnail`) VALUES ('{room_id}', '{setting["title"]}', '{setting["tag"]}', '{user_name}', '{setting["max_streamer"]}', '{setting["max_listener"]}', '{img_name}')"""
        sql_connection(sql_text)

        print("uoo")
        return '', 204


    