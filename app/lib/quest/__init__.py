# クエスト関連を操作してくれるファイル
from .quest_loader import quest_loader
from app.utils.db_conn import sql_connection
import copy

# 進捗関連をうまくやってくれます
class QuestManager():
    def __init__(self):
        self.quest_list = quest_loader()

    # クエスト1 - ビギナーアングラー
    def quest_1(self):
        pass
    
    # クエスト1 - よく見るアイツは迷惑者？
    def quest_2(self):
        pass
    
    # クエスト1 - おめでたい日
    def quest_3(self):
        pass
    
    # クエスト1 - 登魚門
    def quest_4(self):
        pass

    # クエストの進捗状態が存在しないものを登録します。
    def register_progress(self, user_id):
        for key in self.quest_list:
            # 存在可否の判定
            if not sql_connection(f"""SELECT id FROM `ProgressQuest` WHERE `user_id`='{user_id}' AND `id`='{key}'"""):
                sql_connection(f"""INSERT INTO `ProgressQuest`(`id`, `user_id`, `progress`) VALUES ('{key}', '{user_id}', 0)""")
    
    # これに投げれば魚系のクエストの進捗進む関数
    def advance_fish_quest(self, quest_id, user_id, fish_id):
        pass
    
    # クエスト進捗状態を受け取ります。
    def get_quest_progress(self, user_id):
        progresses = sql_connection(f"""SELECT `progress`, `id`, `is_order` FROM `ProgressQuest` WHERE `user_id`='{user_id}'""")
        quest_list = quest_loader()
        # クエストの進捗を書き込み
        # あんまりやりたくないけど仕方ない最大O(N^2)
        for progress in progresses:
            quest_list[progress["id"]]["progress"] = progress["progress"] 
                
        return quest_list

    # 受注しているクエストIDをゲットします
    def get_order(self, user_id):
        try:
            quest_id = sql_connection(f"""SELECT `id` FROM `ProgressQuest` WHERE `user_id`='{user_id}' AND `is_order`=true""")[0]["id"]
        except IndexError:
            quest_id=0
        return quest_id

    # クエストを受注します
    def order_quest(self, user_id, quest_id):
        sql_connection(f"""UPDATE `ProgressQuest` SET `is_order`=false WHERE `user_id`='{user_id}'""")
        sql_connection(f"""UPDATE `ProgressQuest` SET `is_order`=true WHERE `user_id`='{user_id}' AND `id`='{quest_id}'""")
        

        
        

    

    