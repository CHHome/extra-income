<style scoped>
  .user-info{
    padding-top: 60px;
  }

  .user-info > img{
    height: 350px;
    width: 100%;
    margin-bottom: -300px;
  }
  .main-info {
    min-width:500px;
    width:65%;
    margin: 30px auto;
    height: 350px;
  }
  .main-info > div{
    height: 100%;
  }
  .main-info > div:nth-child(1){
    background-color: rgba(3,9,12,0.81);
  }
  .main-info > div:nth-child(2){
    background-color: #fff;
    opacity: 0.9;
  }
  .main-info img{
    margin-top: 60px;
    margin-left: 30px;
    width:120px;
    height: 150px;
  }
  .first-info{
    min-width: 320px;
    margin-left: 165px;

  }
  label{
    margin-right: 8px;
  }
  label, input{
    margin-top: 10px;
    color: #fff;
  }
  input{
    border: none;
    border-bottom: 1px solid #fff;
    background-color: transparent;
    border-radius: 4px;
    outline:none;
  }
  .about-expert{
    width: 90%;
    margin: 0  auto;
    font-weight: 600;
    font-size: 13px;
    color: #000;
  }
  .about-expert input{
    border-bottom:1px solid #000;
  }
  .about-expert label{
    color: #000;
  }
  .submit-banner{
    width: 65%;
    margin: 30px auto;
  }
  .submit-banner span{
    border-style: none;
    line-height: 32px;
    padding: 0 32px;
    background-image: linear-gradient(-133deg,#00ffb9,#ACFFEC);
    border-radius: 16px;
    font-family: PingFangSC-Regular;
    font-size: 14px;
    color: #000;
    letter-spacing: 0;
    display: inline-block;
    cursor: pointer;
    margin-right: 10px;
   }
</style>
<template>
  <div class="user-info">
    <form :action="baseUrl" method="post" id="userInfo"></form>
    <img v-bind:src="baseUrl+'static/imgs/userInfoBanner.jpg'" alt="">
    <div class="main-info row">
      <div class="col-md-7">
        <img v-bind:src="baseUrl+'static/imgs/genhong.jpeg'" alt="">
        <div class="first-info">
          <label for="username">姓名  </label>
          <input type="text" id="username" name="username" form="userInfo"><br>
          <label for="age">年龄  </label>
          <input type="text" id="age" name="age" form="userInfo"><br>
          <label for="goodat">特长  </label>
          <input type="text" id="goodat" name="goodat" form="userInfo"><br>
        </div>
      </div>
      <div class="col-md-5">
        <my-progress></my-progress>
        <div class="about-expert">
          <label for="price" >报价</label>
          <input type="text" id="price" name="priice" placeholder="800" form="userInfo"><br/>
          <label>成交量</label>
          <span>0</span>
        </div>
      </div>
    </div>
    <div class="good-at">

    </div>
    <div class="projects">

    </div>
    <div class="submit-banner">
      <span>保存</span>
      <span>预览</span>
    </div>
  </div>
</template>
<script>
  import {baseUrl} from '@/config/config'
  import MyProgress from '@/components/share/MyProgress'
  import {mapMutations} from 'vuex'
  export default {
    data () {
      return {
        baseUrl: baseUrl
      }
    },
    methods: {
      ...mapMutations(['changeSinger'])
    },
    beforeRouteEnter (to, from, next) {
      next(vm => {
        console.log('sss')
        window.onscroll = function () {}
        vm.$store.commit('changeMyHeader', true)
      })
    },
    components: {
      MyProgress
    }
  }
</script>
