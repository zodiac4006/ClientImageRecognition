from PIL import Image, ImageDraw

# 绘制方形
def draw_box(img, bboxes, scores, filename):
    # label = '%.2f' % score
    draw = ImageDraw.Draw(img)
    for bbox in bboxes:
        draw.rectangle([bbox[0], bbox[1], bbox[2], bbox[3]], outline='cyan', width=2)
    scale_width = 1440.0 / img.size[0] if img.size[0] > 1440 else 1
    scale_height = 1080.0 / img.size[1] if img.size[1] > 1080 else 1
    scale = min(scale_width, scale_height)
    width = int(img.size[0] * scale)
    height = int(img.size[1] * scale)
    img = img.resize((width, height), Image.ANTIALIAS)
    img.save(filename)