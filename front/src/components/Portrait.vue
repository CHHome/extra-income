<style lang="less" rel="stylesheet/less" scoped>
  @import '../css/theme.less';
  .submit-banner span{
    .btnTheme
  }
  #dialog {
    .my-dialog(35%);
    text-align: center;
    & > img {
      max-width: 200px;
      margin-bottom: 30px;
    }
  }
</style>
<template>
  <div id="dialog" class="col-sm-5">
    <img :src="headSrc.result">
    <div class="submit-banner">
      <span @click="submit">确定</span>
      <span @click="cancel">取消</span>
    </div>
  </div>
</template>
<script>
  import {baseUrl} from '@/config/config'
  import sha1 from 'js-sha1'
  export default {
    name: 'Login',
    props: ['headSrc'],
    data () {
      return {
        username: '',
        password: ''
      }
    },
    methods: {
      cancel () {
        this.$emit('next', 'showPortrait')
      },
      submit () {
        this.$emit('confirmHead', this.headSrc)
      }
    }
  }
</script>
