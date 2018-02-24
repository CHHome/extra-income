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
        label, span{
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
  .main-info span{
    color: #fff;
    vertical-align: middle;
    display: inline-block;
    overflow: hidden;
    white-space: nowrap;
    max-width: 100px;
    text-overflow: ellipsis;
  }
  .left-info{
    text-align: left;
  }
  .selected{
    background-color: #00ffb9;
  }
</style>
<template>
  <div class="user-info">
    <img v-bind:src="baseUrl+'static/imgs/userInfoBanner.jpg'" alt="">
    <div class="main-info row">
      <div class="col-md-7 ">
        <div class="row">
          <div class="col-md-6 userImg">
            <img v-bind:src="baseUrl+'static/imgs/'+mainInfo.headImg" alt="更换头像" >
          </div>
          <div class="col-md-6 left-info">
            <label>姓名  </label>
            <span>{{mainInfo.userName}}</span><br>
            <label>职业  </label>
            <span>{{mainInfo.profession}}</span><br>
            <label>年龄  </label>
            <span>{{mainInfo.age}}</span><br>
            <label>手机  </label>
            <span>{{mainInfo.phone}}</span><br>
            <label >邮箱  </label>
            <span>{{mainInfo.email}}</span><br>
            <label>简介  </label>
            <span :title="mainInfo.synopsis">{{mainInfo.synopsis}}</span><br>
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
          <span>{{mainInfo.price}}</span><br>
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
      <div class="user-select">
        <span v-for="item in selected">{{item}}</span>
      </div>
    </div>
    <div class="project">
      <div>
        <div class="title">
          项目案例
        </div>
        <i></i>
      </div>
      <show-old-pro v-for="item in projectList"
                    :item="item"
                    :type="'onlyShow'"></show-old-pro>
    </div>
  </div>
</template>
<script>
  import {baseUrl} from '@/config/config'
  import MyProgress from '@/components/share/MyProgress'
  import ShowOldPro from '@/components/ShowOldPro'
  export default {
    created () {
      this.mainInfo.headImg = 'default_head.jpg'
    },
    mounted(){
      console.log('mounted')
    },
    props: ['id'],
    data(){
      return{
        mainInfo: {},
        baseUrl: baseUrl,
        selected: [],
        projectList: [],
        viewId: 0
      }
    },
    methods: {
      getInfo () {
        let store = window.localStorage
        console.log('get')
        this.$http.get(baseUrl + 'userInfoShow', {params: {id: this.id, type: 'onlyShow'}})
          .then(res => {
            this.mainInfo = res.data
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
    },
    components: {
      MyProgress,
      ShowOldPro
    },
    beforeRouteEnter (to, from, next) {
      next(vm => {
        vm.getInfo()
        window.onscroll = function () {}
        vm.$store.commit('changeSingerState', {stateName: 'myHeader', value: true})
      })
    },
    beforeRouteLeave (to, from, next) {
      console.log('sfsf')
      this.mainInfo = {}
      this.mainInfo.headImg = 'default_head.jpg'
      this.selected = []
      this.projectList = []
      next()
    }
  }
</script>
