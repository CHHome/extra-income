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
        margin-left: -15px;
        margin-right: -15px;
        padding-bottom: 20px;
        padding-top: 20px;
        border-bottom: 1px solid #ccc;
        background-color: #fff;
        font-weight: 600;
        box-sizing: border-box;
        span{
          padding: 15px 8px 5px;
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
  .search {
    float: right;
    width: 280px;
    .el-input {
      width: 220px;
    }
    .search-submit {
      display: inline-block;
      width: 50px;
      height: 40px;
      padding: 10px 10px;
      background-color: #409EFF;
      vertical-align: top;
      color: #fff;
      cursor: pointer;
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
      <header @click="selectProType" class="title-header clearfix">
        <span class="clicked">全部</span>
        <span>开发</span>
        <span>设计</span>
        <span>市场/运营</span>
        <span>产品</span>
        <div class="search">
          <el-input v-model="keyWord" placeholder="请输入项目名称"></el-input><div class="search-submit" @click="doSearch">搜索</div>
        </div>
      </header>
      <transition name="type-fade">
        <card-grounp
          :type="'全部'"
          v-if="showAll"
          ref="showAll"
        ></card-grounp>
      </transition>
      <transition name="type-fade">
        <card-grounp
          :type="'开发'"
          v-if="showDeveloper"
          ref="showDeveloper"
        ></card-grounp>
      </transition>
      <transition name="type-fade">
        <card-grounp
          :type="'设计'"
          v-if="showDesign"
          ref="showDesign"
        ></card-grounp>
      </transition>
      <transition name="type-fade">
        <card-grounp
          :type="'市场/运营'"
          v-if="showMarket"
          ref="showMarket"
        ></card-grounp>
      </transition>
      <transition name="type-fade">
        <card-grounp
          :type="'产品'"
          v-if="showProject"
          ref="showProject"
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
        showProject: false,
        keyWord: '',
        type: 'showAll'
      }
    },
    methods: {
      selectProType(e) {
        if (e.target.nodeName === 'SPAN') {
          switch (e.target.textContent) {
            case '全部':
              this.reInit(e)
              this['showAll'] = true
              this.type = 'showAll'
              break;
            case '开发':
              this.reInit(e)
              this['showDeveloper'] = true
              this.type = 'showDeveloper'
              break;
            case '设计':
              this.reInit(e)
              this['showDesign'] = true
              this.type = 'showDesign'
              break;
            case '市场/运营':
              this.reInit(e)
              this['showMarket'] = true
              this.type = 'showMarket'
              break;
            case '产品':
              this.reInit(e)
              this['showProject'] = true
              this.type = 'showProject'
              break;
          }
        }
      },
      doSearch () {
        this.$refs[this.type].search(this.keyWord);
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
