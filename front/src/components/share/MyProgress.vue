<style scoped>
  .box{
    width:90%;
    margin: 60px auto;
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
    width: 90%;
    height: 7px;
    border-radius: 4px;
  }
</style>
<template>
  <div class="box">
    <div>
      <span>准时率</span>
      <div class="pro-container">
        <div class="left"></div>
      </div>
    </div>
    <div>
      <span>准时率</span>
      <div class="pro-container">
        <div class="left"></div>
      </div>
    </div>
    <div>
      <span>准时率</span>
      <div class="pro-container">
        <div class="left"></div>
      </div>
    </div>
  </div>
</template>
