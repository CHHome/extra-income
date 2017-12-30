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
    margin-top: 80px;
    margin-left: 30px;
    float: left;
    width:120px;
    height: 150px;
  }
  .first-info{
    float: right;
    margin-top: 80px;
    margin-right: 30px;
  }
  label{
    color: #fff;
    margin-right: 8px;
    margin-top: 10px;
  }
  label:nth-child(1){
    margin-top: 0;
  }
  input{
    color: #fff;
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
  .about-expert label, .about-expert input{
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
    <img v-bind:src="baseUrl+'static/imgs/userInfoBanner.jpg'" alt="">
    <div class="main-info row">
      <div class="col-md-7">
        <img v-bind:src="baseUrl+'static/imgs/genhong.jpeg'" alt="">
        <div class="first-info">
          <label>姓名  </label>
          <input type="text" v-model="mainInfo.username"><br>
          <label>年龄  </label>
          <input type="text"  v-model="mainInfo.age"><br>
          <label >特长  </label>
          <input type="text" v-model="mainInfo.good_at"><br>
          <label>手机  </label>
          <input type="text"  v-model="mainInfo.phone"><br>
          <label >邮箱  </label>
          <input type="text" v-model="mainInfo.email"><br>
        </div>
      </div>
      <div class="col-md-5">
        <my-progress
          :on_time="mainInfo.on_time"
          :credit="mainInfo.credit"
          :quality="mainInfo.quality"
        ></my-progress>
        <div class="about-expert">
          <label >报价</label>
          <input type="text" placeholder="800" v-model="mainInfo.price"><br/>
          <label>成交量</label>
          <span>{{mainInfo.has_finish}}</span>
        </div>
      </div>
    </div>
    <div class="good-at">

    </div>
    <div class="projects">

    </div>
    <div class="submit-banner">
      <span @click="submit">保存</span>
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
        baseUrl: baseUrl,
        mainInfo: {}
      }
    },
    created(){
      this.getInfo()
    },
    methods: {
      getInfo(){
        let store = window.localStorage
        console.log(store['token'])
        this.$http.get(baseUrl+'userInfoShow', {params:{token: store['token']}})
          .then(res => {
            this.mainInfo = res.data
          }, res => {
            alert('获取数据失败')
          })
      },
      ...mapMutations(['changeSinger']),
      submit () {
        this.mainInfo.token = window.localStorage.token
        console.log(this.mainInfo)
        this.$http.post(baseUrl+'userInfoSave',this.mainInfo)
          .then(res => {
            this.getInfo()
          },res => {
            console.log(res.data)
          })
      }
    },
    beforeRouteEnter (to, from, next) {
      next(vm => {
        window.onscroll = function () {}
        vm.$store.commit('changeMyHeader', true)
      })
    },
    components: {
      MyProgress
    }
  }
</script>
