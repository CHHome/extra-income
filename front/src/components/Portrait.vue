<style scoped>
  .submit-banner span{
    border-style: none;
    line-height: 32px;
    padding: 0 32px;
    background-image: linear-gradient(-133deg,#00ffb9,#ACFFEC);
    border-radius: 16px;
    font-family: PingFangSC-Regular;
    font-size: 14px;
    color: #000;
    letter-spacing: 0;
    display: inline-block;
    cursor: pointer;
    margin-right: 10px;
  }
  #dialog > img {
    max-width: 200px;
    margin-bottom: 30px;
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
        this.$store.commit('changeSinger', 'showPortrait')
        this.$store.commit('changeSinger', 'curtain')
      },
      submit () {
        this.$emit('confirmHead', this.headSrc)
      }
    }
  }
</script>
<style scoped>
  #dialog{
    position: fixed;
    top: 25%;
    left: calc(50% - 17.5%);
    background-color: #fff;
    width: 35%;
    padding: 30px;
    box-shadow: 0 0 10px #cdcdcd;
    z-index: 10001;
    opacity: 1;
    border-radius: 4px;
  }
  .dialog div > div,.dialog div >input{
    border-style: none;
    line-height: 32px;
    padding: 0 32px;
    background-image: linear-gradient(-133deg,#004cfb,#85a1e1);
    border-radius: 16px;
    font-family: PingFangSC-Regular;
    font-size: 14px;
    color: #fff;
    letter-spacing: 0;
    display: inline-block;
    cursor: pointer;
  }
</style>
