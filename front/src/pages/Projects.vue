<template>
  <div class="projects-container">
    projects
  </div>
</template>
<script>
  import {mapMutations} from 'vuex'
  export default {
    methods: {
      ...mapMutations(['changeSinger'])
    }
//    beforeRouteEnter (to, from, next) {
//      next(vm => {
//        window.onscroll = function () {}
//        vm.$store.commit('changeMyHeader', true)
//      })
//    }
  }
</script>
<style scoped>
  .projects-container{
    padding-top: 60px;
  }
</style>
