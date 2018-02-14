<style lang="less" rel="stylesheet/less" scoped>
  @import '../css/theme.less';
  a{
    text-decoration: none;
    color: #fff;
  }
  #header{
    position: fixed;
    width:100%;
    z-index: 9999;
    color: #fff;
    & > header{
      width: 95%;
      margin: 0 auto;
      height: 60px;
      line-height: 60px;
      /*左边*/
      & > div:nth-child(1){
        float: left;
        font-size: 18px;
        cursor: pointer;
        & span{
          margin-right: 18px;
          &:hover:extend(.span-hover){}
        }
        & > span:nth-child(1){
          margin-right: 65px;
          text-decoration: none;
        }
      }
      /*右边*/
      & > div:nth-child(2){
        float: right;
        cursor: pointer;
        .header-publish{
          .btnTheme;
          margin-right: 50px;
        }
        & > div{
          display: inline;
        }
        & > .user-info{
          img{
            width: 36px;
            border-radius: 50%;
          }
        }
        & > .user-opt{
          & > span{
            margin-right:8px ;
          }
          & > span:hover:extend(.span-hover){}
        }
      }
    }
  }
  .span-hover{
    border-bottom: 2px solid @secondColor;
    padding-bottom: 8px;
    border-radius: 1px;
  }
  .dropdown{
    display: inline-block;
    & > ul{
      position: absolute;
      display: none;
      padding: 0;
      background-color: #fff;
      color: #000;
      min-width: 90px;
      border-radius: 4px;
      & li{
        list-style: none;
        line-height: normal;
        padding: 5px 15px;
        & > a{
          color: #000;
        }
      }
    }
  }
  .headerDropdown{
    background-color: #000;
  }
  .headerDropdown li > a{
    color: #fff;
  }
  .normal{
    color: @fontColor;
    background-color: @baseColor;
    border-bottom: 1px solid #e0dfdf;
    a, span{
      color: @fontColor;
    }
  }
</style>
<template>
  <div id="header" :class="{normal:$store.state.myHeader}">
    <login v-if="showLogin" @next="next"></login>
    <register v-if="showRegister" @next="next"></register>
    <header>
      <div>
        <span>外快网</span>
        <router-link :to="{name:'index'}">
          <span>首页</span>
        </router-link>
        <router-link :to="{name:'projects'}">
          <span>我的项目</span>
        </router-link>
        <span>服务指南</span>
      </div>
      <div>
        <router-link :to="{name: 'releasePro'}">
          <span class="header-publish">发布项目</span>
        </router-link>
        <div class="user-info" v-show="$store.state.hasLogin">
          <div class="dropdown" @click="infoToggle">
            <img v-bind:src="baseUrl+ 'static/imgs/' + $store.state.headPic" alt="">
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
        this.$store.commit('changeLoginId', null)
        this.changeSingerState({stateName: 'hasLogin', value: false})
        this.$store.commit('changeHead', 'default_head.jpg')
      }
    },
    components: {
      Login,
      Register
    }
  }
</script>

