<style lang="less" rel="stylesheet/less" scoped>
  @import '../css/theme.less';
  .release{
    padding-top: 60px;
    text-align: center;
    height: 500px;
    img{
      width: 100%;
    }
    & > div, & > img{
      margin-bottom: 60px;
    }
    .release-form{
      margin: auto;
      width:70%;
      background-color: #fff;
      min-width: 300px;
      padding: 10px;
      & > div{
        text-align: left;
        margin: 30px auto;
        width: 50%;
        min-width: 280px;
        i{
          color: red;
        }
        .select-first{
          display: flex;
          justify-content: space-between;
          input{
            display: none;
          }
          span{
            text-align: center;
            display: inline-block;
            width: 23%;
            padding: 10px 8px;
            border:1px solid #dce0e0;
            cursor: pointer;
            &:hover{
             .first-type-click
            }
          }
        }
        & > div {
          margin-top: 10px;
        }
        &:nth-last-child(1){
          span{
            .btnTheme
          }
          text-align: center;
        }
      }
    }
  }
  .first-type-click{
    background-color: @secondColor;
    color: #fff;
    font-size: 16px;
  }
  select, input, textarea{
    width: 100%;
    height: 50px;
    background-color: #fff;
  }
  textarea{
    height:125px
  }
  .validator-error{
    color: red;
  }
  .error{
    border: 1px solid red;
  }
</style>
<template>
  <div class="release">
    <img src="../assets/releaseBanner.jpg" alt="banner">
    <div class="release-form">
      <div>
        <span>请选择项目一级类型<i>*</i></span>
        <div @click="selectFirst" class="select-first" :class="{error:$v.firstType.$error }">
          <span data-type="developer">开发</span>
          <span data-type="design">设计</span>
          <span data-type="market">市场/运营</span>
          <span data-type="product">产品</span>
          <input type="text" v-model="firstType" @input="$v.firstType.$touch()">
        </div>
        <span v-if="$v.firstType.$error" class="validator-error">项目一级类型必须的</span>
      </div>
      <div>
        <span>请选择项的二级类型<i>*</i></span>
        <div :class="{error:$v.secondType.$error }">
          <select v-model="secondType" @change="$v.firstType.$touch()">
            <option disabled>{{selectTip}}</option>
            <option v-for="item in secondList">{{item}}</option>
          </select>
        </div>
        <span v-if="$v.secondType.$error" class="validator-error">项目二级类型必须的</span>
      </div>
      <div>
        <span>项目名称<i>*</i></span>
        <div :class="{error:$v.projectName.$error }">
          <input type="text" placeholder="给项目取个名字" v-model="projectName" @input="$v.projectName.$touch()">
        </div>
        <span v-if="$v.projectName.$error && !$v.projectName.required" class="validator-error">项目名称必须的</span>
        <span v-if="!$v.projectName.maxLength" class="validator-error">长度为1-30</span>
      </div>
      <div>
        <span>项目描述<i>*</i></span>
        <div :class="{error:$v.describe.$error }">
          <textarea v-model="describe" placeholder="请描述作品/案例" @input="$v.describe.$touch()"></textarea>
        </div>
        <span v-if="$v.describe.$error && !$v.describe.required" class="validator-error">项目描述必须的</span>
        <span v-if="!$v.describe.maxLength" class="validator-error">长度为1-500</span>
      </div>
      <div>
        <span>项目预算<i>*</i></span>
        <div :class="{error:$v.budget.$error }">
          <input type="text" placeholder="项目预算单位为：元" v-model="budget" @input="$v.budget.$touch()">
        </div>
        <span v-if="$v.budget.$error && !$v.budget.required" class="validator-error">项目预算必须的</span>
        <span v-if="!$v.budget.numeric" class="validator-error">项目预算必须为数字</span>
      </div>
      <div>
        <span>项目周期<i>*</i></span>
        <div :class="{error:$v.cycle.$error }">
          <input type="text" placeholder="项目周期请以天为单位" v-model="cycle" @input="$v.cycle.$touch()">
        </div>
        <span v-if="!$v.cycle.required && $v.cycle.$error" class="validator-error">项目周期必须的</span>
        <span v-if="!$v.cycle.numeric" class="validator-error">项目周期必须为数字</span>
      </div>
      <div>
        <span>公司</span>
        <div :class="{error:$v.company.$error }">
          <input type="text" v-model="company" @input="$v.company.$touch()">
        </div>
        <span v-if="!$v.company.maxLength" class="validator-error">长度为1-30</span>
      </div>
      <div>
        <span @click="submit">发布项目</span>
      </div>
    </div>
  </div>
</template>
<script>
  import {baseUrl} from '@/config/config'
  import {category} from '@/js/webData'
  import {required, maxLength, numeric} from 'vuelidate/lib/validators'
  export default {
    data () {
      return {
        category: '',
        firstType: '',
        secondType: '',
        selectTip: '请先选择项目一级类型',
        secondList: [],
        projectName: '',
        describe: '',
        budget: '',
        cycle: '',
        company: ''
      }
    },
    methods: {
      selectFirst (e) {
        this.selectTip = '请选择'
        $('.select-first > span').removeClass('first-type-click')
        this.secondType = ''
        if (e.target.nodeName === 'SPAN') {
          $(e.target).addClass('first-type-click')
          this.category = e.target.getAttribute('data-type')
          this.firstType = e.target.textContent
          this.secondList = category[this.category]
        }
      },
      submit () {
        if (this.$v.validationGroup.$invalid) {
          this.$v.firstType.$touch()
          this.$v.secondType.$touch()
          this.$v.projectName.$touch()
          this.$v.describe.$touch()
          this.$v.budget.$touch()
          this.$v.cycle.$touch()
          this.$v.company.$touch()
          return
        }
        let store = window.localStorage
        let userId = store['token'].split('-')[0]
        this.$http.post(baseUrl + 'releaseSave', {
          userId: userId,
          projectName: this.projectName,
          firstType: this.firstType,
          secondType: this.secondType,
          describe: this.describe,
          budget: this.budget,
          cycle: this.cycle,
          company: this.company
        })
          .then(res => {
          }, res => {
            alert('发布失败，请检查网络')
          })
      }
    },
    validations: {
      firstType: {
        required
      },
      secondType: {
        required,
      },
      projectName: {
        required,
        maxLength: maxLength(30),
      },
      describe: {
        required,
        maxLength: maxLength(500)
      },
      budget: {
        required,
        numeric
      },
      cycle: {
        required,
        numeric
      },
      company: {
        maxLength: maxLength(30)
      },
      validationGroup: ['firstType', 'secondType', 'projectName', 'describe', 'budget', 'cycle', 'company']

    },
    beforeRouteEnter (to, from, next) {
      next(vm => {
        if (!vm.$store.state.hasLogin) {
          vm.$router.push({name: 'index'})
        }
        window.onscroll = function () {}
        vm.$store.commit('changeSingerState', {stateName: 'myHeader', value: true})
      })
    },
  }
</script>
