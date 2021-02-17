from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from flask_cors import *
from flask import jsonify
import huifu as hf
from PIL import Image

app = Flask(__name__)
CORS(app, supports_credentials=True, resources=r'/*')
app.config['UPLOAD_FOLDER'] = '/Users/linruihan/Documents/HBuilderProjects/ClientImageRecognition/frontend/static/upload'
app.config['MODEL_FOLDER'] = '/Users/linruihan/Documents/HBuilderProjects/ClientImageRecognition/service/model'

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
   if request.method == 'POST':
      f = request.files['image']
      filename = str(abs(hash(f.filename)))
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      configure_f = os.path.join(app.config['MODEL_FOLDER'], 'yolov3-spp.cfg')
      weight_f = os.path.join(app.config['MODEL_FOLDER'], 'yolov3-spp.weights')
      classes_f = os.path.join(app.config['MODEL_FOLDER'], 'coco.names')
      image_f = os.path.join(app.config['UPLOAD_FOLDER'], filename)
      num, cost = hf.recognition(configure_f, weight_f, classes_f, image_f)

      im = Image.open(image_f)  # 返回一个Image对象

      response =jsonify({"success": 200,
                         "num": num,
                         "cost": cost,
                         "filename": filename,
                         "nfilename": filename + '.res.jpg',
                         "size": str(im.size[0]) + '*' + str(im.size[1]),
                         "type": im.format})
      response.headers['Access-Control-Allow-Origin'] = '*'

      return response

if __name__ == '__main__':
   app.run('0.0.0.0', '4707')