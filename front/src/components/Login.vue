<style lang="less" rel="stylesheet/less" scoped>
  @import '../css/theme.less';
  #login-dialog{
    .my-dialog(35%);
    padding-top: 30px;
  }
  .loginBtn div > div,.loginBtn div >input{
    .btnTheme
  }
  .validator-error{
    color: red;
  }
</style>
<template>
  <div id="login-dialog" class="col-sm-5">
    <form class="form-horizontal">
      <div class="form-group">
        <label for="accout" class="col-sm-2 control-label">帐号:</label>
        <div class="col-sm-8" :class="{error:$v.userName.$error }">
          <input v-model="userName" @input="$v.userName.$touch()" type="text" id="accout" class="form-control" placeholder="请输入用户名" name="username">
          <span v-if="$v.userName.$error " class="validator-error">用户名是必须的</span>
        </div>
      </div>
      <div class="form-group">
        <label for="psw" class="col-sm-2 control-label">密码:</label>
        <div class="col-sm-8" :class="{error:$v.password.$error }">
          <input v-model="password" @input="$v.password.$touch()" type="password" id="psw" class="form-control" placeholder="请输入密码" name="password">
          <span v-if="$v.password.$error && !$v.password.required" class="validator-error">密码是必须的</span>
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
  import {required} from 'vuelidate/lib/validators'

  export default {
    name: 'Login',
    data () {
      return {
        userName: '',
        password: ''
      }
    },
  validations: {
   userName: {
     required
   },
    password: {
     required
    },
    validationGroup: ['userName', 'password']
  },
    methods: {
      cancel () {
        this.$emit('next', 'showLogin')
      },
      submit () {
        if (this.$v.validationGroup.$invalid) {
          this.$v.userName.$touch()
          this.$v.password.$touch()
          return
        }
        this.$http.post(baseUrl + 'login', {
          userName: this.userName,
          password: sha1(this.password)
        }, {emulateJSON: true}).then(res => {
//          todo 保存登录状态
          if (res.data !== 'fail') {
            let store = window.localStorage
            store['token'] = res.data
            this.$store.commit('changeLoginId', store['token'].split('-')[0])
            this.cancel()
            this.$store.commit('changeSingerState', {stateName: 'hasLogin', value: true})
            return this.$ajax.get(baseUrl + 'showBase', {
              params: {
                id: store['token'].split('-')[0]
              }
            })
          } else {
//            todo
            console.log('登录失败，请检查用户名和密码是否正确')
          }
        }, res => {
//          todo
          console.log('登陆失败，请检查网络')
        }).then(
          res => {
            this.$store.commit('changeHead', res.data.headImg)
          }, res => {
            alert('登录成功但获取您的相关基础信息失败')
          }
        )
      }
    }
  }
</script>

