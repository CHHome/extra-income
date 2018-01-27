<style lang="less" rel="stylesheet/less" scoped>
  @import '../css/theme.less';
  #login-dialog{
    .my-dialog(35%)
  }
  .loginBtn div > div,.loginBtn div >input{
    .btnTheme
  }
</style>
<template>
  <div id="login-dialog" class="col-sm-5">
    <form class="form-horizontal">
      <div class="form-group">
        <label for="accout" class="col-sm-2 control-label">帐号:</label>
        <div class="col-sm-8">
          <input v-model="username" type="text" id="accout" class="form-control" placeholder="请输入手机号/邮箱" name="username">
        </div>
      </div>
      <div class="form-group">
        <label for="psw" class="col-sm-2 control-label">密码:</label>
        <div class="col-sm-8">
          <input v-model="password" type="password" id="psw" class="form-control" placeholder="请输入密码" name="password">
        </div>
      </div>
      <div class="form-group">
        <div class="col-sm-offset-2 col-sm-10">
          <div class="checkbox">
            <label>
              <input type="checkbox"> 记住密码
            </label>
          </div>
        </div>
      </div>
      <div class="form-group loginBtn">
        <div class="col-sm-offset-2 col-sm-10">
          <input type="button" value="登录" @click="submit">
          <div @click="cancel">
            取消
          </div>
        </div>
      </div>
    </form>
  </div>
</template>
<script>
  import {baseUrl} from '@/config/config'
  import sha1 from 'js-sha1'
  export default {
    name: 'Login',
    data () {
      return {
        username: '',
        password: ''
      }
    },
    methods: {
      cancel () {
        this.$emit('next', 'showLogin')
      },
      submit () {
        this.$http.post(baseUrl + 'login', {
          username: this.username,
          password: sha1(this.password)
        }, {emulateJSON: true}).then(res => {
//          todo 保存登录状态
          if (res.data !== 'fail') {
            let store = window.localStorage
            store['token'] = res.data
            this.cancel()
            this.$store.commit('changeSingerState', {stateName: 'hasLogin', value: true})
          } else {
//            todo
            console.log('登录失败，请检查用户名和密码是否正确')
          }
        }, res => {
//          todo
          console.log('登陆失败，请检查网络')
        })
      }
    }
  }
</script>

