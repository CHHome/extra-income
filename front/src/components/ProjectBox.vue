<style scoped>
  .pro-container>div{
    margin: 30px auto;
  }
  .pro-container>div:nth-child(1){
    width:70%;
    position: relative;
    min-height: 200px;
  }
  .first:before{
    content: "";
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,.5) url(//static.lagou.com/www/static/account-c/modules/userinfo/img/camera_8d64bc7.png) center center no-repeat;
    cursor: pointer;
  }
  .first>span{
    position: relative;
    top:150px;
  }
  .pro-container>div:nth-child(1)>img{
    display: none;
    z-index: 10000;
    width: 100%;
  }
  .pro-container>div:nth-child(1)>input{
    display: none;
  }
</style>
<template>
  <div class="pro-container">
    <div @click="selectImg">
      <img alt="案例图片">
      <div class="first">
        <span>上传案例图片</span>
      </div>
      <input type="file">
    </div>
  </div>
</template>
<script>
  export default {
    data () {
      return {}
    },
    mounted () {
      $('.pro-container>div:nth-child(1)>input').bind('change', () => {
        let reader = new FileReader()
        reader.onload = () => {
          $('.pro-container>div:nth-child(1)>img')[0].style.display = 'inline-block'
          $('.pro-container>div:nth-child(1)>img')[0].src = reader.result
          $('.first')[0].style.display = 'none'
        }
        reader.readAsDataURL($('.pro-container>div:nth-child(1)>input')[0].files[0])
      })
    },
    methods: {
      selectImg () {
        $('.pro-container>div:nth-child(1)>input').click()
      }
    }
  }
</script>
