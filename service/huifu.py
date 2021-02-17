# This code is written at BigVision LLC. It is based on the OpenCV project. It is subject to the license terms in the LICENSE file found in this distribution and at http://opencv.org/license.html

# Usage example:  python3 object_detection_yolo.py --video=run.mp4
#                 python3 object_detection_yolo.py --image=bird.jpg

import cv2 as cv
import sys
from sys import stderr
import numpy as np
import os.path

def person_overlap(b1, b2):
    '''
    left, top, width, height
    '''
    # TODO
    return 0.5

class PersonCounter:
    def __init__(self, classes_f, configure_f, weight_f, score_thres=0.5, nms_thres=0.4):
        '''
        init
        '''
        # classes
        self.classes = None
        with open(classes_f, 'rt') as f:
            self.classes = f.read().rstrip('\n').split('\n')
    
        # network
        self.net = cv.dnn.readNetFromDarknet(configure_f, weight_f)
        self.net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
        self.net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU) 
        
        # parameters
        self.score_thres = score_thres  # Confidence threshold
        self.nms_thres = nms_thres      # Non-maximum suppression threshold置信度阈值
        self.width = 608       # Width of network's input image，改为320*320更快
        self.height = 608      # Height of network's input image，改为608*608更准

    def count_image_person(self, image_file):
        """
        计算 image_file 中的人数, 将识别结果保存到 <image_file>.res.jpg
    
        return  人数, info
        """
        if not os.path.isfile(image_file):
            stderr.write('Input image file %s not exists!\n' % image_file)
            return -1, ''

        output_f = image_file + '.res.jpg'
        cap = cv.VideoCapture(image_file)
        has_frame, frame = cap.read()
        if not has_frame:
            stderr.write('No frame!\n')
            return -2, ''

        blob = cv.dnn.blobFromImage(frame, 1/255.0, (self.width, self.height), [0,0,0], 1, crop=False)
        self.net.setInput(blob)
        outs = self.net.forward(self.get_output_names())
        pcnt = self.postprocess(frame, outs)

        t, _ = self.net.getPerfProfile()
        label = '%.2f' % (t * 1000.0 / cv.getTickFrequency())

        cv.imwrite(output_f, frame.astype(np.uint8))

        return pcnt, label

    def get_output_names(self):
        '''
        Get the names of the output layers
        '''
        layers_names = self.net.getLayerNames()
        return [layers_names[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]

    def draw_pred(self, frame, cls_id, score, left, top, right, bottom):
        '''
        Draw the predicted bounding box
        '''
        label = '%.2f' % score

        # draw bounding box
        cv.rectangle(frame, (left, top), (right, bottom), (255, 178, 50), 2)

        # draw label
        label_size, baseline = cv.getTextSize(label, cv.FONT_HERSHEY_SIMPLEX, 0.5, 1)
        top = max(top, label_size[1])
        cv.rectangle(frame, (left, top - round(label_size[1])), (left + round(label_size[0]), top + baseline), (255, 178, 50), cv.FILLED)
        cv.putText(frame, label, (left, top), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1)

    def postprocess(self, frame, outs):
        '''
        Remove the bounding boxes with low confidence using non-maxima suppression

        return  count of person
        '''
        frame_h, frame_w = frame.shape[0], frame.shape[1]
        cls_ids, scores, boxes = [], [], []
        # Scan through all the bounding boxes output from the network and 
        # keep only the ones with high confidence scores. Assign the box's 
        # class label as the class with the highest score.
        for out in outs:
            for detection in out:
                ss = detection[5:]
                cls_id = np.argmax(ss)
                score = ss[cls_id]
                if score > self.score_thres:
                    center_x, center_y = int(detection[0]*frame_w), int(detection[1]*frame_h)
                    width, height = int(detection[2]*frame_w), int(detection[3]*frame_h)
                    left, top = int(center_x - width/2), int(center_y - height/2)
                    cls_ids.append(cls_id)
                    scores.append(float(score))
                    boxes.append([left, top, width, height])

        # Perform non maximum suppression to eliminate redundant overlapping boxes 
        # with lower confidences
        indices = cv.dnn.NMSBoxes(boxes, scores, self.score_thres, self.nms_thres)
        #indices = nms.boxes(boxes, scores, {'score_threshold':0.0, 'nms_threshold':0.8, 'compare_function':person_overlap})
        person_cnt = 0

        for i in indices:
            i = i[0]
            box = boxes[i]
            left, top, width, height = box[0], box[1], box[2], box[3]

            # 不是person的 不要
            if self.classes[cls_ids[i]] != 'person':
                continue

            # 宽度超过图像宽度一半的 不要
            if width*2 >= frame_w:
                continue

            person_cnt += 1

            self.draw_pred(frame, cls_ids[i], scores[i], left, top, left+width, top+height)

        return person_cnt

def recognition(configure_f, weight_f, classes_f, image_f):
    # configure_f = './model/yolov3-spp.cfg'
    # weight_f = './model/yolov3-spp.weights'
    # classes_f = './model/coco.names'

    pcounter = PersonCounter(classes_f, configure_f, weight_f, score_thres=0.0)
    n, msg = pcounter.count_image_person(image_f)
    stderr.write('%d\n%s\n' % (n, msg))
    return n, msg

if __name__ == '__main__':
    if len(sys.argv) != 5:
        stderr.write('\npython3 %s <model_configure> <model_weight> <classes> <image>\n\n' % sys.argv[0])
        sys.exit()

    configure_f, weight_f, classes_f, image_f = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    pcounter = PersonCounter(classes_f, configure_f, weight_f, score_thres=0.0)

    n, msg = pcounter.count_image_person(image_f)
    stderr.write('%d\n%s\n' % (n, msg))

