<style lang="less" rel="stylesheet/less" scoped>
  @import '../css/theme.less';
  .user-info{
    padding-top: 60px;
    text-align: center;
    & > div{
      margin: auto;
      margin-bottom: 60px;
    }
    & > img{
      height: 350px;
      width: 100%;
      margin-bottom: -250px;
    }
    .main-info {
      width:65%;
      margin: 30px auto;
      .userImg{
        &:hover{
          &:before{
            content: "";
            position: absolute;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,.5) url(//static.lagou.com/www/static/account-c/modules/userinfo/img/camera_8d64bc7.png) center center no-repeat;
            cursor: pointer;
          }
        }
        & > input{
          display: none;
        }
      }
      img{
        width:120px;
        height: 150px;
        cursor: pointer;
      }
      & > div{
        padding-top: 10%;
        padding-bottom: 10%;
        min-height: 350px;
      }
      & > div:nth-child(1){
        background-color: rgba(3,9,12,0.81);
      }
      & > div:nth-child(2){
        background-color: #fff;
        opacity: 0.9;
        text-align: left;
      }
      .justChange{
        width:90%;
        margin: 0 auto;
      }
      .about-expert{
        width: 90%;
        margin: 0  auto;
        font-weight: 600;
        font-size: 13px;
        color: #000;
        input{
          border-bottom:1px solid #000;
        }
        label, input{
          color: #000;
        }
      }
    }
     .goodAt-pro(){
      width:85%;
      min-width: 300px;
      background-color: #fff;
      margin: 30px auto;
      padding: 50px 10px;
      position: relative;
       .title{
         color: #000;
         text-align: center;
         font-size: 20px;
         font-weight: 500;
       }
       & > div> i{
         width: 40px;
         height: 5px;
         background-image: linear-gradient(-133deg,#00ffb9,#ACFFEC);
         display: inline-block;
       }
       & > .add-box{
         position: relative;
         width: 60%;
         background-color: #f8f9fb;
         margin: 20px auto;
         min-width: 280px;
         padding: 10px;
         clear: both;
       }
    }
    .good-at{
      .goodAt-pro;
      span{
        margin-right: 5px;
        padding: 5px 10px;
        margin-bottom: 3px;
        border-radius: 10px;
        border:1px solid #00ffb9;
        cursor: pointer;
        display: inline-block;
      }
      .user-select{
        width: 60%;
        margin: 30px auto;
      }
      & > div:nth-last-child(1){
        & > div{
          padding-top: 10px;
          text-align: left;
        }
        header{
          padding-top: 15px;
          padding-bottom: 8px;
          color: #00ffb9;
        }
      }
    }
    .project{
      .goodAt-pro;
    }
  }
  label{
    color: #fff;
    margin-right: 8px;
    margin-top: 10px;
    &:nth-child(1){
      margin-top: 0;
    }
  }
  input{
    color: #fff;
    border: none;
    border-bottom: 1px solid #fff;
    background-color: transparent;
    border-radius: 4px;
    outline:none;
  }
  .submit-banner{
    width: 65%;
    margin: 30px auto;
    span{
      .btnTheme
    }
  }
  .add{
    float: right;
    margin-right: 30px;
    line-height: 32px;
    padding: 0 32px;
    border-radius: 16px;
    border:1px solid #00ffb9;
    font-size: 14px;
    font-weight: normal;
    cursor: pointer;
  }
  .add:hover{
    background-image: linear-gradient(-133deg,#00ffb9,#ACFFEC);
  }
  .box-fade-enter-active, .box-fade-leave-active {
    transition: all 1s ease;
  }
  .box-fade-enter, .box-fade-leave-to{
    opacity: 0;
    transform: translateX(150px);
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
    <portrait v-if="showPortrait"
    :headSrc="reader"
    @next="next"
    @confirmHead="confirmHeadPic"></portrait>
    <img v-bind:src="baseUrl+'static/imgs/userInfoBanner.jpg'" alt="">
    <div class="main-info row">
      <div class="col-md-7 ">
        <div class="row">
          <div class="col-md-6 userImg" @click="changePortrait">
            <img v-bind:src="baseUrl+'static/imgs/'+mainInfo.headImg" alt="更换头像" >
            <input type="file" name="headPic">
          </div>
          <div class="col-md-6 ">
            <label>姓名  </label>
            <input type="text" v-model="mainInfo.userName"><br>
            <label>职业  </label>
            <input type="text" v-model="mainInfo.profession"><br>
            <label>年龄  </label>
            <input type="text"  v-model="mainInfo.age"><br>
            <label>手机  </label>
            <input type="text"  v-model="mainInfo.phone"><br>
            <label >邮箱  </label>
            <input type="text" v-model="mainInfo.email"><br>
            <label>简介  </label>
            <input type="text" v-model="mainInfo.synopsis"><br>
          </div>
        </div>
      </div>
      <div class="col-md-5">
        <div class="justChange">
          <my-progress
            :value="mainInfo.onTime"
            :label="'准时率'"
          ></my-progress>
          <my-progress
            :value="mainInfo.credit"
            :label="'信任度'"
          ></my-progress>
          <my-progress
            :value="mainInfo.quality"
            :label="'优质比'"
          ></my-progress>
        </div>
        <div class="about-expert">
          <label >报价</label>
          <input type="text" placeholder="800" v-model="mainInfo.price"><br/>
          <label>成交量</label>
          <span>{{mainInfo.hasFinish}}</span>
        </div>
      </div>
    </div>
    <div class="good-at">
      <div>
        <div class="title">
          擅长技能
        </div>
        <i></i>
      </div>
      <div class="add" @click="showBox">{{goodAtText}}</div>
      <div class="user-select" @click="remove">
        <span v-for="item in selected">{{item}}<i class="glyphicon glyphicon-remove"></i></span>
      </div>
      <transition name="box-fade">
        <div class="add-box" v-show="goodAtBox">
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
    <div class="project">
      <div>
        <div class="title">
          项目案例
        </div>
        <i></i>
      </div>
      <div class="add" @click="showBoxPro">{{projectText}}</div>
      <transition name="box-fade" >
        <div v-if="projectBox" class="add-box">
          <span>建议提交两个以上具有代表性的作品</span>
          <project-box
          @proCancle="showBoxPro"
          @confirmPro="confirmPro"
          ></project-box>
        </div>
      </transition>
      <show-old-pro v-for="item in projectList" :item="item"></show-old-pro>
    </div>
    <div class="submit-banner">
      <span @click="submit">保存</span>
      <router-link :to="{name:'showUserInfo', params: {id: id}}"><span>预览</span></router-link>
    </div>
  </div>
</template>
<script>
  import {baseUrl} from '@/config/config'
  import MyProgress from '@/components/share/MyProgress'
  import {mapMutations} from 'vuex'
  import Portrait from '@/components/Portrait'
  import ProjectBox from '@/components/ProjectBox'
  import {category} from '@/js/webData'
  import ShowOldPro from '@/components/ShowOldPro'
  export default {
    created () {
      this.mainInfo.headImg = this.$store.state.headPic
    },
//    mounted () {
//      this.listenPortrait()
//    },
    data () {
      return {
        id: null,
        baseUrl: baseUrl,
        showPortrait: false,
        mainInfo: {},
        reader: new FileReader(), //todo  不能全局要修改
        goodAtBox: false,
        projectBox: false,
        category: category,
        selected: [],
        goodAtText: '添加',
        projectText: '添加',
        projectList: [],
        viewId: 0
      }
    },
    methods: {
      getInfo () {
        let store = window.localStorage
        this.id = store['token'].split('-')[0]
        this.$http.get(baseUrl + 'userInfoShow', {params: {id: store['token'].split('-')[0]}})
          .then(res => {
            this.mainInfo = res.data
            this.$store.commit('changeHead', this.mainInfo.headImg) // todo 独立出来，所有页面共用获取base信息
            this.projectList = this.mainInfo.projectList
            if (this.mainInfo.goodAt !== '') {
              if (this.mainInfo.goodAt !== null) {
                this.selected = this.mainInfo.goodAt.split(' ')
              }
            }
          }, res => {
            alert('获取数据失败')
          })
      },
      listenPortrait () {
        $('.userImg>input').bind('change', () => {
          this.reader.readAsDataURL($('.userImg>input')[0].files[0])
          this.reader.addEventListener("load", () => {
            this.$store.commit('changeSingerState', {stateName: 'curtain', value: true})
            this.showPortrait = true
          }, false);
        })
      },
      ...mapMutations(['changeSinger']),
      submit () {
        this.mainInfo.projectList = this.projectList
        this.mainInfo.goodAt = this.selected.join(' ');
        this.mainInfo.token = window.localStorage.token
        this.$http.post(baseUrl + 'userInfoSave', this.mainInfo)
          .then(res => {
            location.reload()
          }, res => {
            console.log(res.data)
          })
      },
      changePortrait () {
        $('.userImg>input').click()
      },
      confirmHeadPic (headSrc) {
        this.next('showPortrait')
        $('.userImg>img')[0].src = headSrc.result
        this.mainInfo.headPic = headSrc.result.split(/;base64,/)[1]
      },
      confirmPro (obj) {
        this.projectList.unshift(obj)
        this.showBoxPro()
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
      },
      showBoxPro () {
        this.projectBox = !this.projectBox
        if (this.projectText === '添加') {
          this.projectText = '取消'
          this.viewId++
        } else {
          this.projectText = '添加'
        }
      },
      next (dialogName) {
        this[dialogName] = !this[dialogName]
        console.log(this.showPortrait)
        this.$store.commit('changeSinger', 'curtain')
      }
    },
    beforeRouteEnter (to, from, next) {
      next(vm => {
        if (!vm.$store.state.hasLogin) {
          vm.$router.push({name: 'index'})
        }
        vm.getInfo()
        vm.listenPortrait()
        vm.$store.commit('changeSingerState', {stateName: 'myHeader', value: true})
      })
    },
    components: {
      MyProgress,
      Portrait,
      ProjectBox,
      ShowOldPro
    }
  }
</script>
