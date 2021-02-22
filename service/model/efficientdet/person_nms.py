'''
person nms

zhangqi01
'''
from sys import stderr

def iou(ymn1, xmn1, ymx1, xmx1, ymn2, xmn2, ymx2, xmx2):
    ymn, xmn, ymx, xmx = max(ymn1, ymn2), max(xmn1, xmn2), min(ymx1, ymx2), min(xmx1, xmx2)
    w, h = xmx - xmn + 1, ymx - ymn + 1
    w1, h1 = xmx1 - xmn1 + 1, ymx1 - ymn1 + 1
    w2, h2 = xmx2 - xmn2 + 1, ymx2 - ymn2 + 1
    ai, a1, a2 = w*h, w1*h1, w2*h2
    return ai / (a1 + a2 - ai)


def person_overlap_score(b1, b2):
    '''
    Params
        b1: [ymin, xmin, ymax, xmax]
        b2: [ymin, xmin, ymax, xmax]

    Return
        score
    '''
    if b1[0]>=b2[2] or b1[2]<=b2[0] or b1[1]>=b2[3] or b1[3]<=b2[1]:
        return 0.0

    mx_xmn, mn_xmx, mn_ymx = max(b1[1], b2[1]), min(b1[3], b2[3]), min(b1[2], b2[2])
    
    s = iou(b1[0], mx_xmn, b1[2], b1[3], b2[0], mx_xmn, b2[2], b2[3])
    s = max(s, iou(b1[0], b1[1], b1[2], mn_xmx, b2[0], b2[1], b2[2], mn_xmx))
    s = max(s, iou(b1[0], b1[1], mn_ymx, b1[3], b2[0], b2[1], mn_ymx, b2[3]))
    
    return s

def person_nms(boxes, classes, scores, nms_thres):
    '''
    Params
        boxes: a box prediction with shape [N, 4] ordered [ymin, xmin, ymax, xmax].
        classes: a class prediction with shape [N].
        scores: a sorted list of float value with shape [N].
        nms_thres: nms threshold
    
    Returns  
        nms_boxes, nms_classes, nms_scores
    '''
    stderr.write('PNMS len=%d\n' % (len(boxes)))
    keep, N = [True], len(boxes)
    for j in range(1, N):
        keep.append(True)
        for i in range(j):
            if not keep[i]:
                continue
            if person_overlap_score(boxes[i], boxes[j]) >= nms_thres:
                keep[j] = False
                stderr.write('PNMS b[%d]=%s, b[%d]=%s\n' % (i, boxes[i], j, boxes[j]))
                break
    stderr.write('PNMS len=%d\n' % (len(boxes[keep])))
    return boxes[keep], classes[keep], scores[keep]
