<template>
  <div id="app">
    <register v-if="$store.state.showRegister"></register>
    <div class="curtain" v-if="$store.state.curtain"></div>
    <my-header></my-header>
    <keep-alive>
      <router-view/>
    </keep-alive>
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

</style>
<script>
  import MyHeader from '@/components/MyHeader'
  export default {
    name: 'app',
    data () {
      return {}
    },
    components: {
      MyHeader
    }
  }
</script>


