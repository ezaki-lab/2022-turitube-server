import base64
import numpy as np
import cv2

def img_to_base64(dst):
    result, dst_data = cv2.imencode('.jpg', dst)
    dst_base64 = base64.b64encode(dst_data)

    return dst_base64