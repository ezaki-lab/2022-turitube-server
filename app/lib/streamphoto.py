from app.utils.db_conn import sql_connection
from app.utils.save_b64img import save_b64img
from app.utils.unique_generater import generate_id
from app.utils.reverse_geo_coding import reverse_geo_coding

def save_streamphoto(post_data):
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
    sql_text = f"""INSERT INTO `StreamPhoto`(`user_id`, `room_id`, `img_name`, `lat`, `lng`, `place_name`) VALUES ('{user_id}', '{room_id}', '{img_name}', '{lat}', '{lng}', '{place_name}')"""
    sql_connection(sql_text)

def get_streamphoto(user_id, room_id):
    # 画像名取得
    sql_text = f"""SELECT `img_name`, `place_name` FROM `StreamPhoto` WHERE `user_id`='{user_id}' AND `room_id`='{room_id}'"""
    img_data = sql_connection(sql_text)
    # 取得したis_sentを全てtrueにして再度取得しないようにする(デバッグ用に今は切る)
    '''
    sql_text = f"""UPDATE `StreamPhoto` SET `is_sent`=true WHERE `user_id`='{user_id}' AND `is_sent`=false"""
    sql_connection(sql_text)
    '''

    return img_data