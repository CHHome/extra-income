<style lang="less" rel="stylesheet/less" scoped>
  @import '../css/theme.less';
  .show-release{
    padding-top: 60px;
    img{
      width: 100%;
    }
    & > div, & > img{
      margin-bottom: 40px;
    }
    .show-release-container{
      background-color: #fff;
      padding: 0 10%;
      display: -webkit-box; /* 老版本语法: Safari, iOS, Android browser, older WebKit browsers. */
      display: -moz-box; /* 老版本语法: Firefox (buggy) */
      display: -ms-flexbox; /* 混合版本语法: IE 10 */
      display: -webkit-flex; /* 新版本语法: Chrome 21+ */
      display: flex; /* 新版本语法: Opera 12.1, Firefox 22+ */
      -webkit-box-pack: center;
      -moz-justify-content: center;
      -webkit-justify-content: center;
      justify-content: center;
      flex-wrap: wrap;
      .title{
        span{
          margin-right: 8px;
          &:nth-child(1), &:nth-child(2){
            font-size: 16px;
            font-weight: 700;
          }
        }
        & > span:nth-child(3){
          margin-left: 8px;
          padding: 2px 10px;
          border: 1px solid @secondColor;
          border-radius: 8px;
          background-color: @secondColor;
          color: #fff;
        }
      }
      .container-right{
        margin: 20px 0;
        width:65%;
        min-width: 320px;
        padding: 0 10%;
        .title i{
          color: @secondColor;
          cursor: pointer;
          float: right;
          margin-right: 30px;
          font-size: 20px;
        }
        & > div{
          margin-bottom: 30px;
        }
        .container-title{
          & > div{
            display: flex;
            justify-content: flex-start;
            margin-bottom: 15px;
            & > div{
              span{
                display: inline-block;
              }
              padding-right: 60px;
              & > span:nth-child(1){
                color: #999;
                margin-right: 8px;
              }
            }
          }
        }
        .container-describe{
          header{
            display: inline;
            padding-right: 20px;
            padding-bottom: 20px;
            border-bottom: 1px solid #999;
          }
          p{
            margin-top: 35px;
          }
        }
      }
      .container-left{
        width: 35%;
        background-color: @secondColor;
        min-width: 300px;
        margin-top: -8%;
        color: #fff;
        & > div{
          width: 80%;
          padding: 30px 0;
          margin: 0 auto;
          & > div{
            margin-bottom: 30px;
            & > span{
              &:nth-child(1){
                color: #999;
                font-size: 16px;
              }
              &:nth-child(3){
                font-size: 24px;
                font-weight: 700;
              }
            }
          }
        }
        .container-parameters{
          & > div{
            margin-bottom: 8px;
          }
        }
        .container-apply{
          cursor: pointer;
          border-radius: 4px;
          text-align: center;
          padding: 13px 8px;
          background-color: #fff;
          color: @secondColor;
        }
      }
    }
  }
</style>
<template>
  <div class="show-release">
    <img src="../assets/releaseBanner.jpg" alt="banner">
    <div class="show-release-container" v-if="!showModify">
      <div class="container-left">
        <div>
          <div>
            <span>项目预算</span><br>
            <span>{{data.budget}}</span>
          </div>
          <div>
            <span>项目周期</span><br>
            <span>{{data.cycle}}</span>
          </div>
          <div class="container-apply">
            发送申请
          </div>
          <div class="container-parameters">
            <div>
              <span>申请数</span>
              <span>{{data.apply}}</span>
            </div>
            <div>
              <span>浏览数</span>
              <span>{{data.browse}}</span>
            </div>
          </div>
        </div>
      </div>
      <div class="container-right">
        <div class="title">
          <span>项目名称</span><span>{{data.projectName}}</span>
          <span>{{data.status}}</span>
          <i class="glyphicon glyphicon-pencil" title="修改" @click="modify" v-if="modifyIcon"></i>
        </div>
        <div class="container-title">
          <div>
            <div>
              <span>项目类型</span><br>
              <span>{{data.firstType}}/{{data.secondType}}</span>
            </div>
            <div>
              <span>公司</span><br>
              <span>{{data.company}}</span>
            </div>
          </div>
          <div>
            <div>
              <span>发布时间</span>
              <span>{{data.releaseTime}}</span>
            </div>
          </div>
        </div>
        <div class="container-describe">
          <header>项目描述</header>
          <p>{{data.describe}}</p>
        </div>
      </div>
    </div>
    <release-form
      :type="'showReleasePro'"
      v-if="showModify"
      @cancelModify="modify"
    :itemData="data"></release-form>
  </div>
</template>
<script>
  import {baseUrl} from '@/config/config'
  import ReleaseForm from '@/components/share/ReleaseForm'
  export default {
    data () {
      return{
        data: {},
        showModify: false,
        modifyIcon: false
      }
    },
    methods: {
      getData () {
        this.$ajax.get(baseUrl + 'showReleasePro',
          {
            params:{
              id: this.id
            }
          }).then(res => {
          this.data = res.data
          let store = window.localStorage
          if (this.$store.state.hasLogin && store['token']) {
            //todo 此处需要增加token验证用户token的正确性
            let userId = store['token'].split('-')[0]
            if (parseInt(userId) === this.data.employerId) {
              this.modifyIcon = true
            }
          }
        }, res => {
            confirm('获取数据失败，请检查网络连接')
        })
      },
      modify () {
        this.showModify = !this.showModify
      },
    },
    props: ['id'],
    beforeRouteEnter (to, from, next) {
      next(vm => {
        vm.getData()
        window.onscroll = function () {}
        vm.$store.commit('changeSingerState', {stateName: 'myHeader', value: true})
      })
    },
    components: {
      ReleaseForm
    }
  }
</script>
