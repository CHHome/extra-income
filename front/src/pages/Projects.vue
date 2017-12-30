<template>
  <div class="projects-container">
    projects
  </div>
</template>
<script>
  import {baseUrl} from '@/config/config'
  import {mapMutations} from 'vuex'
  export default {
    methods: {
      ...mapMutations(['changeSinger'])
    },
    beforeRouteEnter (to, from, next) {
      next(vm => {
        console.log('sss')
        window.onscroll = function () {}
        vm.$store.commit('changeMyHeader', true)
      })
    }
  }
</script>
<style scoped>
  .projects-container{
    padding-top: 60px;
  }
</style>
