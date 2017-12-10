<template>
  <div>
    <login v-if="showLogin" @next="next"></login>
    <register v-if="showRegister" @next="next"></register>
    <header>
      <div @click="next('showLogin')">
        登录
      </div>
      <div @click="next('showRegister')">
        注册
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
  header div:nth-child(1), header div:nth-child(2){
    float: right;
    cursor: pointer;
  }
</style>
<script>
  import {mapMutations} from 'vuex'
  import Login from '@/components/Login'
  import Register from '@/components/Register'
  export default {
    name: 'MyHeader',
    data () {
      return {
        showLogin: false,
        showRegister: false
      }
    },
    components: {
      Login,
      Register
    },
    methods: {
      ...mapMutations(['changeSinger']),
      next (dialogName) {
        this[dialogName] = !this[dialogName]
        this.changeSinger('curtain')
      }
    }
  }
</script>

