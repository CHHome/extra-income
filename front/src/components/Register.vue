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
  .validator-error{
    color: red;
  }
</style>
<template>
  <div id="dialog" class="col-sm-5">
    <form class="form-horizontal">
      <div class="form-group">
        <div class="col-sm-offset-2 col-sm-8" :class="{error:$v.phone.$error }">
          <input v-model="phone" @input="$v.phone.$touch()" type="text" id="phone" class="form-control" placeholder="请输入常用手机号" name="phone">
          <span class="validator-error" v-if="$v.phone.$error && !$v.phone.required">请输入手机号码</span>
          <span class="validator-error" v-if="!$v.phone.maxLength || !$v.phone.minLength">请输入11位手机号码</span>
          <span class="validator-error" v-if="!$v.phone.numeric">手机号码必须为数字</span>
        </div>
      </div>
      <div class="form-group">
        <div class="col-sm-offset-2 col-sm-8" :class="{error:$v.userName.$error }">
          <input v-model="userName" @input="$v.userName.$touch()" type="text" id='username' class="form-control " placeholder="请输入用户名" name="username">
          <span class="validator-error" v-if="$v.userName.$error && !$v.userName.required">请输入用户名</span>
          <span class="validator-error" v-if="!$v.userName.minLength">用户名至少两个字符</span>
        </div>
      </div>
      <div class="form-group">
        <div class="col-sm-offset-2 col-sm-8" :class="{error:$v.password.$error }">
          <input v-model.trim="password"  @input="delayTouch($v.password)" type="password" class="form-control psw" placeholder="请输入登录密码" name="password">
          <span class="validator-error" v-if="$v.password.$error && !$v.password.required">请输入密码</span>
          <span class="validator-error" v-if="!$v.password.minLength">密码至少六位数</span>
        </div>
      </div>
      <div class="form-group">
        <div class="col-sm-offset-2 col-sm-8" :class="{error:$v.password2.$error }">
          <input v-model.trim="password2"  @input="delayTouch($v.password2)" type="password" class="form-control psw" placeholder="请确认登录密码" name="password2">
          <span class="validator-error" v-if="$v.password2.$dirty && !$v.password2.sameAsPassword">两次密码输入不一致</span>
          <span>{{$v.password2.$dirty}}</span>
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
  import { required, sameAs, minLength, maxLength, numeric} from 'vuelidate/lib/validators'

  const touchMap = new WeakMap()
  export default {
    name: 'Register',
    data () {
      return {
        userName: '',
        phone: '',
        password: '',
        password2: ''
      }
    },
    validations: {
      userName: {
        required,
        minLength: minLength(2)
      },
      password: {
        required,
        minLength: minLength(6)
      },
      password2: {
        sameAsPassword: sameAs('password')
      },
      phone: {
        required,
        minLength: minLength(11),
        maxLength: maxLength(11),
        numeric
      },
      validationGroup: ['userName', 'password', 'phone', 'password2']
    },
    methods: {
      cancel () {
        this.$emit('next', 'showRegister')
      },
      delayTouch ($v) {
        $v.$reset()
        if (touchMap.has($v)) {
          clearTimeout(touchMap.get($v))
        }
        touchMap.set($v, setTimeout($v.$touch, 1000))
      },
      submit () {
        if (this.$v.validationGroup.$invalid) {
          this.$v.userName.$touch()
          this.$v.password.$touch()
          this.$v.password2.$touch()
          this.$v.phone.$touch()

          return
        }
        this.$http.post(baseUrl + 'register', {
          phone: this.phone,
          userName: this.userName,
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

