<style lang="less" rel="stylesheet/less" scoped>
  @import '../css/theme.less';
  .employee-score{
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
  <div class="employee-score">
    <div>准时率: <br><input type="text" placeholder="0～100" v-model="onTime"></div>
    <div>信任度: <br><input type="text" placeholder="0～100" v-model="credit"></div>
    <div>优质比: <br><input type="text" placeholder="0～100" v-model="quality"></div>
    <div>评价专家: <br><textarea v-model="employeeEvaluate" name="" id="" cols="30" rows="5" placeholder="请给专家评价"></textarea></div>
    <span @click="submit">提交</span>
    <span @click="cancel">取消</span>
  </div>
</template>
<script>
  export default {
    data () {
      return {
        credit: '',
        quality: '',
        onTime: '',
        employeeEvaluate: ''
      }
    },
    methods: {
      submit () {
        this.$emit('submit', this.credit, this.quality, this.onTime, this.employeeEvaluate)
      },
      cancel () {
        this.$emit('showDialog', 'employeeDialog')
      }
    }
  }
</script>
