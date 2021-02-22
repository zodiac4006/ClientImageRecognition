from PIL import Image, ImageDraw

# 绘制方形
def draw_box(img, bboxes, scores, filename):
    # label = '%.2f' % score
    draw = ImageDraw.Draw(img)
    for bbox in bboxes:
        draw.rectangle([bbox[0], bbox[1], bbox[2], bbox[3]], outline='cyan', width=2)
    img.save(filename)