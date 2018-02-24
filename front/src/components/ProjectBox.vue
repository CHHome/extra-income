<style lang="less" rel="stylesheet/less" scoped>
  @import '../css/theme.less';
  .pro-container>div{
    margin: 30px auto;
    &:nth-child(1){
      width:70%;
      position: relative;
       min-height: 200px;
      &>img{
        display: none;
        z-index: 10000;
        width: 100%;
      }
      &>input{
        display: none;
      }
     }
    .first{
      &:before{
        content: "";
        position: absolute;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        background: rgba(0,0,0,.5) url(../assets/camera.png) center center no-repeat;
        cursor: pointer;
      }
      &>span{
        position: relative;
        top:150px;
      }
    }
  }
  .pro-info{
    & > div{
      width: 50%;
      margin: 20px auto;
      min-width: 260px;
      text-align: left;
      input, textarea{
        width:100%;
        height: 40px;
      }
      textarea{
        height:125px
      }
    }
  }
  .add-to-list{
    span{
      .btnTheme
    }
  }
  .error{
    input{
      border: 1px solid red;
    }
    span{
      color:red;
    }
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
    <div class="pro-info">
      <div :class="{error:$v.proName.$error }">
        <label for="proname">作品名称</label><br>
        <input type="text" id="proname" v-model="proName" @input="$v.proName.$touch()">
        <span v-if="$v.proName.$error">项目名是必须的</span>
      </div>
      <div :class="{error:$v.player.$error }">
        <label for="player">职责</label><br>
        <input type="text" id="player" v-model="player" @input="$v.player.$touch()">
        <span v-if="$v.player.$error">职责是必须的</span>
      </div>
      <div :class="{error:$v.industry.$error }">
        <label for="industry">行业</label><br>
        <input type="text" id="industry" v-model="industry" @input="$v.industry.$touch()">
        <span v-if="$v.industry.$error">行业是必须的</span>
      </div>
      <div>
        <label for="linkto">作品链接</label><br>
        <input type="text" id="linkto">
      </div>
      <div>
        <label for="describe">作品描述</label><br>
        <textarea id="describe" placeholder="请描述作品/案例"></textarea>
      </div>
    </div>
    <div class="add-to-list">
      <span @click="addToList">添加</span>
      <span @click="cancel">取消</span>
    </div>
  </div>
</template>
<script>
  import {required} from 'vuelidate/lib/validators'
  export default {
    data () {
      return {
        imgUrl: '',
        proName: '',
        player: '',
        industry:''

      }
    },
    validations: {
      proName: {
        required
      },
      player: {
        required
      },
      industry: {
        required
      },
      validationGroup: ['proName', 'player', 'industry']
    }
    ,
    mounted () {
      $('.pro-container>div:nth-child(1)>input').bind('change', () => {
        let reader = new FileReader()
        reader.onload = () => {
          $('.pro-container>div:nth-child(1)>img')[0].style.display = 'inline-block'
          $('.pro-container>div:nth-child(1)>img')[0].src = reader.result
          this.imgUrl = reader.result
          $('.first')[0].style.display = 'none'
        }
        reader.readAsDataURL($('.pro-container>div:nth-child(1)>input')[0].files[0])
      })
    },
    methods: {
      selectImg () {
        $('.pro-container>div:nth-child(1)>input').click()
      },
      cancel () {
        this.$emit('proCancle')
      },
      addToList () {
        if (this.$v.validationGroup.$invalid) {
          this.$v.proName.$touch()
          this.$v.industry.$touch()
          this.$v.player.$touch()
          return
        }
        let obj = {}
        obj.imgData = this.imgUrl
        obj.proName = this.proName
        obj.player = this.player
        obj.industry = this.industry
        obj.linkTo = document.getElementById('linkto').value
        obj.describe = document.getElementById('describe').value
        this.$emit('confirmPro', obj)
      }
    }
  }
</script>
