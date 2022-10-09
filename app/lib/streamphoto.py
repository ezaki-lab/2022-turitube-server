from app.utils.db_conn import sql_connection
from app.utils.save_b64img import save_b64img
from app.utils.unique_generater import generate_id
from app.utils.reverse_geo_coding import reverse_geo_coding
import cv2
import os

folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../static/img/')

def save_streamphoto_diary(post_data):
    room_id = post_data["room_id"]
    user_id = post_data["user_id"]
    lat = post_data["lat"]
    lng = post_data["lng"]
    base64img = post_data["base64img"]
    img_name = ""
    if base64img:
        # 画像名(extension含む)
        img_name = generate_id(64) + "." + base64img.split(";")[0][11:]
        save_b64img(base64img, savepath="stream_photo/", img_name=img_name)

    place_name = "記録なし"
    if (lat!=0 and lng!=0):
        place_name = reverse_geo_coding(lat, lng)
    
    print(img_name)
    sql_text = f"""INSERT INTO `StreamPhoto`(`user_id`, `room_id`, `img_name`, `lat`, `lng`, `place_name`, `type`) VALUES ('{user_id}', '{room_id}', '{img_name}', '{lat}', '{lng}', '{place_name}', 'diary')"""
    sql_connection(sql_text)

def save_streamphoto_book(post_data, class_id):
    tags = {0: "000", 1: "001", 2:"002", 3: "003", 4:"004", 6:"005", 8:"006", 9:"007", 10:"008", 11:"009", 12:"010", 13:"011", 14:"012", 15:"013", 16:"014", 17:"015"}
    room_id = post_data["room_id"]
    user_id = post_data["user_id"]
    lat = post_data["lat"]
    lng = post_data["lng"]
    img = post_data["img"]
    img_name = generate_id(64) + "." + "jpg"
    cv2.imwrite(f"{folder_path}stream_photo/{img_name}", img)

    place_name = "記録なし"
    if (lat!=0 and lng!=0):
        place_name = reverse_geo_coding(lat, lng)
    
    print(img_name)
    sql_text = f"""INSERT INTO `StreamPhoto`(`user_id`, `room_id`, `img_name`, `lat`, `lng`, `place_name`, `type`, `fish_id`) VALUES ('{user_id}', '{room_id}', '{img_name}', '{lat}', '{lng}', '{place_name}', 'book', '{tags[class_id]}')"""
    sql_connection(sql_text)

def get_streamphoto(user_id, room_id):
    fishes = {
        "000": "void",
        "001":"タケノコメバル",
        "002":"マダイ",
        "003":"カサゴ",
        "004":"アジ",
        "005":"ハゼ",
        "006":"カワハギ",
        "007":"サバ",
        "008":"ブラックバス",
        "009":"ベラ",
        "010":"ウナギ",
        "011":"サケ",
        "012":"タナゴ",
        "013":"クロダイ",
        "014":"キス",
        "015":"ブリ",  
    }
    # 画像名取得
    sql_text = f"""SELECT `img_name`, `place_name`, `type`, `fish_id`, DATE_FORMAT(`datetime`, '%Y-%m-%d %H:%i:%s') as 'datetime' FROM `StreamPhoto` WHERE `user_id`='{user_id}' AND `room_id`='{room_id}'"""
    img_data = sql_connection(sql_text)
    for i in range(len(img_data)):
        img_data[i]["fish"] = fishes[img_data[i]["fish_id"]]

    return img_data