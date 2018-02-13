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
</style>
<template>
  <div class="more-release">
    <div>
      <header @click="selectProType">
        <span class="clicked">全部</span>
        <span>开发</span>
        <span>设计</span>
        <span>市场/运营</span>
        <span>产品</span>
      </header>
      <div class="more-release-container clearfix">
        <router-link
          v-for="item in showList"
          :to="{name: 'showReleasePro', params: {id: item.id}}">
          <project-card :item="item"></project-card>
        </router-link>
      </div>
      <div class="show-next-page" @nextPage>
        更多<i class="glyphicon glyphicon-plus"></i>
      </div>
    </div>
  </div>
</template>
<script>
  import {baseUrl} from '@/config/config'
  import ProjectCard from '@/components/share/ProjectCard'
  export default {
    mounted () {
      this.getPageData(this.nowType, this.allPage)
    },
    data () {
      return {
        allPage: 1,
        developerPage: 1,
        designPage: 1,
        marketPage: 1,
        productPage: 1,
        showList: [],
        nowType: '全部'
      }
    },
    methods: {
      getPageData (type, index) {
        this.$ajax.get(baseUrl + 'proPageQuery', {
          params: {
            index: index,
            type: type
          }
        }).then(res => {
          this.showList = res.data
        }, res => {
          alert('获取数据失败,请检查网络')
        })
      },
      selectProType (e) {
        if (e.target.nodeName === 'SPAN') {
          switch(e.target.textContent)
          {
            case '全部':
              this.getPageData('全部', this.allPage)
              break;
          }
        }
      },
      nextPage () {
      }
    },
    beforeRouteEnter (to, from, next) {
      next(vm => {
        window.onscroll = function () {}
        vm.$store.commit('changeSingerState', {stateName: 'myHeader', value: true})
      })
    },
    components: {
      ProjectCard
    }
  }
</script>
