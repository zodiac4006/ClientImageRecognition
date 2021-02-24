from flask import Flask, render_template, request
import os
from flask_cors import *
from flask import jsonify
from PIL import Image
import time

from model.efficientdet.model import EfficientdetModel

app = Flask(__name__)
CORS(app, supports_credentials=True, resources=r'/*')
# app.config['UPLOAD_FOLDER'] = '/Users/linruihan/Documents/HBuilderProjects/ClientImageRecognition/frontend/static/upload'
app.config['UPLOAD_FOLDER'] = '/usr/local/webserver/nginx/html/static/upload'

# 模型加载
efficientdetModel = EfficientdetModel(score_thres=0.17)

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
   if request.method == 'POST':
      f = request.files['image']
      filename = str(abs(hash(time.time())))
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      image_f = os.path.join(app.config['UPLOAD_FOLDER'], filename)

      ### 调用
      num, cost = efficientdetModel.recognition(image_f)

      im = Image.open(image_f)  # 返回一个Image对象

      response =jsonify({"success": 200,
                         "num": num,
                         "cost": cost,
                         "filename": filename,
                         "nfilename": filename + '.eff.jpg',
                         "size": str(im.size[0]) + '*' + str(im.size[1]),
                         "type": im.format})
      response.headers['Access-Control-Allow-Origin'] = '*'

      return response

if __name__ == '__main__':
   app.run('0.0.0.0', '4707')