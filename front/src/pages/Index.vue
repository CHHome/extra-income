<template>
  <div>
    <div class="swiper-container">
      <div class="swiper-wrapper">
        <div class="swiper-slide"><img src="../assets/banner1.jpg" ></div>
        <div class="swiper-slide"><img src="../assets/banner2.jpg" ></div>
      </div>
      <!-- Add Pagination -->
      <div class="swiper-pagination"></div>
    </div>
    <div style="height: 900px">

    </div>
  </div>
</template>
<style scoped>
  .swiper-container{
    height:600px;
  }
  .swiper-slide img{
    height:100%;
    width:100%;
  }
</style>
<script>
  import 'swiper/dist/css/swiper.min.css'
  import Swiper from 'swiper/dist/js/swiper.min'
  export default {
    beforeRouteEnter (to, from, next) {
      next(vm => {
        vm.$store.commit('changeMyHeader', false)
      })
    },
    data () {
      return {}
    },
    mounted () {
      var swiper = new Swiper('.swiper-container', {
        spaceBetween: 30,
        effect: 'fade',
        autoplay: {
          delay: 3000,
          disableOnInteraction: false
        },
        loop: true,
        pagination: {
          el: '.swiper-pagination',
          clickable: true
        }
      })
      window.onscroll = () => {
        if (document.documentElement.scrollTop >= 540) {
          this.$store.commit('changeMyHeader', true)
        } else {
          this.$store.commit('changeMyHeader', false)
        }
      }
    }
  }
</script>
