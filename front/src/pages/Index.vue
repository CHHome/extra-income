<style lang="less" rel="stylesheet/less" scoped>
  @import '../css/theme.less';
  .main-container{
    & > header{
      margin-top: 60px;
      color: #000;
      text-align: center;
      font-size: 30px;
      font-weight: 600;
      & > span{
        font-weight:normal;
        font-size: 16px;
      }
    }
    & > .swiper-container{
      height:700px;
      img{
        height:100%;
        width:100%;
      }
    }
    .experts{
      width: 90%;
      margin: auto;
      img{
        width:100%;
        height: 230px;
      }
      & > a > div{
        margin-top: 20px;
        &:hover{
          .box-shadow(rgba(71,83,108,.12), 0, 7px, 15px, 2px)
        }
      }
    }
    .export-introduce{
      text-align: center;
      padding-top: 12px;
      padding-bottom: 10px;
      font-size: 14px;
      background-color: #fff;
      color: #000;
      span:nth-child(1){
        font-size: 20px;
        font-weight: 600;
      }
    }
    .recommend-pro {
      background-color: #fff;
      width: 90%;
      margin: 0 auto;
      & > a{
        cursor: pointer;
        color: #000;
      }
    }
    .show-more-release{
      clear: both;
      text-align: center;
      padding: 8px;
      width: 90%;
      margin: 0 auto;
      cursor: pointer;
      a{
        color: #000;
        text-decoration: none;
        i{
          margin-left: 5px;
          font-size: 12px;
          font-weight: 500;
        }
      }
      &:hover{
        a{
          color: @secondColor;
        }
      }
    }
  }
</style>
<template>
  <div class="main-container">
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
    <div class="experts clearfix row">
      <router-link
        v-for="item in employee"
        :key="item.id"
        :to="{name: 'showUserInfo', params: {id: item.id}}">
        <div class="col-md-3 col-sm-4 ">
          <img alt="chengenhong" :src="baseUrl + 'static/imgs/' + item.headImg">
          <div class="export-introduce">
            <span>{{item.userName}}</span>
            / {{item.profession}} <br>
            <span>{{item.synopsis}}</span>
          </div>
        </div>
      </router-link>
    </div>
    <header>
      推荐对接最优质的项目<br>
      <span class="subtitle">每个项目的交易都有完善的保障</span>
    </header>
    <div class="recommend-pro clearfix row">
      <router-link
        v-for="item in releasePro"
        :to="{name: 'showReleasePro', params: {id: item.id}}"
        :key="item.id">
        <project-card :item="item"></project-card>
      </router-link>
      <div class="show-more-release">
        <router-link :to="{name: 'showMoreRelease'}">更多<i class="glyphicon glyphicon-plus"></i></router-link>
      </div>
    </div>
  </div>
</template>
<script>
  import {baseUrl} from '@/config/config'
  import 'swiper/dist/css/swiper.min.css'
  import Swiper from 'swiper/dist/js/swiper.min'
  import ProjectCard from '@/components/share/ProjectCard'

  export default {
    data () {
      return{
        employee: [],
        releasePro: [],
        baseUrl: baseUrl
      }
    },
    methods: {
      getRecommend () {
        this.$ajax(baseUrl + 'recommend')
          .then(res => {
            this.employee = res.data.employeeList
            this.releasePro = res.data.releaseProList
          }, res => {
            alert('获取数据失败，请检查网络')
          })
      }
    },
    beforeRouteEnter (to, from, next) {
      next(vm => {
        vm.$store.commit('changeSingerState', {stateName: 'myHeader', value: false})
        vm.getRecommend()
        window.onscroll = () => {
          if (document.documentElement.scrollTop >= 540) {
            vm.$store.commit('changeSingerState', {stateName: 'myHeader', value: true})
          } else {
            vm.$store.commit('changeSingerState', {stateName: 'myHeader', value: false})
          }
        }
      })
    },
    beforeRouteLeave (to, from, next) {
      window.onscroll = function () {}
      this.$store.commit('changeSingerState', {state: 'myHeader', value: true})
      next()
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
    },
    components: {
      ProjectCard
    }
  }
</script>
