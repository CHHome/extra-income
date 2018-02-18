<style lang="less" rel="stylesheet/less" scoped>
  @import '../css/theme';
  .projects-page{
    padding-top: 60px;
    & > div{
      background-color: #fff;
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
      .projects-container{
        padding: 30px 0;
        box-sizing: border-box;
      }
    }
  }
  .clicked{
    border-bottom: 2px solid @secondColor;
  }
</style>
<template>
  <div class="projects-page">
    <div>
      <header @click="selectType">
        <span data-type="releasing" class="clicked">发布中</span>
        <span data-type="applying">申请中</span>
        <span data-type="haveInHand">进行中</span>
        <span>已完成</span>
      </header>
      <div class="projects-container row">
        <router-link
          v-for="item in showList"
          :to="{name: linkTo, params: {id: item.id}}"
          :key="item.id">
          <project-card :item="item"></project-card>
        </router-link>
      </div>
    </div>
  </div>
</template>
<script>
  import ProjectCard from '@/components/share/ProjectCard'
  import {baseUrl} from '@/config/config'
  export default {
    data () {
      return {
        showList: [],
        linkTo: 'showReleasePro'
      }
    },
    beforeRouteEnter (to, from, next) {
      next(vm => {
        if (!vm.$store.state.hasLogin) {
          alert('请先登录')
          vm.$router.push({name: 'index'})
        }
        vm.getTypeData('myProjectData', 'releasing')
        window.onscroll = function () {}
        vm.$store.commit('changeSingerState', {stateName: 'myHeader', value: true})
      })
    },
    methods: {
      selectType (e) {
        if (e.target.nodeName === 'SPAN') {
          switch(e.target.getAttribute('data-type'))
          {
            case 'releasing':
              this.linkTo = 'showReleasePro'
              this.getTypeData('myProjectData', 'releasing')
              break;
            case 'applying':
              this.linkTo = 'showReleasePro'
              this.getTypeData('applyListShow', '申请中')
              break
            case 'haveInHand':
              this.linkTo = 'projectOrder'
              this.getTypeData('haveInHandListShow', '进行中')
              break
          }
        }
    },
      getTypeData (url, type) {
        if (this.$store.state.loginId) {
          this.$ajax.get(baseUrl + url, {
            params: {
              id: this.$store.state.loginId,
              type: type
            }
          })
            .then(res => {
              this.showList = res.data
            }, res => {
              alert('获取数据失败，请检查网络')
            })
        }
      }
    },
    components: {
      ProjectCard
    }
  }
</script>

