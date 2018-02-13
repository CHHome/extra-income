<style lang="less" rel="stylesheet/less" scoped>
  @import '../../css/theme.less';
  .project-card{
    color: #000;
    margin-top: 20px;
    .up-banner{
      background-image: url("../../assets/recommendPro.jpg");
      height: 120px;
      display: flex;
      justify-content: center;
      align-items: center;
      & > i{
        color: #fff;
        font-size: 30px;
      }
    }
    .recommend-pro-container {
      border: 1px solid #e5e8ef;
      text-align: center;
      padding-bottom: 20px;
      header {
        font-size: 16px;
        font-weight: 600;
        margin-top: 30px;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
        word-wrap: normal;
        margin-bottom: 15px;
      }
      & > i {
        color: #ff734b;
      }
      .container-second-title {
        width: 50%;
        border-radius: 16px;
        border: 1px solid @secondColor;
        padding: 6px 8px;
        box-sizing: border-box;
        margin-top: 15px;
        display: inline-block;
      }
      .container-info {
        margin-top: 20px;
        & > div {
          display: inline-block;
          padding: 10px 12px;
          border-right: 1px dotted #d9d9d9;
          &:nth-last-child(1) {
            border-right: none;
          }
        }
      }
    }
  }

</style>

<template>
  <div class="col-md-3 col-sm-4 project-card">
    <div class="up-banner">
      <i class="glyphicon glyphicon-pushpin"></i>
    </div>
    <div class="recommend-pro-container">
      <header>{{item.projectName}}</header>
      <i>{{item.budget}}元</i><br>
      <span class="container-second-title">{{item.secondType}}</span>
      <div class="container-info">
        <div>
          <i>申请数</i><br>
          <span>{{item.applyAmount}}</span>
        </div>
        <div>
          <i>浏览数</i><br>
          <span>{{item.browse}}</span>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  export default {
    props: ['item']
  }
</script>
