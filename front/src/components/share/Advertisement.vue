<style lang="less" rel="stylesheet/less" scoped>
  @import '../../css/theme';
  .advertisement {
    position: fixed;
    right: 0;
    bottom: 0;
    max-width:330px;
    max-height: 330px;
    z-index: 1000000;
    cursor: pointer;
    img {
      width: 100%;
    }
  }
  .el-icon-close {
    position: absolute;
    right: 0;
    top:0;
    font-size: 16px;
  }
  .adv-text {
    padding: 1px 2px;
    position: absolute;
    right: 0;
    bottom: 0;
    background-color: rgba(18,16,4,0.94);
    opacity: 0.3;
    color: #fff;
  }
</style>
<template>
  <div class="advertisement">
    <span class="el-icon-close" @click="show = false"></span>
    <span class="adv-text">广告</span>
    <img :src="baseUrl + 'static/' + 'imgs/adv/' + currentAdv + '.jpeg'" alt="广告" v-if="show">
  </div>
</template>

<script>
  import {baseUrl} from '@/config/config'
  export  default{
    data () {
      return {
        show: true,
        baseUrl: baseUrl,
        currentAdv: 1
      }
    },

    mounted () {
      this.currentAdv = 1 + Math.floor(Math.random()*5);
    }
  }
</script>
