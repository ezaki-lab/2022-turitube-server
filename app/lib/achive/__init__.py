# クエスト関連を操作してくれるファイル
from .achive_loader import achive_loader
from app.utils.db_conn import sql_connection
import copy

# 実績関連をうまくやってくれます
class AchiveManager():
    def __init__(self):
        self.achive_list = achive_loader()

    # クエスト1 - ビギナーアングラー
    def achive_1(self):
        pass
    
    # クエスト1 - よく見るアイツは迷惑者？
    def achive_2(self):
        pass
    
    # クエスト1 - おめでたい日
    def achive_3(self):
        pass
    
    # クエスト1 - 登魚門
    def achive_4(self):
        pass

    # 実績の進捗状態が存在しないものを登録します。
    def register_progress(self, user_id):
        for key in self.achive_list:
            # 存在可否の判定
            if not sql_connection(f"""SELECT id FROM `ProgressAchive` WHERE `user_id`='{user_id}' AND `id`='{key}'"""):
                sql_connection(f"""INSERT INTO `ProgressAchive`(`id`, `user_id`, `progress`) VALUES ('{key}', '{user_id}', 0)""")
    
    # これに投げれば魚系の実績の進捗進む関数
    def advance_fish_achive(self, achive_id, user_id, fish_id):
        pass
    
    # 実績進捗状態を受け取ります。
    def get_achive_progress(self, user_id):
        progresses = sql_connection(f"""SELECT `progress`, `id` FROM `ProgressAchive` WHERE `user_id`='{user_id}'""")
        achive_list = achive_loader()

        # 実績の進捗を書き込み
        for progress in progresses:
            achive_list[progress["id"]]["progress"] = progress["progress"]
                
        return achive_list
        

        
        

    

    