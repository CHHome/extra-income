<style lang="less" rel="stylesheet/less" scoped>
  @import '../css/theme';
  .more-release{
    padding-top: 60px;
    & > div{
      width:90%;
      padding: 10px 15px;
      margin: 0 auto;
      margin-top: 60px;
      border-radius: 4px;
      & > header{
        padding-bottom: 20px;
        border-bottom: 1px solid #ccc;
        font-weight: 600;
        box-sizing: border-box;
        span{
          padding: 15px 8px;
          cursor: pointer;
        }
      }
      .more-release-container{
        background-color: #fff;
        padding-top: 30px;
        box-sizing: border-box;
      }
      .show-next-page{
        text-align: center;
        padding: 8px;
        margin: 0 auto;
        background-color: @secondColor;
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
            color: #fff;
          }
        }
      }
    }
  }
  .clicked{
    border-bottom: 2px solid @secondColor;
  }
  .type-fade-enter-active, .type-fade-leave-active {
    transition: all 1.5s ease;
  }
  .type-fade-enter{
    opacity: 0;
    transform: translateX(300px);
  }
  .type-fade-leave{
    opacity: 0;
    transform: translateY(300px);
  }
</style>
<template>
  <div class="more-release">
    <div>
      <header @click="selectProType" class="title-header">
        <span class="clicked">全部</span>
        <span>开发</span>
        <span>设计</span>
        <span>市场/运营</span>
        <span>产品</span>
      </header>
      <transition name="type-fade">
        <card-grounp
          :type="'全部'"
          v-show="showAll"
        ></card-grounp>
      </transition>
      <transition name="type-fade">
        <card-grounp
          :type="'开发'"
          v-show="showDeveloper"
        ></card-grounp>
      </transition>
      <transition name="type-fade">
        <card-grounp
          :type="'设计'"
          v-show="showDesign"
        ></card-grounp>
      </transition>
      <transition name="type-fade">
        <card-grounp
          :type="'市场/运营'"
          v-show="showMarket"
        ></card-grounp>
      </transition>
      <transition name="type-fade">
        <card-grounp
          :type="'产品'"
          v-show="showProject"
        ></card-grounp>
      </transition>
    </div>
  </div>
</template>
<script>
  import {baseUrl} from '@/config/config'
  import ProjectCard from '@/components/share/ProjectCard'
  import CardGrounp from '@/components/share/CardGrounp'
  export default {
    data () {
      return {
        showAll: true,
        showDeveloper: false,
        showMarket: false,
        showDesign: false,
        showProject: false
      }
    },
    methods: {
      selectProType(e) {
        if (e.target.nodeName === 'SPAN') {
          switch (e.target.textContent) {
            case '全部':
              this.reInit(e)
              this['showAll'] = true
              break;
            case '开发':
              this.reInit(e)
              this['showDeveloper'] = true
              break;
            case '设计':
              this.reInit(e)
              this['showDesign'] = true
              break;
            case '市场/运营':
              this.reInit(e)
              this['showMarket'] = true
              break;
            case '产品':
              this.reInit(e)
              this['showProject'] = true
              break;
          }
        }
      },
      reInit (e) {
        $('.title-header span').removeClass('clicked')
        e.target.classList.add('clicked')
        this.showAll = this.showDesign = this.showDeveloper = this.showMarket = this.showProject = false
      }
    },
    beforeRouteEnter (to, from, next) {
      next(vm => {
        vm.$store.commit('changeSingerState', {stateName: 'myHeader', value: true})
      })
    },
    components: {
      CardGrounp
    }
  }
</script>
