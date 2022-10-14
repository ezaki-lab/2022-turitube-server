import tensorflow as tf
import numpy as np
import copy
import os

def run_inference_single_image(image, inference_func):
    tensor = tf.convert_to_tensor(image)
    output = inference_func(tensor)

    output['num_detections'] = int(output['num_detections'][0])
    output['detection_classes'] = output['detection_classes'][0].numpy()
    output['detection_boxes'] = output['detection_boxes'][0].numpy()
    output['detection_scores'] = output['detection_scores'][0].numpy()
    return output

# 魚種判別をうまくやってくれます
class FishDetectionManager():
    def __init__(self):
        # model_path = os.path.dirname(__file__) + "/saved_model" # 本番モデル(15種分類)
        model_path = os.path.dirname(__file__) + "/demo_model" # デモ用モデル(1種類、真鯛)
        DEFAULT_FUNCTION_KEY = 'serving_default'
        loaded_model = tf.saved_model.load(model_path)
        self.inference_func = loaded_model.signatures[DEFAULT_FUNCTION_KEY]
        self.classes = ["void", "take", "madai", "kasago", "aji", "", "haze", "", "kawahagi", "saba","burakkubasu", "bera", "unagi", "sake", "tanago", "kurodai", "kisu", "buri"]

    def detect(self, image):
        debug_image = copy.deepcopy(image)
        image_width, image_height = image.shape[1], image.shape[0]
        image = image[:, :, [2, 1, 0]]  # BGR2RGB
        image_np_expanded = np.expand_dims(image, axis=0)
        class_id = 0
        score = 0

        output = run_inference_single_image(image_np_expanded, self.inference_func)
        num_detections = output['num_detections']
        min_score = 0.75
        cutout_img = False
        for i in range(num_detections):
            bbox = output['detection_boxes'][i]
            if output['detection_scores'][i] < min_score:
                continue
            score = output['detection_scores'][i]
            class_id = output['detection_classes'][i].astype(np.int)
            min_score = score # スコア上書き(最も高いスコアを参照する)
            x1, y1 = int(bbox[1] * image_width), int(bbox[0] * image_height)
            x2, y2 = int(bbox[3] * image_width), int(bbox[2] * image_height)
            cutout_img = debug_image[y1:y2, x1:x2]
        
        image = image[:, :, [2, 1, 0]]  # RGB2BGR
        return class_id, cutout_img