# クエスト内容記述ファイル

def achive_loader():
    achives = [
        {
            "title": "ビギナーアングラー",
            "id": 1,
            "max_progress": 1,
            "purpose": "魚を初めて釣り上げる",
            "rewords_text": ["100XP", "ビギナー帽子",],
            "rewords": [
                {
                    "id": "xp",
                    "num": 100
                },
                {
                    "id": "hat-01",
                }
            ]
        },

        {
            "title": "よく見るアイツは迷惑者？",
            "id": 2,
            "max_progress": 3,
            "purpose": "フグを3匹釣り上げる",
            "rewords_text": ["500XP", "フグ帽子"],
            "rewords": [
                {
                    "id": "xp",
                    "num": 500
                },
                {
                    "id": "hat-02",
                }
            ]
        },

        {
            "title": "おめでたい日",
            "id": 3,
            "max_progress": 1,
            "purpose": "タイを1匹釣り上げる",
            "rewords_text": ["500XP", "タイ服"],
            "rewords": [
                {
                    "id": "xp",
                    "num": 500
                },
                {
                    "id": "body-1",
                }
            ]
        },

        {
            "title": "登魚門 - 博士",
            "id": 4,
            "max_progress": 10,
            "purpose": "10種類魚を釣り上げる",
            "rewords_text": ["2000XP", "博士の帽子"],
            "rewords": [
                {
                    "id": "xp",
                    "num": 2000
                },
                {
                    "id": "hat-03",
                }
            ]
        },
        
        {
            "title": "タケノコの季節",
            "id": 5,
            "max_progress": 3,
            "purpose": "タケノコメバルを3匹釣り上げる",
            "rewords_text": ["500XP", "タケノコ帽子"],
            "rewords": [
                {
                    "id": "xp",
                    "num":500
                },
                {
                    "id": "hat-04",
                }
            ]
        },
        
        {
            "title": "真っ赤でトゲトゲ",
            "id": 6,
            "max_progress": 3,
            "purpose": "カサゴを3匹釣り上げる",
            "rewords_text": ["500XP", "カサゴの靴"],
            "rewords": [
                {
                    "id": "xp",
                    "num": 500
                },
                {
                    "id": "foot-01",
                }
            ]
        },
        
        {
            "title": "登魚門 - 少年",
            "id": 7,
            "max_progress": 50,
            "purpose": "50匹魚を釣り上げる",
            "rewords_text": ["5000XP", "魚の服"],
            "rewords": [
                {
                    "id": "xp",
                    "num": 5000
                },
                {
                    "id": "body-2",
                }
            ]
        },
    ]

    return achives