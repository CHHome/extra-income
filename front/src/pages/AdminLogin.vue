<style lang="less" rel="stylesheet/less" scoped>
  @import '../css/theme.less';
  .admin-login{
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .el-input {
    width: 250px;
  }
</style>
<template>
  <div class="admin-login">
    <el-form ref="form" :model="form" label-width="100px" :label-position="'left'">
      <el-form-item label="管理员名：">
        <el-input v-model="form.name"></el-input>
      </el-form-item>
      <el-form-item  label="密码：">
        <el-input v-model="form.password"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">登录</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
  import {baseUrl, commonRules} from '@/config/config'

  export default {
    data () {
      return {
        form: {
          name: '',
          password: ''
        }
      }
    },
    methods: {
      onSubmit () {
        this.$ajax.get(baseUrl + 'adminLogin', {
          params: {
            name: this.form.name,
            password: this.form.password
          }
        })
          .then(res => {
            if (res.data === 100001) {
              this.$store.state.adminLogin = true
              this.$store.adminName = this.form.name
              this.$router.push({name: 'dashboard'})
            } else {
              this.$notify.error({
                title: '错误',
                message: '用户名或者密码错误',
                offset: 75
              })
            }
          }, res => {
            this.$notify.error({
              title: '错误',
              message: '网络连接失败',
              offset: 75
            })
          })
      }
    }
  }
</script>
