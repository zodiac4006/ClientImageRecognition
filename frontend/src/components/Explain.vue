<template>
  <div id='explain'>
    <h2>系统说明</h2>
    <hr />
    <p>创新实验室——人脸识别POC平台应用于针对图像文件中人员数量信息进行识别。用户可通过点击<span class='highlight'>&nbsp;Browse...&nbsp;</span>按钮进行体验。为保证识别效果，建议使用<span
        class='highlight'>高清晰度正面照片</span>，并尽量<span class='highlight'>避免面部遮挡</span>。</p>
    <p>目前平台尚处于实验阶段，如遇到各类问题或发现任何不足，请通过下方联系方式与我们联系。感谢您的支持与陪伴~</p>
    <img :src='dce' />
    <h2>联系方式</h2>
    <hr />
    <div id='contact'>
      <div>
        <span>联系人：张&nbsp;&nbsp;&nbsp;&nbsp;琦</span><br />
        <span>电&nbsp;&nbsp;&nbsp;&nbsp;话：84807329</span><br />
        <span>邮&nbsp;&nbsp;&nbsp;&nbsp;箱：<a href='mailto:zhangqi01@dce.com.cn'>点击联系</a></span><br />
        <span>微&nbsp;&nbsp;&nbsp;&nbsp;信：</span><br />
        <div class="wx"><img :src="wx_1" /></div>
      </div>
      <div>
        <span>联系人：林瑞涵</span><br />
        <span>电&nbsp;&nbsp;&nbsp;&nbsp;话：84807732</span><br />
        <span>邮&nbsp;&nbsp;&nbsp;&nbsp;箱：<a href='mailto:linruihan@dce.com.cn'>点击联系</a></span><br />
        <span>微&nbsp;&nbsp;&nbsp;&nbsp;信：</span><br />
        <div class="wx"><img :src="wx_2"></div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Explain',
    data() {
      return {
        dce: require('./../image/DCE.jpeg'),
        wx_1: require('./../image/wx_zhangqi.png'),
        wx_2: require('./../image/wx_linruihan.jpeg')
      }
    }
  }
</script>

<style>
  #explain {
    background-color: antiquewhite;
    overflow: auto;
    padding: 0 10px;
    color: #42719A;
    border-left: #e3d3c1 2px solid;
    text-align: left;
  }

  #explain img {
    width: 100%;
  }

  #explain span.highlight {
    color: mediumvioletred;
    font-weight: 700;
  }

  #explain #contact>div {
    width: 50%;
    float: left;
    height: 200px;
  }

  #explain .wx {
    text-align: center;
    margin-top: 5px;
  }

  #explain #contact img {
    width: 90%;
    border: #3B5A82 1px solid;
  }
</style>
