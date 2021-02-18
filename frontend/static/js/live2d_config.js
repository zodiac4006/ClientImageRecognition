L2Dwidget.init({
  "model": {
    jsonPath: "static/model/shizuku/shizuku.model.json",
    "scale": 1
  },
  "display": {
    superSample: 1.6, //大小
    "position": "right",
    "width": 110,
    "height": 210,
    "hOffset": 350,
    "vOffset": 0
  },
  "mobile": {
    "show": true,
    "scale": 0.5
  },
  "react": {
    "opacityDefault": 0.8,
    "opacityOnHover": 0.1
  }
});
