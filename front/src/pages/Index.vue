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
    <header>
      精选高质量可信赖的专家/团队入驻平台<br/>
      <span class="subtitle">每一位专家都经过严格审核</span>
    </header>
      <div class="experts clearfix">
        <router-link :to="{name: 'expert'}">
          <div class="col-md-3 col-sm-4 ">
            <img src="../assets/genchan.jpeg" alt="chengenhong">
            <div class="export-introduce">
              <span>陈根鸿</span>
              / 全栈开发工程师 <br>
              <span>提供一站式网站开发</span>
            </div>
          </div>
        </router-link>
        <router-link :to="{name: 'expert'}">
          <div class="col-md-3 col-sm-4 ">
            <img src="../assets/genchan.jpeg" alt="chengenhong">
            <div class="export-introduce">
              <span>陈根鸿</span>
              / 全栈开发工程师 <br>
              <span>提供一站式网站开发</span>
            </div>
          </div>
        </router-link>
        <router-link :to="{name: 'expert'}">
          <div class="col-md-3 col-sm-4 ">
            <img src="../assets/genchan.jpeg" alt="chengenhong">
            <div class="export-introduce">
              <span>陈根鸿</span>
              / 全栈开发工程师 <br>
              <span>提供一站式网站开发</span>
            </div>
          </div>
        </router-link>
        <router-link :to="{name: 'expert'}">
          <div class="col-md-3 col-sm-4 ">
            <img src="../assets/genchan.jpeg" alt="chengenhong">
            <div class="export-introduce">
              <span>陈根鸿</span>
              / 全栈开发工程师 <br>
              <span>提供一站式网站开发</span>
            </div>
          </div>
        </router-link>
        <router-link :to="{name: 'expert'}">
          <div class="col-md-3 col-sm-4 ">
            <img src="../assets/genchan.jpeg" alt="chengenhong">
            <div class="export-introduce">
              <span>陈根鸿</span>
              / 全栈开发工程师 <br>
              <span>提供一站式网站开发</span>
            </div>
          </div>
        </router-link><router-link :to="{name: 'expert'}">
        <div class="col-md-3 col-sm-4 ">
          <img src="../assets/genchan.jpeg" alt="chengenhong">
          <div class="export-introduce">
            <span>陈根鸿</span>
            / 全栈开发工程师 <br>
            <span>提供一站式网站开发</span>
          </div>
        </div>
      </router-link>
        <router-link :to="{name: 'expert'}">
          <div class="col-md-3 col-sm-4 ">
            <img src="../assets/genchan.jpeg" alt="chengenhong">
            <div class="export-introduce">
              <span>陈根鸿</span>
              / 全栈开发工程师 <br>
              <span>提供一站式网站开发</span>
            </div>
          </div>
        </router-link>
        <router-link :to="{name: 'expert'}">
          <div class="col-md-3 col-sm-4 ">
            <img src="../assets/genchan.jpeg" alt="chengenhong">
            <div class="export-introduce">
              <span>陈根鸿</span>
              / 全栈开发工程师 <br>
              <span>提供一站式网站开发</span>
            </div>
          </div>
        </router-link>

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
  header{
    color: #000;
    text-align: center;
    font-size: 30px;
    margin-top: 60px;
    font-weight: 600;
  }
  .subtitle{
    font-weight:normal;
    font-size: 16px;
  }
  .experts{
    width: 90%;
    margin: 20px auto;
  }
  .experts > div{
    margin-top: 20px;
    cursor: pointer;
  }
  .experts img{
    width:100%;
    height: 230px;
  }
  .export-introduce{
    text-align: center;
    padding-top: 12px;
    padding-bottom: 10px;
    font-size: 14px;
    background-color: #fff;
  }
  .export-introduce span:nth-child(1){
    font-size: 20px;
    font-weight: 600;
  }
</style>
<script>
  import 'swiper/dist/css/swiper.min.css'
  import Swiper from 'swiper/dist/js/swiper.min'
  export default {
    beforeRouteEnter (to, from, next) {
      next(vm => {
        vm.$store.commit('changeMyHeader', false)
        window.onscroll = () => {
          if (document.documentElement.scrollTop >= 540) {
            vm.$store.commit('changeMyHeader', true)
          } else {
            vm.$store.commit('changeMyHeader', false)
          }
        }
      })
    },
    beforeRouteLeave (to, from, next) {
      window.onscroll = function () {}
      this.$store.commit('changeMyHeader', true)
      next()
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
    }
  }
</script>
