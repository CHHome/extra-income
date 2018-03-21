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
    <release-form :type="'releasePro'" :key="viewId"></release-form>
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
    data () {
      return {
        viewId: 1
      }
    },
    beforeRouteEnter (to, from, next) {
      next(vm => {
        if (!vm.$store.state.hasLogin) {
          alert('请先登录')
          vm.$router.push({name: 'index'})
        }
        vm.$store.commit('changeSingerState', {stateName: 'myHeader', value: true})
      })
    },
    beforeRouteLeave (to, from, next) {
      this.viewId++
      next()
    },
  }
</script>
