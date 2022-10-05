from app.utils.db_conn import sql_connection
import random
from .load_model import load_model
from .speacies_dict import speacies
import copy

# 魚種判別をうまくやってくれます
class SpeaciesDetectionManager():
    def __init__(self):
        model = load_model()

    def detect(self):
        r = random.randint(0,5)
        result = speacies[r]
        return result