<template>
  <div id="header" :class="{normal:$store.state.myHeader}">
    <login v-if="showLogin" @next="next"></login>
    <register v-if="showRegister" @next="next"></register>
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
        <div class="user-info" v-show="$store.state.hasLogin">
          <div class="dropdown" @click="infoToggle">
            <img v-bind:src="baseUrl+'static/imgs/genhong.jpeg'" alt="">
            <span>我的外快</span>
            <ul :class="{headerDropdown:$store.state.myHeader}">
              <li>通知</li>
              <li><router-link :to="{name: 'userInfo'}">个人信息</router-link></li>
              <li>我的项目</li>
              <li @click="Cancellation">退出登录</li>
            </ul>
          </div>
        </div>
        <div class="user-opt" v-show="!$store.state.hasLogin">
          <span @click="next('showLogin')">
            登录
          </span>
          <span @click="next('showRegister')">
            注册
          </span>
        </div>
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
  .right > div{
    display: inline;
  }
  .user-info img{
    height: 35px;
    border-radius: 50%;
  }
  .dropdown{
    display: inline-block;
  }
  .dropdown ul{
    position: absolute;
    display: none;
    padding: 0;
    background-color: #fff;
    color: #000;
    min-width: 90px;
    border-radius: 4px;
  }
  .dropdown ul.headerDropdown{
    background-color: #000;
  }
  .dropdown ul.headerDropdown li > a{
    color: #fff;
  }
  .dropdown ul li{
    list-style: none;
    line-height: normal;
    padding: 5px 15px;
  }
  .dropdown ul li > a{
    color: #000;
  }
  header .user-opt > span:nth-child(2){
    margin-right:8px ;
  }
  header .user-opt > span:hover, .left span:hover{
    border-bottom: 2px solid #18f3fa;
    padding-bottom: 8px;
    border-radius: 1px;
  }
  .header-publish{
    margin-right: 32px;
    border:none;
    padding: 8px 32px;
    border-radius: 16px;
    font-size: 14px;
    cursor: pointer;
  }
  .header-publish:hover{
    background-image: linear-gradient(-133deg,#004cfb,#85a1e1);
    opacity: 0.85;
    color: #000;

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
  import {baseUrl} from '@/config/config'
  import Login from '@/components/Login'
  import Register from '@/components/Register'
  import {mapMutations} from 'vuex'
  export default {
    name: 'MyHeader',
    data () {
      return {
        baseUrl: baseUrl,
        showLogin: false,
        showRegister : false
      }
    },
    methods: {
      ...mapMutations(['changeSinger', 'changeSingerState']),
      next (dialogName) {
        this[dialogName] = !this[dialogName]
        this.changeSinger('curtain')
      },
      infoToggle (e) {
//      todo 阻止事件冒泡
        window.event ? window.event.cancelBubble = true : e.stopPropagation()
        let targer = $('.dropdown ul')
        targer.slideToggle(function () {
          document.onclick = function () {
            targer.slideUp()
          }
        })
      },
      Cancellation () {
        window.localStorage.removeItem('token')
        this.changeSingerState({stateName: 'hasLogin', value: false})
      }
    },
    components: {
      Login,
      Register
    }
  }
</script>

