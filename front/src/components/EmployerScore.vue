<style lang="less" rel="stylesheet/less" scoped>
  @import '../css/theme.less';
  .employer-score{
    div{
      margin-bottom: 10px;
      textarea{
        width: 100%;
      }
    }
    span{
      .btnTheme
    }
  }
</style>
<template>
  <div class="employer-score">
    <div>雇主分数: <br><input type="text" placeholder="0～100" v-model="score"></div>
    <div>评价雇主: <br><textarea v-model="employerEvaluate" name="" id="" cols="30" rows="5" placeholder="请给雇主评价"></textarea></div>
    <span @click="submit">提交</span>
    <span @click="cancel">取消</span>
  </div>
</template>
<script>
  export default {
    data () {
      return{
        score: '',
        employerEvaluate: ''
      }
    },
    methods: {
      cancel () {
        this.$emit('showDialog', 'employerDialog')
      },
      submit () {
        this.$emit('submit', this.score, this.employerEvaluate)
      }
    }
  }
</script>
