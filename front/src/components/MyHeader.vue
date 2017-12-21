<template>
  <div id="header" :class="{normal:$store.state.myHeader}">
    <header>
      <div class="left">
        <span>外快网</span>
        <router-link :to="{name:'index'}">
          <span>首页</span>
        </router-link>
        <router-link :to="{name:'projects'}">
          <span>我的项目</span>
        </router-link>
        <span>服务指南</span>
      </div>
      <div class="right">
        <span class="header-publish">发布项目</span>
        <span @click="next('showLogin')" class="user-opt">
          登录
        </span>
        <span @click="next('showRegister')" class="user-opt">
          注册
        </span>
      </div>
    </header>
  </div>
</template>
<style scoped>
  a{
    color: #fff;
    text-decoration: none;
  }
  #header{
    position: fixed;
    width:100%;
    z-index: 9999;
  }
  header{
    width: 95%;
    margin: 0 auto;
    height: 60px;
    line-height: 60px;
    color: #fff;
  }
  header .user-opt:nth-child(2){
    margin-right:8px ;
  }
  header .user-opt:hover, .left span:hover{
    border-bottom: 2px solid #ff4c81;
    padding-bottom: 8px;
    border-radius: 1px;
  }
  .header-publish{
    margin-right: 32px;
    border:none;
    padding: 8px 32px;
    border-radius: 16px;
    font-family: PingFangSC-Regular;
    font-size: 14px;
    color: #fff;
    letter-spacing: 0;
    cursor: pointer;
  }
  .header-publish:hover{
    background-color: #ff4c81;
    opacity: 0.85;

  }
  .right{
    float: right;
    cursor: pointer;
  }
  .left{
    float: left;
    font-size: 18px;
    cursor: pointer;
  }
  .left span{
    margin-right: 18px;
  }
  .left > span:nth-child(1){
    margin-right: 65px;
    text-decoration: none;
    color: #fff;
  }
  .normal{
    background-color: black;
  }

</style>
<script>
  import {mapMutations} from 'vuex'
  export default {
    name: 'MyHeader',
    data () {
      return {}
    },
    methods: {
      ...mapMutations(['changeSinger']),
      next (dialogName) {
        this.changeSinger(dialogName)
        this.changeSinger('curtain')
      }
    }
  }
</script>

