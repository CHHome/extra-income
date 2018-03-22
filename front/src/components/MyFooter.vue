<style lang="less" rel="stylesheet/less" scoped>
  @import '../css/theme.less';
  .my-footer{
    height: 226px;
    margin-top: 30px;
    border-top: 1px solid #e0dfdf;
    background-color: black;
    padding: 15px;
    text-align: center;
    & > div{
      color: #fff;
      text-align: center;
      & > div{
        display: inline-block;
        min-width: 370px;
        & > div{
          margin-bottom: 15px;
          text-align: left;
        }
      }
      span, a {
        color: #fff;
      }
    }
  }
  .row{
    margin: 0;
  }
</style>
<template>
  <div class="my-footer row">
    <div class="col-md-7">
      <div>
        <div>
          网站作者：
          <span>陈根鸿</span>
        </div>
        <div>
          职责：
          <span>前后端同步开发</span>
        </div>
        <div>作者邮箱：
          <span>genhongchan@outlook.com</span>
        </div>
        <div><a href="#">作者简历</a></div>
        <div>
          <span>Tip:</span><br>
          <span>如果你是hr/技术前辈且对网站感兴趣，欢迎通过<a href="genhongchan@outlook.com">邮箱</a>联系我</span>
        </div>
      </div>
    </div>
    <div class="col-md-5">
      <div>
        <div>
          网站主要技术点：<br>
          <span>Vue, bootstrap, less, python, flask, uwsgi, nginx, mysql</span>
        </div>
        <div>
          github：
          <span><a href="https://github.com/CHHome/extra-income">CHHome</a></span>
        </div>
      </div>
    </div>
  </div>
</template>
