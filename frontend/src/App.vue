<template>
  <el-container>
    <el-header>
      <Header />
    </el-header>
    <el-main>
      <Main class="left" />
      <Explain class="right" />
    </el-main>
  </el-container>
</template>

<script>
  import Header from './components/Header'
  import Main from './components/Main'
  import Explain from './components/Explain'

  export default {
    name: 'App',
    components: {
      Header,
      Main,
      Explain
    }
  }
</script>

<style>
  html,
  body {
    display: block;
    height: 100%;
    margin: 0px;
  }

  .el-header,
  .el-footer {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
  }

  .el-main {
    height: 100%;
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    margin: 0px;
    padding: 0px;
    display: flex;
  }

  body>.el-container {
    margin-bottom: 40px;
    height: 100%;
  }

  .left {
    height: 100%;
    float: left;
    width: 100%;
    flex: 1;
  }

  .right {
    height: 100%;
    float: right;
    width: 320px;
  }
</style>
