<template>
  <div id="main">
    <div class="ctrl-content">
      <div>
        <el-image :src="rimage" v-on:load="rimage_load"></el-image>
      </div>
      <div style='padding-top: 10px;'>
        <el-upload ref="upload" action="https://jsonplaceholder.typicode.com/posts/" :auto-upload="false" accept='image/*'>
          <el-button slot="trigger" size="small" type="primary">上传照片</el-button>
          <div class="el-upload__tip" slot="tip">支持<span class="highlight">jpg/jpeg/png</span>等图片类型文件</div>
        </el-upload>
      </div>
    </div>
    <div class="info-content">
      <div style="clear:unset">
        <el-image :src="oimage"></el-image>
      </div>
      <div id='info-panel'>
        <h3>图像信息</h3>
        <div id='image-info'>
          <div>
            <div>识别人数：<span id='person-num' class='highlight'>9</span>人</div>
            <div>识别用时：<span id='cost-time' class='highlight'>5</span>ms</div>
            <div>图片尺寸：<span id='image-size'>1200*800</span></div>
            <div>图片类型：<span id='image-type'>JPEG</span></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Main',
    data() {
      return {
        rimage: require('./../image/lab.res.jpg'),
        oimage: require('./../image/lab.jpg')
      }
    },
    methods: {
      rimage_load: function(e) {
        var height = e.srcElement.naturalHeight;
        var width = e.srcElement.naturalWidth;

        if (height > width) {
          e.target.style = "height: 500px";
        } else {
          e.target.style = "width: 90%; min-width: 600px;";
        }
      }
    }
  }
</script>

<style>
  #main {
    overflow: auto;
    height: 100%;
    padding: 20px;
    display: flex;
  }

  #main .ctrl-content {
    height: 100%;
    width: 100%;
    min-width: 650px;
    float: left;
    text-align: center;
  }

  #main .ctrl-content .el-image__inner {
    border-radius: 5px;
    border: dashed 2px #e3d3c1;
  }

  #main .info-content {
    height: 100%;
    width: 320px;
    min-width: 320px;
  }

  #main .info-content .el-image__inner {
    border-radius: 5px;
    border: dashed 2px #e3d3c1;
    width: 310px;
  }

  #main span.highlight {
    padding: 0px 2px;
    color: mediumvioletred;
    font-weight: 700;
  }

  #main .el-upload {
    width: 100%;
  }

  #main .el-button {
    width: 90%;
    min-width: 600px
  }

  #main #info-panel {
    margin-top: 10px;
    color: #42719A;
    border: 2px #e3d3c1 solid;
    background-color: rgba(255, 255, 255, 0.5);
    text-align: left;
    width: 310px;
  }

  #main #info-panel h3 {
    padding-left: 10px;
  }

  #main #info-panel #image-info {
    padding-left: 10px;
    padding-bottom: 10px;
  }
</style>
