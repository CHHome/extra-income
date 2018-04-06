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
      .apply-card{
        padding-bottom: 10px;
        border: 1px solid #ccc;
        position: relative;
        cursor: pointer;
        margin-top: 20px;
      }
      header{
        padding: 10px 15px;
        border-bottom: 1px solid #ccc;
      }
      .row{
        margin: auto;
      }
    }
    .release-apply-list-tip{
      text-align: center;
      color: @secondColor;
    }
  }
</style>
<template>
  <div class="show-release">
    <el-dialog
      title="提示"
      :visible.sync="applyConfirm"
      width="30%"
      :before-close="handleClose">
      <span>确定申请本项目吗？申请成功后，您余额中的{{data.budget}}元将作为押金，暂时不能动用!</span>
      <span slot="footer" class="dialog-footer">
    <el-button @click="applyConfirm = false">取 消</el-button>
    <el-button type="primary" @click="sendApply">确 定</el-button>
  </span>
    </el-dialog>
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
           @click="applyConfirm = true"
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
        <div class="col-md-3 col-sm-4 apply-card" v-for="item in applyUserList">
          <apply-card :item="item"
                      :key="item.id">
          <span class="agree"
                @click="agree(item.id, item.applyUserId)"
                slot="agree">同意申请</span>
          </apply-card>
        </div>
        <div v-if="applyUserList.length === 0" class="release-apply-list-tip">还没有专家申请呢，请稍后刷新查看</div>
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
        applyUserList: [],
        applyConfirm: false
      }
    },
    methods: {
      handleClose(done) {
        this.$confirm('确认关闭？')
          .then(_ => {
            done();
          })
          .catch(_ => {});
      },
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
          this.applyConfirm = false
          this.$ajax.get(baseUrl + 'addApply', {
            params: {
              ReleaseProId: this.id,
              applyUserId: this.$store.state.loginId
            }
          }).then(res => {
            if (res.data === 100001) {
              this.$notify.error({
                title: '申请成功',
                message: '申请消息已经发送给雇主，请耐心等待',
                offset: 75
              })
              this.increase('applyAmount')
            } else {
              if (res.data === 100002) {
                this.$notify.error({
                  title: '错误',
                  message: '您的余额不足以作为此项目的押金, 请前往充值',
                  offset: 75
                })
              } else {
                this.$notify.error({
                  title: '错误',
                  message: '您已经申请过本项目',
                  offset: 75
                })
              }
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
          if (res.data = 10008) {
            alert('已生成订单，请在我的项目中查看项目进度等信息')
          } else {
            alert('操作异常')
          }
        }, res => {
          alert('操作失败，请检查网络')
        })
      },
      increase (type) {
        this.$ajax.get(baseUrl+ 'increase', {
          params: {
            releaseId: this.id,
            type: type
          }
        }).then(res => {
          if (res.data === 10007) {
            return
          }else {
            alert('不好了，服务器好像出现了问题')
          }
        }, res => {
          alert('请检查网络连接')
        })
      }
    },
    props: ['id'],
    beforeRouteEnter (to, from, next) {
      next(vm => {
        vm.getData()
        if (vm.id !== parseInt(vm.$store.state.loginId)) {
          vm.increase('browse')
        }
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
