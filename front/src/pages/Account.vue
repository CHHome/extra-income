<style lang="less" rel="stylesheet/less" scoped>
  .account-page {
    padding-top: 60px;
    & > div, & > img{
      margin: 30px auto;
      padding: 30px;
    }
    & > div{
      header{
        font-size: 16px;
        font-weight: 600;
        text-align: center;
        padding-bottom: 30px;
      }
      background-color: #fff;
      width: 90%;
    }
    .my-money {
      display: flex;
      & > div{
        width: 50%;
        text-align: center;
        span{
          margin-right: 10px;
        }
      }
    }
    .account-history{
      & > div {
        width:85%;
        margin: auto;
        min-width:900px;
      }
    }
  }
</style>
<template>
  <div class="account-page">
    <div class="account-info" v-loading="loading">
      <el-dialog title="充值" :visible.sync="rechargeDialog">
        <el-form :model="rechargeForm" ref="rechargeForm" :rules="inputRules" label-width="100px" class="demo-ruleForm">
          <el-form-item
            label="金额"
            prop="quota"
          >
            <el-input type="quota" v-model.number="rechargeForm.quota" auto-complete="off"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="rechargeDialog = false">取 消</el-button>
          <el-button type="primary" @click="submitForm('rechargeForm')">确 定</el-button>
        </div>
      </el-dialog>
      <header>账户信息</header>
      <div class="my-money">
        <div>
          <strong>账户余额：</strong>
          <el-tag  type="success">{{accountAllInfo.balance}}元</el-tag>
          <el-button  type="primary" size="small" @click="rechargeDialog = true">充值</el-button>
          <el-button  type="success" size="small">提现</el-button>
        </div>
        <div>
          <strong>押金：</strong>
          <el-tag  type="danger">{{accountAllInfo.deposit}}元</el-tag>
        </div>
      </div>
    </div>
    <div class="account-history">
      <header>账户流水</header>
        <el-table
          :data="accountAllInfo.turnoverList"
          style="width: 900px">
          <el-table-column
            prop="time"
            label="日期"
            width="180">
          </el-table-column>
          <el-table-column
            prop="type"
            label="类型"
            width="180">
          </el-table-column>
          <el-table-column
            prop="quota"
            width="180"
            label="金额(元)">
          </el-table-column>
          <el-table-column
            prop="balance"
            width="180"
            label="余额(元)">
          </el-table-column>
          <el-table-column
            prop="deposit"
            width="180"
            label="押金(元)">
          </el-table-column>
        </el-table>
    </div>
  </div>
</template>
<script>
  import {baseUrl, commonRules} from '@/config/config'

  export default {
    data () {
      return {
        accountAllInfo: {},
        rechargeDialog: false,
        rechargeForm: {
          quota: 0
        },
        loading: false,
        formLabelWidth: '120px',
        commonRules: commonRules,
        inputRules: {
          quota: [
            { validator: this.checkQuota, trigger: 'blur' },
          ]
        }
      }
    },
    methods: {
      getDate() {
        let store = window.localStorage
        this.id = store['token'].split('-')[0]
        this.$ajax.get(baseUrl + 'showAccountInfo', {
          params: {
            userId: this.id
          }
        })
          .then(res => {
            this.accountAllInfo = res.data
          }, res => {
            this.$notify.error({
              title: '错误',
              message: '获取数据失败， 请检查网络链接',
              offset: 75
            })
          });
      },
      checkQuota(rule, value, callback) {
        if (!value && value !== 0) {
          return callback(new Error('充值金额不能为空'));
        }
        if (!Number.isInteger(value)) {
          callback(new Error('请输入数字值'));
        } else {
          if (value <= 0) {
            callback(new Error('充值金额必须大于0'));
          } else {
            callback();
          }
        }
      },
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            this.loading = true
            this.rechargeDialog = false
            this.$ajax.post(baseUrl + 'recharge', $.extend(true, {}, this.rechargeForm, {userId: this.id}))
              .then(res => {
                if (res.data === 'success') {
                  this.loading = false
                  this.$notify({
                    title: '充值成功',
                    message: '充值成功, 已更新账户信息',
                    type: 'success',
                    offset: 75
                  })
                  this.getDate()
                }
              }, res => {
                this.$notify.error({
                  title: '充值失败',
                  message: '获取数据失败， 请检查网络链接',
                  offset: 75
                })
              })
          } else {
            return false;
          }
        });
      },
    },

    beforeRouteEnter (to, from, next) {
      next(vm => {
        if (!vm.$store.state.hasLogin) {
          vm.$router.push({name: 'index'})
        }
        vm.getDate();
        vm.$store.commit('changeSingerState', {stateName: 'myHeader', value: true})
      })
    }
  }
</script>
