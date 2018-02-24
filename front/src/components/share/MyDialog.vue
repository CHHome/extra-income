<style lang="less" rel="stylesheet/less" scoped>
  @import '../../css/theme';
  .my-dialog{
    .my-dialog(30%);
    header{
      text-align: center;
      padding: 10px;
      padding-top: 0px;
      border-bottom: 1px solid #ccc;
      margin-bottom: 10px;
    }
  }
</style>
<template>
  <div class="my-dialog">
    <header>{{title}}</header>
    <slot></slot>
  </div>
</template>
<script>
  export default {
    props:['title']
  }
</script>
