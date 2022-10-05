# クエスト関連を操作してくれるファイル
from app.utils.db_conn import sql_connection
import copy
from .picture_book_loader import picture_book_loader

# 図鑑関連をうまくやってくれます
class PictureBookManager():
    def __init__(self):
        pass

    def get_list(self, user_id):
        books = picture_book_loader()
        fishes = sql_connection(f"""SELECT `fish_id`, `img_name` FROM `PictureBook` WHERE `user_id`='{user_id}'""")
        print(fishes)
        for fish in fishes:
            fish_id = fish["fish_id"]
            img_name = fish["img_name"]
            books[fish_id]["data"].append({
                "img": img_name,
            })
        return books

    def get(self, user_id, fish_id):
        book = picture_book_loader()[fish_id]
        fishes = sql_connection(f"""SELECT `img_name`, `datetime`, `lat`, `lng`, `length` FROM `PictureBook` WHERE `user_id`='{user_id}' AND `fish_id`='{fish_id}'""")
        book["data"] = fishes
        return book