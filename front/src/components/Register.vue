<style lang="less" rel="stylesheet/less" scoped>
  @import '../css/theme.less';
  #dialog{
    .my-dialog(35%);
  }
  .registerBtn div > div, .registerBtn div >input{
    .btnTheme
  }
  .form-control{
    border: 0;
    border-bottom: 1px solid #e6e6e6;
    box-shadow: none;
  }
</style>
<template>
  <div id="dialog" class="col-sm-5">
    <form class="form-horizontal">
      <div class="form-group">
        <div class="col-sm-offset-2 col-sm-8">
          <input v-model="phone" type="text" id="phone" class="form-control" placeholder="请输入常用手机号" name="phone">
        </div>
      </div>
      <div class="form-group">
        <div class="col-sm-offset-2 col-sm-8">
          <input v-model="username" type="text" id='username' class="form-control " placeholder="请输入用户名" name="username">
        </div>
      </div>
      <div class="form-group">
        <div class="col-sm-offset-2 col-sm-8">
          <input v-model="password" type="password" class="form-control psw" placeholder="请输入登录密码" name="password">
        </div>
      </div>
      <div class="form-group">
        <div class="col-sm-offset-2 col-sm-8">
          <input v-model="password2" type="password" class="form-control psw" placeholder="请确认登录密码" name="password2">
        </div>
      </div>
      <div class="form-group registerBtn">
        <div class="col-sm-offset-2 col-sm-10">
          <input type="button" value="注册" @click="submit">
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
    name: 'Register',
    data () {
      return {
        username: '',
        phone: '',
        password: '',
        password2: ''
      }
    },
    methods: {
      cancel () {
        this.$emit('next', 'showRegister')
      },
      submit () {
        this.$http.post(baseUrl + 'register', {
          phone: this.phone,
          username: this.username,
          password: sha1(this.password)
        }, {emulateJSON: true}).then(res => {
          console.log(res.data)
          if (res.data === '1') {
            if (confirm('注册成功!请登录')) {
              this.cancel()
              this.$emit('next', 'showLogin')
            }
          }
        }, res => {
          console.log(res.data)
        })
      }
    }
  }
</script>

