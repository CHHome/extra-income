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
        window.onscroll = function () {}
        vm.$store.commit('changeMyHeader', true)
        vm.$http.get(baseUrl+'user').then(res => {
          console.log(res.data)
        }, res => {
          console.log('fail')
        })

      })
    }
  }
</script>
<style scoped>
  .projects-container{
    padding-top: 60px;
  }
</style>
