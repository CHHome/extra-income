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
      .row{
        margin: auto;
      }
    }
  }
</style>
<template>
  <div class="show-release">
    <img src="../assets/releaseBanner.jpg" alt="banner">
    <release-info
      :data="data"
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
    :itemData="data"></release-form>
    <div class="release-apply-list" v-if="modifyIcon">
      <header>申请列表</header>
      <div class="row">
        <apply-card :item="item" v-for="item in applyUserList"
                    :key="item.id">
          <span class="agree"
                @click="agree(item.id, item.applyUserId)"
          slot="agree">同意申请</span>
        </apply-card>
      </div>
    </div>
  </div>
</template>
<script>
  import {baseUrl} from '@/config/config'
  import ReleaseForm from '@/components/share/ReleaseForm'
  import ApplyCard from '@/components/share/ApplyCard'
  import ReleaseInfo from '@/components/share/ReleaseInfo'

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
      },
      agree (applyId, applyUserId) {
        this.$ajax.post(baseUrl + 'generatingOrder', {
          applyId: applyId,
          employeeId: applyUserId,
          releaseId: this.data.id,
          employerId: this.data.employerId,
          cycle: this.data.cycle
        }).then(res => {

        }, res => {

        })
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
      ApplyCard,
      ReleaseInfo
    }
  }
</script>
