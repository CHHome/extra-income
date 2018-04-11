<style lang="less" rel="stylesheet/less" scoped>
  @import '../css/theme.less';
</style>
<template>
  <div>
    <keep-alive>
      <router-view/>
    </keep-alive>
  </div>
</template>

<script>

  export default {
    beforeRouteEnter (to, from, next) {
      next(vm => {
        vm.$store.state.adminLogin = true
        window.localStorage.removeItem('token')
        vm.$store.commit('changeLoginId', null)
      })
    }
  }
</script>
