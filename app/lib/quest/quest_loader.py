# クエスト内容記述ファイル

def quest_loader():
    quests = {
        "001": {
            "title": "クエスト1",
            "content": "クエスト1の目的",
            "max_progress": 2,
            "items": [{
                "id": "900",
                "amount": 200
            },
            {
                "id": "901",
                "amount": 200
            }]
        },
        "002": {
            "title": "クエスト2",
            "content": "クエスト2の目的",
            "max_progress": 4,
            "items": [{
                "id": "900",
                "amount": 300
            },
            {
                "id": "901",
                "amount": 300
            }]
        }
    }

    return quests