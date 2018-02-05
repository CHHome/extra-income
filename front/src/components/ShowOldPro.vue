<style lang="less" rel="stylesheet/less" scoped>
  @import '../css/theme.less';
  .show-pro{
    position: relative;
    width: 60%;
    margin: 20px auto;
    background-color: #fff;
    min-width: 280px;
    padding: 10px;
    clear: both;
    img{
      width:100%;
    }
    .show-pro-info{
      text-align: left;
      .show-pro-info-title{
        font-weight: 600;
        font-size: 16px;
      }
      & > div, & > p{
        margin-top: 20px;
      }
      .show-pro-info-opt{
        float: right;
        margin-right: 30px;
        i{
          margin-left: 15px;
          color: @secondColor;
          cursor: pointer;
        }
      }
      a{
        text-decoration: none;
        color: black;
      }
    }
  }
</style>

<template>
  <div class="show-pro">
    <img :src="item.head_img" v-if="item.head_img.indexOf('base64,') != -1" alt="">
    <img :src="baseUrl+'static/imgs/project/default_pro.jpg'" v-else-if="item.head_img == ''"/>
    <img :src="baseUrl+'static/imgs/'+item.head_img" v-else/>
    <div class="show-pro-info">
      <div class="show-pro-info-title">
        <span>{{item.proName}}</span>
        <span> / </span>
        <span>{{item.player}}</span>
      </div>
      <p>
        {{item.describe}}
      </p>
      <div>
        <a :href="item.linkTo">作品链接</a>
        <div class="show-pro-info-opt">
          <i class="glyphicon glyphicon-pencil"></i>
          <i class="glyphicon glyphicon-calendar"></i>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  import {baseUrl} from '@/config/config'
  export default{
    props: ['item'],
    data () {
      return{
        baseUrl: baseUrl
      }
    }
  }
</script>
