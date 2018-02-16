<style lang="less" rel="stylesheet/less" scoped>
  @import '../../css/theme';
  .apply-card{
    padding-bottom: 10px;
    border: 1px solid #ccc;
    position: relative;
    cursor: pointer;
    margin-top: 20px;
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
  <div class="col-md-3 col-sm-4 apply-card">
    <router-link
      :to="{name: 'showUserInfo', params: {id: item.id}}">
      <img alt="chengenhong" :src="baseUrl + 'static/imgs/' + item.headImg">
      <div class="apply-user-info">
        <span>职业：</span><span>{{item.profession}}</span><br>
        <span>phone：</span><span>{{item.phone}}</span><br>
        <span>email：</span><span>{{item.email}}</span>
      </div>
    </router-link>
    <span class="agree" @click="agree">同意申请</span>
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
    props: ['item'],
    methods: {
      agree (e) {
        console.log('dsffs')
      }
    }
  }
</script>
