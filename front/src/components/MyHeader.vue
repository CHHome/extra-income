<template>
  <div>
    <login v-if="showLogin" @login="login"></login>
    <header>
      <div @click="login">
        登录
      </div>
    </header>
  </div>
</template>
<style scoped>
  header{
    width: 100%;
    height: 60px;
    background-color: #ffae83;
  }
  header div:nth-child(1){
    float: right;
    cursor: pointer;
  }
</style>
<script>
  import {mapMutations} from 'vuex'
  import Login from '@/components/Login'
  export default {
    name: 'MyHeader',
    data () {
      return {
        showLogin: false,
        showRegister: false
      }
    },
    components: {
      Login
    },
    methods: {
      ...mapMutations(['changeSinger']),
      login () {
        this.showLogin = !this.showLogin
        this.changeSinger('curtain')
      }
    }
  }
</script>

