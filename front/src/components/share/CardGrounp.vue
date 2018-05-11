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
      空数据!
    </div>
  </div>
</template>
<script>
  import {baseUrl} from '@/config/config'
  import ProjectCard from '@/components/share/ProjectCard'
  export default{
    props: {
      type: {
        type: String
      },
      keyWord: {
        type: String,
        default: ''
      }
    },
    data () {
      return{
        page: 1,
        showList: [],
        noneTip: false
      }
    },
    mounted () {
      this.getPageData()
    },
    methods: {
      search (keyWord) {
        this.getPageData(keyWord)
      },

      getPageData () {
        this.$ajax.get(baseUrl + 'proPageQuery', {
          params: {
            index: this.page,
            type: this.type,
            keyWord: this.keyWord
          }
        }).then(res => {
          if (this.showList.length  >= res.data.length) {
            this.$notify.success({
              title: '提示',
              message: '没有更多了哦',
              offset: 75
            })
          }
          this.showList = [...res.data]
          if (!this.showList.length) {
            this.noneTip = true
          } else {
            this.noneTip = false
          }
        }, res => {
          alert('获取数据失败,请检查网络')
        })
      },
      nextPage () {
        this.page++
        this.getPageData()
      }
    },
    components: {
      ProjectCard
    }
  }
</script>
