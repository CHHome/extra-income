<style scoped>
  .box{
    width:90%;
    margin: 0 auto;
  }
  .box > div{
    display: flex;
    justify-content: flex-start;
    align-items: center;
    font-weight: 600;
    font-size: 13px;
    color: #000;
    margin-bottom: 15px;
  }
  .pro-container{
    border-radius: 4px;
    height:7px;
    background-color: rgba(0,0,0,0.49);
    width: 70%;
    margin-left: 8px;
    opacity: 0.65;
  }
  .pro-container .left{
    background-color: #00ffb9;
    height: 7px;
    border-radius: 4px;
  }
</style>
<template>
  <div class="box">
    <div>
      <span>准时率</span>
      <div class="pro-container">
        <div class="left on-time"></div>
      </div>
    </div>
    <div>
      <span>高质比</span>
      <div class="pro-container">
        <div class="left quality"></div>
      </div>
    </div>
    <div>
      <span>信用度</span>
      <div class="pro-container">
        <div class="left credit"></div>
      </div>
    </div>
  </div>
</template>
<script>
  export default {
    props: ['on_time', 'credit', 'quality'],
    computed: {
      time () {
        return this.on_time + '%'
      }
    },
    watch: {
      on_time () {
        $('.on-time').css('width', this.on_time + '%')
      },
      credit () {
        $('.credit').css('width', this.credit + '%')
      },
      quality () {
        $('.quality').css('width', this.quality + '%')
      }
    }
  }
</script>
