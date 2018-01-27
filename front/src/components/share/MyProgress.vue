<style scoped>
  .slider{
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
    <div class="slider">
      <span>{{label}}</span>
      <div class="pro-container">
        <div :class="[label, 'left']"></div>
      </div>
    </div>
</template>
<script>
  export default {
    props: ['value', 'label'],
    watch: {
      value () {
        $('.' + this.label).css('width', this.value + "%")
      }
    }
  }
</script>
