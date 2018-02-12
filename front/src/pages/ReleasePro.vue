<style lang="less" rel="stylesheet/less" scoped>
  @import '../css/theme';
  .release{
    padding-top: 60px;
    text-align: center;
    img{
      width: 100%;
    }
    & > div, & > img{
      margin-bottom: 60px;
    }
    & > div:nth-last-child(1){
      span{
        .btnTheme
      }
      text-align: center;
    }
  }
</style>
<template>
  <div class="release">
    <img src="../assets/releaseBanner.jpg" alt="banner">
    <release-form :type="'releasePro'"></release-form>
    <router-link :to="{name: 'showReleasePro', params: {id: 2}}">test</router-link>
  </div>
</template>
<script>
  import {baseUrl} from '@/config/config'
  import {category} from '@/js/webData'
  import {required, maxLength, numeric} from 'vuelidate/lib/validators'
  import ReleaseForm from '@/components/share/ReleaseForm'
  export default {
    components: {
      ReleaseForm
    },
    beforeRouteEnter (to, from, next) {
      next(vm => {
        if (!vm.$store.state.hasLogin) {
          alert('请先登录')
          vm.$router.push({name: 'index'})
        }
        window.onscroll = function () {}
        vm.$store.commit('changeSingerState', {stateName: 'myHeader', value: true})
      })
    }
  }
</script>
