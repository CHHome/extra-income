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
  </div>
</template>
<script>
  import {baseUrl} from '@/config/config'
  import ReleaseForm from '@/components/share/ReleaseForm'
  import ReleaseInfo from '@/components/share/ReleaseInfo'
  export default {
    props: ['id'],   //todo 订单id
    data () {
      return{
        releaseData: {}, //todo 项目信息
        orderData: {},
        showModify: false,
        modifyIcon: false,
        releaseProData: {}
      }
    },
    components: {
      ReleaseForm,
      ReleaseInfo
    },
    methods: {
      getData () {
        this.$ajax.get(baseUrl + 'showOrderData', {
          params: {
            orderId: this.$store.state.loginId,
          }
        }).then(res => {
          return res.data
        }, res => {
          alert('获取数据失败，请检查网络')
        }).then(data => {
          console.log(data)
          if (parseInt(this.$store.state.loginId !== data.employeeId) || parseInt(this.$store.state.loginId !== data.employerId)) {
            alert('非法访问，请立即退出!')
            this.$router.push({name: 'index'})
          } else {
            this.$ajax.get(baseUrl + 'showReleasePro', {
              params:{
                id: data.releaseId
              }
            }).then(res => {
              console.log(res.data)
              this.releaseProData = res.data
              if (parseInt(this.$store.state.loginId) === res.data.employerId) {
                this.modifyIcon = true
              } else {
                this.modifyIcon = false
              }
            }, res => {
              alert('获取数据失败，请检查网络')
            })
          }
        })
      },
      modify () {
        this.showModify = !this.showModify
      },
      sendApply () {}
//      getData () {
//        this.$ajax.get(baseUrl + 'showReleasePro',
//          {
//            params:{
//              id: this.id
//            }
//          }).then(res => {
//          this.data = res.data
//          if (this.$store.state.hasLogin) {
//            //todo 此处需要增加token验证用户token的正确性
//            let userId = this.$store.state.loginId
//            if (parseInt(userId) === this.data.employerId) {
//              this.modifyIcon = true
//              return this.$ajax.get(baseUrl + 'applyUserList', {
//                params:{
//                  releaseProId: this.id
//                }
//              })
//            } else {
//              this.modifyIcon = false
//              return null
//            }
//          }
//        }, res => {
//          confirm('获取数据失败，请检查网络连接')
//        }).then(res => {
//          if (res){
//            this.applyUserList = res.data
//          }
//        })
//      },
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
