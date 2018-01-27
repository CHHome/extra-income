<template>
  <div class="projects-container">
    projects
    <span>sdjbkjdsksdf</span>
  </div>
</template>
<script>
  import {baseUrl} from '@/config/config'
  export default {
    beforeRouteEnter (to, from, next) {
      next(vm => {
        window.onscroll = function () {}
        vm.$store.commit('changeSingerState', {stateName: 'myHeader', value: true})
        vm.$http.get(baseUrl + 'user').then(res => {
          console.log(res.data)
        }, res => {
          console.log('fail')
        })
      })
    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import '../css/test.less';
  .projects-container{
    padding-top: 60px;
  }
  .projects-container{
    color: @base;
  }
  span{
    color: blue;
  }
</style>
