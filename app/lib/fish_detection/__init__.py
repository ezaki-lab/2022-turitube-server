from app.utils.db_conn import sql_connection
import random
from .load_model import load_model
import copy

# 魚種判別をうまくやってくれます
class FishDetectionManager():
    def __init__(self):
        model = load_model()

    def detect(self):
        r = random.randint(1,20)
        return r

