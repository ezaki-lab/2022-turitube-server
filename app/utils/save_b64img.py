import base64
import numpy as np 
import io
import os

folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../static/img/')

def save_b64img(base64img, savepath, img_name):
    img_binary = base64.b64decode(base64img.split(",")[1])
    with open(folder_path + savepath + img_name, "wb") as f:
        f.write(img_binary)
