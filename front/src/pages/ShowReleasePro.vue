<style lang="less" rel="stylesheet/less" scoped>
  @import '../css/theme.less';
  .show-release{
    padding-top: 60px;
    img{
      width: 100%;
    }
    & > div, & > img{
      margin: 30px auto;
    }
    .show-release-container{
      background-color: #fff;
      width: 80%;
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
            & > span:nth-child(1){
              color: #999;
            }
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
    .release-apply-list{
      width: 90%;
      margin:  auto;
      background-color: #fff;
      border-radius: 4px;
      padding-bottom: 30px;
      header{
        padding: 10px 15px;
        border-bottom: 1px solid #ccc;
      }
    }
  }
</style>
<template>
  <div class="show-release">
    <img src="../assets/releaseBanner.jpg" alt="banner">
    <div class="show-release-container row" v-if="!showModify">
      <div class="container-left col-md-4">
        <div>
          <div>
            <span>项目预算</span><br>
            <span>{{data.budget}}</span>
          </div>
          <div>
            <span>项目周期</span><br>
            <span>{{data.cycle}}</span>
          </div>
          <div class="container-apply" v-if="!modifyIcon" @click="sendApply">
            发送申请
          </div>
          <div class="container-parameters">
            <div>
              <span>申请数</span>
              <span>{{data.applyAmount}}</span>
            </div>
            <div>
              <span>浏览数</span>
              <span>{{data.browse}}</span>
            </div>
          </div>
        </div>
      </div>
      <div class="container-right col-md-8">
        <div class="title">
          <span>项目名称</span><span>{{data.projectName}}</span>
          <span>{{data.status}}</span>
          <i class="glyphicon glyphicon-pencil" title="修改" @click="modify" v-if="modifyIcon"></i>
        </div>
        <div class="container-title">
          <div>
            <div>
              <span>项目类型</span>
              <span>{{data.firstType}}/{{data.secondType}}</span>
            </div>
            <div>
              <span>公司</span>
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
    <div class="release-apply-list" v-if="modifyIcon">
      <header>申请列表</header>
      <div class="row">
        <router-link
          v-for="item in applyUserList"
          :key="item.id"
          :to="{name: 'showUserInfo', params: {id: item.id}}">
          <apply-card :item="item"></apply-card>
        </router-link>
      </div>
    </div>
  </div>
</template>
<script>
  import {baseUrl} from '@/config/config'
  import ReleaseForm from '@/components/share/ReleaseForm'
  import ApplyCard from '@/components/share/ApplyCard'
  export default {
    data () {
      return{
        data: {},
        showModify: false,
        modifyIcon: false,
        applyUserList: []
      }
    },
    methods: {
      getData () {
        this.data = {}
        this.$ajax.get(baseUrl + 'showReleasePro',
          {
            params:{
              id: this.id
            }
          }).then(res => {
          this.data = res.data
          if (this.$store.state.hasLogin) {
            //todo 此处需要增加token验证用户token的正确性
            let userId = this.$store.state.loginId
            if (parseInt(userId) === this.data.employerId) {
              this.modifyIcon = true
              return this.$ajax.get(baseUrl + 'applyUserList', {
                params:{
                  releaseProId: this.id
                }
              })
            } else {
              this.modifyIcon = false
              return null
            }
          }
        }, res => {
            confirm('获取数据失败，请检查网络连接')
        }).then(res => {
          if (res){
            this.applyUserList = res.data
          }
        })
      },
      modify () {
        this.showModify = !this.showModify
      },
      sendApply () {
        if (this.$store.state.loginId){
          this.$ajax.get(baseUrl + 'addApply', {
            params: {
              ReleaseProId: this.id,
              applyUserId: this.$store.state.loginId
            }
          }).then(res => {
            if (res.data === 100001) {
              confirm('已发送申请')
            } else {
              alert('您已经申请过该项目')
            }
          })
        } else {
          alert('请先登录')
        }
      }
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
      ReleaseForm,
      ApplyCard
    }
  }
</script>
