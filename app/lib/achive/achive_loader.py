# クエスト内容記述ファイル

def achive_loader():
    achives = {
        "001": {
            "title": "魚を初めて釣り上げる",
            "max_progress": 1,
            "rewords_text": ["100xp", "100pt"],
            "rewords": [
                {
                    "id": "xp",
                    "num": 100,
                },
                {
                    "id": "pt",
                    "num": 100,
                }
            ]
        },
        "002": {
            "title": "魚を初めて釣り上げる2",
            "max_progress": 2,
            "rewords_text": ["200xp", "200pt"],
            "rewords": [
                {
                    "id": "xp",
                    "num": 200,
                },
                {
                    "id": "pt",
                    "num": 200,
                }
            ]
        },
        "003": {
            "title": "魚を初めて釣り上げる3",
            "max_progress": 3,
            "rewords_text": ["300xp", "300pt"],
            "rewords": [
                {
                    "id": "xp",
                    "num": 300,
                },
                {
                    "id": "pt",
                    "num": 300,
                }
            ]
        },
        "004": {
            "title": "魚を初めて釣り上げる4",
            "max_progress": 4,
            "rewords_text": ["400xp", "400pt"],
            "rewords": [
                {
                    "id": "xp",
                    "num": 400,
                },
                {
                    "id": "pt",
                    "num": 400,
                }
            ]
        },
    }

    return achives