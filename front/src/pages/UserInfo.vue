<style scoped>
  .user-info{
    padding-top: 60px;
    text-align: center;
  }

  .user-info > img{
    height: 350px;
    width: 100%;
    margin-bottom: -300px;
  }
  .main-info {
    width:65%;
    margin: 30px auto;
  }
  .main-info > div{
    padding-top: 10%;
    padding-bottom: 10%;
    min-height: 350px;
  }
  .main-info > div:nth-child(1){
    background-color: rgba(3,9,12,0.81);
  }
  .main-info > div:nth-child(2){
    background-color: #fff;
    opacity: 0.9;
    text-align: left;
  }
  .main-info img{
    width:120px;
    height: 150px;
    cursor: pointer;
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
  .userImg:hover:before{
    content: "";
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,.5) url(//static.lagou.com/www/static/account-c/modules/userinfo/img/camera_8d64bc7.png) center center no-repeat;
    cursor: pointer;
  }
  .userImg > input{
    display: none;
  }
  .good-at{
    width:85%;
    background-color: #fff;
    margin: 30px auto;
    padding: 50px 0;
    position: relative;
  }
  .good-at > .good-at-title{
    color: #000;
    text-align: center;
    font-size: 20px;
    font-weight: 500;
  }
  .good-at>i{
    width: 40px;
    height: 5px;
    color: red;
    background-image: linear-gradient(-133deg,#00ffb9,#ACFFEC);
    display: inline-block;
  }
  .good-at-add{
    display: inline-block;
    position: absolute;
    right: 30px;
    line-height: 32px;
    padding: 0 32px;
    border-radius: 16px;
    border:1px solid #00ffb9;
    font-size: 14px;
    font-weight: normal;
    cursor: pointer;
  }
  .good-at-add:hover{
    background-image: linear-gradient(-133deg,#00ffb9,#ACFFEC);
  }
  .user-select{
    width: 60%;
    margin: 0 auto;
  }
  .good-at-box{
    position: relative;
    width: 60%;
    background-color: #f8f9fb;
    margin: 20px auto;
    padding: 10px 30px;
  }
  .box-fade-enter-active, .box-fade-leave-active {
    transition: all 1s ease;
  }
  .box-fade-enter, .box-fade-leave-to{
    opacity: 0;
    transform: translateX(150px);
  }
  .good-at-box > div{
    padding-top: 10px;
    text-align: left;
  }
  .good-at-box header{
    padding-top: 15px;
    padding-bottom: 8px;
    color: #00ffb9;
  }
  .good-at span{
    margin-right: 5px;
    padding: 5px 10px;
    margin-bottom: 3px;
    border-radius: 10px;
    border:1px solid #00ffb9;
    cursor: pointer;
    display: inline-block;
  }
  .selected{
    background-color: #00ffb9;
  }
  .glyphicon-remove{
    color: rgba(0,0,0,0.53);
    padding-left:5px;
    font-weight: 300;
    font-size: 10px;
  }
</style>
<template>
  <div class="user-info">
    <portrait v-if="$store.state.showPortrait"
    :headSrc="reader"
    @confirmHead="confirmHeadPic"></portrait>
    <img v-bind:src="baseUrl+'static/imgs/userInfoBanner.jpg'" alt="">
    <div class="main-info row">
      <div class="col-md-7 ">
        <div class="row">
          <div class="col-md-6 userImg" @click="changePortrait">
            <img v-bind:src="baseUrl+'static/imgs/genhong.jpeg'" alt="更换头像" >
            <input type="file" name="headPic">
          </div>
          <div class="col-md-6 ">
            <label>姓名  </label>
            <input type="text" v-model="mainInfo.username"><br>
            <label>年龄  </label>
            <input type="text"  v-model="mainInfo.age"><br>
            <label>手机  </label>
            <input type="text"  v-model="mainInfo.phone"><br>
            <label >邮箱  </label>
            <input type="text" v-model="mainInfo.email"><br>
          </div>
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
      <div class="good-at-title">
        擅长技能
        <div class="good-at-add" @click="showBox">{{goodAtText}}</div>
      </div>
      <i></i>
      <div class="user-select" @click="remove">
        <span v-for="item in selected">{{item}}<i class="glyphicon glyphicon-remove"></i></span>
      </div>
      <transition name="box-fade">
        <div class="good-at-box" v-show="goodAtBox">
          <div>
            <header>
              开发
            </header>
            <div @click="select">
              <span v-for="item in category.developer">{{item}}</span>
            </div>
          </div>
          <div>
            <header>
              设计
            </header>
            <div @click="select">
              <span v-for="item in category.design">{{item}}</span>
            </div>
          </div>
          <div>
            <header>
              市场/运营
            </header>
            <div @click="select">
              <span v-for="item in category.market">{{item}}</span>
            </div>
          </div>
          <div>
            <header>
              产品
            </header>
            <div @click="select">
              <span v-for="item in category.product">{{item}}</span>
            </div>
          </div>
        </div>
      </transition>
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
  import Portrait from '@/components/Portrait'
  import {category} from '@/js/webData'
  export default {
    mounted () {
      $('.userImg>input').bind('change', () => {
        this.reader.readAsDataURL($('.userImg>input')[0].files[0])
        this.reader.addEventListener("load", () => {
          this.$store.commit('changeSingerState', {stateName: 'curtain', value: true})
          this.$store.commit('changeSingerState', {stateName: 'showPortrait', value: true})
        }, false);
      })
    },
    data () {
      return {
        baseUrl: baseUrl,
        showPortrait: false,
        mainInfo: {},
        reader: new FileReader(),
        goodAtBox: false,
        category: category,
        selected: [],
        goodAtText: '添加'
      }
    },
    methods: {
      getInfo () {
        let store = window.localStorage
        console.log('hahahah')
        this.$http.get(baseUrl + 'userInfoShow', {params: {token: store['token']}})
          .then(res => {
            this.mainInfo = res.data
            this.selected = this.mainInfo.good_at.split(' ')
          }, res => {
            alert('获取数据失败')
          })
      },
      ...mapMutations(['changeSinger']),
      submit () {
        this.mainInfo.good_at = this.selected.join(' ');
        this.mainInfo.token = window.localStorage.token
        this.$http.post(baseUrl + 'userInfoSave', this.mainInfo)
          .then(res => {
            this.getInfo()
          }, res => {
            console.log(res.data)
          })
      },
      changePortrait () {
        $('.userImg>input').click()
      },
      confirmHeadPic (headSrc) {
        this.$store.commit('changeSingerState', {stateName: 'curtain', value: false})
        this.$store.commit('changeSingerState', {stateName: 'showPortrait', value: false})
        $('.userImg>img')[0].src = headSrc.result
        this.mainInfo.headPic = headSrc.result.split(/;base64,/)[1]
      },
      showBox(){
        if (this.goodAtText === '添加') {
          this.goodAtText = '取消'
        } else {
          this.goodAtText = '添加'
        }
        this.goodAtBox = !this.goodAtBox
      },
      select (e) {
        console.log()
        if (e.target.nodeName === 'DIV') {
          return
        }
        if (this.selected.indexOf(e.target.textContent) === -1) {
          this.selected.push(e.target.textContent)
          e.target.classList.add('selected')
        }
      },
      remove (e) {
        if (e.target.nodeName !== 'I') {
          return
        }
        this.selected.splice(this.selected.indexOf(e.target.parentNode.textContent), 1)
      }
    },
    beforeRouteEnter (to, from, next) {
      next(vm => {
        vm.getInfo()
        if (!vm.$store.state.hasLogin) {
          vm.$router.push({name: 'index'})
        }
        window.onscroll = function () {}
        vm.$store.commit('changeSingerState', {stateName: 'myHeader', value: true})
      })
    },
    components: {
      MyProgress,
      Portrait
    }
  }
</script>
