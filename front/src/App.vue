<template>
  <div id="app">
    <register v-if="$store.state.showRegister"></register>
    <div class="curtain" v-if="$store.state.curtain"></div>
    <my-header v-if="!$store.state.adminLogin"></my-header>
    <keep-alive>
      <router-view/>
    </keep-alive>
    <my-footer v-if="!$store.state.adminLogin"></my-footer>
  </div>
</template>
<style scoped>
  .curtain{
    position: absolute;
    width: 100%;
    height: 100%;
    top:0;
    left: 0;
    background-color: #fff;
    opacity: 0.40;
    z-index: 1000;
  }
  #app div:nth-last-child(2){
    min-height: calc(100vh - 226px);
  }


</style>
<script>
  import MyHeader from '@/components/MyHeader'
  import MyFooter from '@/components/MyFooter'

  export default {
    name: 'app',
    data () {
      return {}
    },
    components: {
      MyHeader,
      MyFooter
    }
  }
</script>


