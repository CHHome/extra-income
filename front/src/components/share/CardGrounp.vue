<style lang="less" rel="stylesheet/less" scoped>
  @import '../../css/theme';
  .more-release-container{
    background-color: #fff;
    padding-top: 30px;
    box-sizing: border-box;
    .show-next-page{
      text-align: center;
      clear: both;
      padding: 15px 10px;
      cursor: pointer;
      &:hover{
        color: @secondColor;
      }
      i{
        margin-left: 8px;
        font-size: 12px;
      }
    }
  }
</style>

<template>
  <div class="more-release-container clearfix row">
    <router-link
      v-for="item in showList"
      :to="{name: 'showReleasePro', params: {id: item.id}}">
      <project-card :item="item"></project-card>
    </router-link>
    <div class="show-next-page" @click="nextPage" v-if="!noneTip">
    更多<i class="glyphicon glyphicon-plus"></i>
    </div>
    <div class="show-next-page" v-if="noneTip">
      客官，我是有底线的
    </div>
  </div>
</template>
<script>
  import {baseUrl} from '@/config/config'
  import ProjectCard from '@/components/share/ProjectCard'
  export default{
    props: ['type'],
    data () {
      return{
        page: 1,
        showList: [],
        noneTip: false
      }
    },
    mounted () {
      this.getPageData(this.type, this.page)
    },
    methods: {
      getPageData (type, index) {
        this.$ajax.get(baseUrl + 'proPageQuery', {
          params: {
            index: index,
            type: type
          }
        }).then(res => {
          if (res.data.length !== 0) {
            this.showList = [...this.showList, ...res.data]
          } else {
            this.noneTip = true
          }
        }, res => {
          alert('获取数据失败,请检查网络')
        })
      },
      nextPage () {
        this.page++
        this.getPageData(this.type, this.page)
      }
    },
    components: {
      ProjectCard
    }
  }
</script>
