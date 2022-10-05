from app.utils.db_conn import sql_connection
from app.utils.save_b64img import save_b64img
from app.utils.unique_generater import generate_id

def save_streamphoto(post_data):
    room_id = post_data["room_id"]
    user_id = post_data["user_id"]
    user_name = post_data["user_name"]
    lat = post_data["lat"]
    lng = post_data["lng"]
    base64img = post_data["base64img"]
    if base64img:
        # 画像名(extension含む)
        img_name = generate_id(64) + "." + base64img.split(";")[0][11:]
        save_b64img(base64img, savepath="stream_photo/", img_name=img_name)
            
    sql_text = f"""INSERT INTO `StreamPhoto`(`user_id`, `user_name`, `room_id`, `img_name`, `lat`, `lng`) VALUES ('{user_id}', '{user_name}', '{room_id}', '{img_name}', '{lat}', '{lng}')"""
    sql_connection(sql_text)