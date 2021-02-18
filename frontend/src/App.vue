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
    font-family: "Open Sans", "Helvetica Neue", helvetica, arial, verdana, sans-serif;
    font-size: 13px;
  }

  .el-header,
  .el-footer {
    background-color: #5fa2dd;
    height: 44px !important;
  }

  .el-main {
    height: 100%;
    margin: 0px;
    padding: 0px;
    display: flex !important;
    background: linear-gradient(90deg,rgba(206,214,224,.32) 1px,transparent 0), linear-gradient(rgba(206,214,224,.32) 1px,transparent 0);
    background-size: 15px 15px;
    background-position: 11px 15px;
    background-color: #fef9f3;
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
