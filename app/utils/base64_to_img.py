import base64
import numpy as np
import cv2

def base64_to_img(img_base64):
    img_binary = base64.b64decode(img_base64.split(",")[1])
    png = np.frombuffer(img_binary, dtype=np.uint8)
    img = cv2.imdecode(png, cv2.IMREAD_ANYCOLOR)
    return img