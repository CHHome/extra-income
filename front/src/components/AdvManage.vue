<style lang="less" rel="stylesheet/less" scoped>
  @import '../css/theme.less';
  .adv-manage{
    min-height: calc(100vh - 63px);
    background-color: #fff;
    padding-top: 30px;
    margin-left: 30px;
    img {
      width: 60px;
    }
  }
  .adv-img {
    display: none;
  }
</style>
<template>
  <div>
    <portrait v-if="showPortrait"
              :headSrc="reader"
              @next="next"
              @confirmHead="confirmHeadPic"></portrait>
    <input type="file" class="adv-img">
    <div class="adv-manage">
      <el-table
        :data="tableData"
        style="width: 100%">
        <el-table-column
          prop="num"
          label="广告序号"
          width="180">
        </el-table-column>
        <el-table-column
          prop="price"
          label="广告价格">
        </el-table-column>
        <el-table-column
          label="缩略图">
          <template slot-scope="scope">
            <img v-bind:src="baseUrl+ 'static/imgs/adv/' + scope.row.img" alt="">
          </template>
        </el-table-column>
        <el-table-column
          label="操作">
          <template slot-scope="scope">
            <el-button  @click="changeImg(scope.row.num)" type="text" size="small">更换</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
  import {baseUrl} from '@/config/config'
  import Portrait from '@/components/Portrait'

  export default {
    data () {
      return {
        tableData: [
          {
            num: 1,
            price: 20000,
            img: '1.jpeg'
          },
          {
            num: 2,
            price: 23000,
            img: '2.jpeg'
          },
          {
            num: 3,
            price: 15000,
            img: '3.jpeg'
          },
          {
            num: 4,
            price: 26000,
            img: '4.jpeg'
          },
          {
            num: 5,
            price: 60000,
            img: '5.jpeg'
          }
        ],
        baseUrl: baseUrl,
        reader: new FileReader(),
        showPortrait: false,
        currentNum: null
      }
    },

    components: {
      Portrait
    },

    mounted () {
      $('.adv-img').change( () => {
        this.reader.readAsDataURL($('.adv-img')[0].files[0])
        this.reader.addEventListener("load", () => {
          this.$store.commit('changeSingerState', {stateName: 'curtain', value: true})
          this.showPortrait = true
        }, false)
      })
    },

    methods: {
      changeImg(num) {
        this.currentNum = num
        $('.adv-img').click();
      },

      next(dialogName) {
        this[dialogName] = !this[dialogName]
        this.$store.commit('changeSinger', 'curtain')
      },

      confirmHeadPic(headSrc) {
        this.next('showPortrait')
        this.$ajax.post(this.baseUrl + 'changeAdv', {
          index: this.currentNum,
          img: headSrc.result.split(/;base64,/)[1]
        })
          .then(res => {
            if (res.data === 100001) {
              this.tableData[this.currentNum - 1].img += '?t=' + Math.random()
            } else {
              this.$notify.error({
                title: '错误',
                message: '更换广告失败',
                offset: 75
              })
            }
          }, res => {
            this.$notify.error({
              title: '错误',
              message: '网络连接失败',
              offset: 75
            })
          })
      }
    }
  }
</script>
