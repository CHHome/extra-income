<style lang="less" rel="stylesheet/less" scoped>
  @import '../../css/theme';
  .apply-card-container{
    text-align: center;
    a{
      color: #000;
    }
    &:hover{
      -webkit-box-shadow: rgba(71, 83, 108, 0.12) 0 7px 15px 2px;
      box-shadow: rgba(71, 83, 108, 0.12) 0 7px 15px 2px;
    }
    img{
      width: 100%;
      height: 230px;
    }
    .apply-user-info{
      width: 100%;
      height: 100%;
      padding: 8px;
      span{
        display: inline-block;
        font-size: 12px;
        margin: 5px auto;
      }
    }
    .agree{
      .btnTheme
    }
  }
</style>
<template>
  <div class="apply-card-container">
    <router-link
      :to="{name: 'showUserInfo', params: {id: item.userId}}">
      <img alt="chengenhong" :src="baseUrl + 'static/imgs/' + item.headImg">
      <div class="apply-user-info">
        <span>姓名：</span><span>{{item.userName}}</span><br>
        <span>职业：</span><span>{{item.profession}}</span><br>
        <span>phone：</span><span>{{item.phone}}</span><br>
        <span>email：</span><span>{{item.email}}</span>
      </div>
    </router-link>
    <slot name="agree"></slot>
  </div>
</template>
<script>
  import {baseUrl} from '@/config/config'

  export default {
    data () {
      return{
        baseUrl: baseUrl
      }
    },
    props: ['item']
  }
</script>
