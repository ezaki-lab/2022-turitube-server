# クエスト内容記述ファイル

def quest_loader():
    quests = {
        "001": {
            "title": "初めての釣り",
            "content": "魚を一匹釣りあげる",
            "max_progress": 1,
            "items": [{
                "id": "900",
                "amount": 500
            },
            {
                "id": "901",
                "amount": 500
            }]
        },
        "002": {
            "title": "海底を駆けるもの",
            "content": "ハゼを3匹釣り上げる",
            "max_progress": 3,
            "items": [{
                "id": "900",
                "amount": 300
            },
            {
                "id": "901",
                "amount": 300
            }]
        },
        "003": {
            "title": "誰にも奴は止められない",
            "content": "マグロを一匹釣り上げる",
            "max_progress": 1,
            "items": [{
                "id": "900",
                "amount": 300
            },
            {
                "id": "901",
                "amount": 300
            }]
        },
        "004": {
            "title": "海の厄介者たち",
            "content": "クサフグまたはゴンズイを合計5匹釣り上げる",
            "max_progress": 5,
            "items": [{
                "id": "900",
                "amount": 300
            },
            {
                "id": "901",
                "amount": 300
            }]
        },
        "005": {
            "title": "可愛いものにも毒がある",
            "content": "ゴンズイを3匹釣り上げる",
            "max_progress": 3,
            "items": [{
                "id": "900",
                "amount": 300
            },
            {
                "id": "901",
                "amount": 300
            }]
        },
        "006": {
            "title": "めでタイ！",
            "content": "タイを1匹釣り上げる",
            "max_progress": 1,
            "items": [{
                "id": "900",
                "amount": 300
            },
            {
                "id": "901",
                "amount": 300
            }]
        },
        "007": {
            "title": "美味なる黒",
            "content": "ブラックバスを1匹釣り上げる",
            "max_progress": 1,
            "items": [{
                "id": "900",
                "amount": 300
            },
            {
                "id": "901",
                "amount": 300
            }]
        },
        "008": {
            "title": "陰と陽",
            "content": "タイとクロダイをそれぞれ1匹釣り上げる",
            "max_progress": 2,
            "items": [{
                "id": "900",
                "amount": 300
            },
            {
                "id": "901",
                "amount": 300
            }]
        },
        "009": {
            "title": "海の女王",
            "content": "キスを3匹釣り上げる",
            "max_progress": 3,
            "items": [{
                "id": "900",
                "amount": 300
            },
            {
                "id": "901",
                "amount": 300
            }]
        },
        "010": {
            "title": "餌取り名人",
            "content": "カワハギを3匹釣り上げる",
            "max_progress": 3,
            "items": [{
                "id": "900",
                "amount": 300
            },
            {
                "id": "901",
                "amount": 300
            }]
        },
        "011": {
            "title": "ざわめく海",
            "content": "イワシを3匹釣り上げる",
            "max_progress": 3,
            "items": [{
                "id": "900",
                "amount": 300
            },
            {
                "id": "901",
                "amount": 300
            }]
        },
        "012": {
            "title": "穴釣りといえば...",
            "content": "カサゴを3匹釣り上げる",
            "max_progress": 3,
            "items": [{
                "id": "900",
                "amount": 300
            },
            {
                "id": "901",
                "amount": 300
            }]
        },
        "013": {
            "title": "春を告げる魚",
            "content": "メバルを3匹釣り上げる",
            "max_progress": 3,
            "items": [{
                "id": "900",
                "amount": 300
            },
            {
                "id": "901",
                "amount": 300
            }]
        },
        "014": {
            "title": "熱気に勝るもの",
            "content": "ウナギを3匹釣り上げる",
            "max_progress": 3,
            "items": [{
                "id": "900",
                "amount": 300
            },
            {
                "id": "901",
                "amount": 300
            }]
        },
        "015": {
            "title": "渓流の王",
            "content": "イワナを3匹釣り上げる",
            "max_progress": 3,
            "items": [{
                "id": "900",
                "amount": 300
            },
            {
                "id": "901",
                "amount": 300
            }]
        },
        "016": {
            "title": "渓流の女王",
            "content": "ヤマメを3匹釣り上げる",
            "max_progress": 3,
            "items": [{
                "id": "900",
                "amount": 300
            },
            {
                "id": "901",
                "amount": 300
            }]
        },
        "017": {
            "title": "陰の偽物",
            "content": "メジナを3匹釣り上げる",
            "max_progress": 3,
            "items": [{
                "id": "900",
                "amount": 300
            },
            {
                "id": "901",
                "amount": 300
            }]
        },
        "018": {
            "title": "鮒に始まり鮒に終わる",
            "content": "フナを3匹釣り上げる",
            "max_progress": 3,
            "items": [{
                "id": "900",
                "amount": 300
            },
            {
                "id": "901",
                "amount": 300
            }]
        },
        "019": {
            "title": "音を立てるな",
            "content": "オイカワを3匹釣り上げる",
            "max_progress": 3,
            "items": [{
                "id": "900",
                "amount": 300
            },
            {
                "id": "901",
                "amount": 300
            }]
        },
        "020": {
            "title": "清流の女王",
            "content": "アユを1匹釣り上げる",
            "max_progress": 3,
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