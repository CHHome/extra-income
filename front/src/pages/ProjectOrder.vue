<style lang="less" rel="stylesheet/less" scoped>
  @import '../css/theme.less';
  .project-order{
    padding-top: 60px;
    img{
      width: 100%;
    }
    & > div, & > img{
      margin: 30px auto;
    }
    & > div{
      header{
        font-size: 16px;
        font-weight: 600;
        padding: 30px;
      }
      background-color: #fff;
      width: 90%;
      .participants{
       display: inline-block;
        & > div{
          width: 300px;
          margin: 0 auto;
          display: inline-block;
          border: 1px solid #ccc;
        }
      }
    }
    .order-progress{
      overflow: hidden;
      text-align: center;
      & > div{
        display: inline-block;
        width: 100%;
      }
      span{
        .btnTheme;
        margin-top: 25px;
      }
    }
  }
</style>
<template>
  <div class="project-order">
    <img src="../assets/releaseBanner.jpg" alt="banner">
    <release-info
      :data="releaseProData"
      v-if="!showModify">
      <!--运用slot实现实现组件的复用，防止组件强依赖-->
      <i slot="icon"
         class="glyphicon glyphicon-pencil"
         title="修改"
         @click="modify"
         v-if="modifyIcon"></i>

      <div class="container-apply"
           v-if="!modifyIcon"
           @click="sendApply"
           slot="applyBtn">
        发送申请
      </div>
    </release-info>
    <release-form
      :type="'showReleasePro'"
      v-if="showModify"
      @cancelModify="modify"
      :itemData="releaseProData"></release-form>
    <div class="participant-info">
      <header>参与者信息</header>
      <div class="participants clearfix">
        <div v-for="item in Object.keys(participantInfo)">
          <apply-card :item="participantInfo[item]" ></apply-card>
        </div>
      </div>
    </div>
    <div class="order-progress">
      <header>项目进度</header>
      <div>
        <my-progress
          :label="'进度条'"
          :value="orderData.progress"
        ></my-progress>
        <div v-if="!modifyIcon">
          输入最新进度：<input type="text" v-model="orderData.progress"><br>
          <span v-if="orderData.status=='进行中'" @click="updateProgress">更新进度</span>
          <span v-if="orderData.status=='进行中'" @click="submitProgress">交付项目</span>
          <span v-if="orderData.status=='交付中'">交付中</span>
        </div>
        <div v-if="modifyIcon">
          <span v-if="orderData.status=='进行中'">进行中</span>
          <span v-if="orderData.status=='交付中'">验收通过</span>
          <span v-if="orderData.status=='交付中'">验收不通过</span>
        </div>
        <span v-if="orderData.status=='已完成'">已完成</span>
      </div>
    </div>
  </div>
</template>
<script>
  import {baseUrl} from '@/config/config'
  import ReleaseForm from '@/components/share/ReleaseForm'
  import ReleaseInfo from '@/components/share/ReleaseInfo'
  import ApplyCard from '@/components/share/ApplyCard'
  import MyProgress from '@/components/share/MyProgress'

  export default {
    props: ['id'],   //todo 订单id
    data () {
      return{
        releaseData: {}, //todo 项目信息
        orderData: {},
        showModify: false,
        modifyIcon: false,
        releaseProData: {},
        participantInfo: {}
      }
    },
    components: {
      ReleaseForm,
      ReleaseInfo,
      ApplyCard,
      MyProgress
    },
    methods: {
      getData () {
        this.$ajax.get(baseUrl + 'showOrderData', {
          params: {
            releaseId: this.id,
          }
        })
          .then(
            res => {
              this.orderData = res.data
              return this.orderData
            }, res => {
              alert('获取数据失败，请检查网络')
            }
          )
          .then(
            data => {
              if (parseInt(this.$store.state.loginId !== data.employeeId) || parseInt(this.$store.state.loginId !== data.employerId)) {
                alert('非法访问，请立即退出!')
                this.$router.push({name: 'index'})
              } else {
                return this.$ajax.get(baseUrl + 'showReleasePro', {
                  params:{
                    id: data.releaseId
                  }
                })
              }
            }
          )
          .then(
            res => {
              this.releaseProData = res.data
              console.log(this.releaseProData)
              if (parseInt(this.$store.state.loginId) === res.data.employerId) {
                this.modifyIcon = true
              } else {
                this.modifyIcon = false
              }
            }, res => {
              alert('获取数据失败，请检查网络')
            }
          )
          .then(() => {
            return this.$ajax.get(baseUrl + 'participantInfo', {
              params:{
                employerId: this.orderData.employerId,
                employeeId: this.orderData.employeeId
              }
            })
            }
          )
          .then(res => {
            this.participantInfo = res.data
          }, res => {
            alert('获取数据失败，请检查网络')
          })
      },
      modify () {
        this.showModify = !this.showModify
      },
      sendApply () {},
      updateProgress () {
        this.$ajax.get(baseUrl + 'updateProgress' ,{
          params: {
            orderId: this.orderData.id,
            value: this.orderData.progress
          }
        }).then(res => {
          if (res.data === 10003) {
            this.getData()
            alert('更新成功')
          } else {
            alert('更新失败')
          }
        }, res => {
          alert('更新失败，请检查网络')
        })
      },
      submitProgress () {
        this.$ajax.get(baseUrl + 'updateProgress' ,{
          params: {
            orderId: this.orderData.id,
            value: 100,
            type: '交付项目'
          }
        }).then(res => {
          if (res.data === 10004) {
            this.getData()
            alert('交付成功')
          } else {
            alert('交付失败')
          }
        }, res => {
          alert('交付失败，请检查网络')
        })      }
    },
    beforeRouteEnter (to, from, next) {
      next(vm => {
        if (!vm.$store.state.hasLogin) {
          alert('请先登录')
          vm.$router.push({name: 'index'})
        }
        vm.getData()
        window.onscroll = function () {}
        vm.$store.commit('changeSingerState', {stateName: 'myHeader', value: true})
      })
    },
  }
</script>
