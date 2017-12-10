<template>
  <div id="app">
    <div class="curtain" v-if="$store.state.curtain"></div>
    <my-header></my-header>
    <router-view/>
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
    z-index: 10000;
  }
</style>
<script>
  import MyHeader from '@/components/MyHeader'
  export default {
    name: 'app',
    components: {
      MyHeader
    }
  }
</script>


