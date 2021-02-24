import tensorflow as tf
from PIL import Image, ImageDraw
import numpy as np
import os
import time
import utils
current_path = os.path.dirname(__file__)
import sys
sys.path.append(current_path)
import person_nms


class EfficientdetModel():
    def __init__(self, model_dir=current_path + '/model/efficientdet-d0-lab', score_thres=0.5):
        self.export_model = tf.saved_model.load(model_dir)
        self.score_thres = score_thres

    def recognition(self, image_path):
        start_time = time.time()
        img = Image.open(image_path)
        imgs = [np.array(img)]
        imgs = tf.convert_to_tensor(np.asarray(imgs), dtype=tf.uint8)
        boxes, scores, classes, valid_len = self.export_model.f(imgs)

        # people_nms
        # Visualize results.
        length = valid_len[0]

        person_id = 1
        b = boxes[0].numpy()[:length]
        c = classes[0].numpy().astype(np.int)[:length]
        s = scores[0].numpy()[:length]
        fltr = c == person_id
        nms_b, nms_c, nms_s = person_nms.person_nms(b[fltr], c[fltr], s[fltr], 0.7)

        bboxes = []

        for i in range(len(nms_b)):
            if nms_s[i] > self.score_thres:
                bboxes.append([nms_b[i][1], nms_b[i][0], nms_b[i][3], nms_b[i][2]])
        scores = scores.cpu().numpy().astype('float32')[0]
        utils.draw_box(img, bboxes, scores, image_path + '.eff.jpg')

        end_time = time.time()
        time_cost = '%.2f' % ((end_time - start_time) * 1000)
        return (len(bboxes), time_cost)

if __name__ == '__main__':
    model = EfficientdetModel('/root/automl/tmp/efficientdet-d0-lab')
    model.recognition('/root/automl/tmp/5.jpg')
