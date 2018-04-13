<style lang="less" rel="stylesheet/less" scoped>
  @import '../css/theme.less';
  header{
    font-weight: 600;
    font-size: 14px;
    padding: 30px;
  }
  .user-manage{
    min-height: calc(100vh - 63px);
    background-color: #fff;
    padding-top: 30px;
    margin-left: 30px;
    img {
      width: 60px;
    }
    .show-release-container{
      width: 100%;
    }
    .content{
      padding: 60px;
    }
    .order-progress{
      overflow: hidden;
      text-align: center;
      & > div{
        display: inline-block;
        width: 100%;
        div {
          margin-top: 30px;
        }
      }
      & > span{
        .btnTheme;
        margin-top: 25px;
      }
      .progress-block {
        display: inline-block;
        width: 40%;
        box-sizing: border-box;
      }
    }
    .submit-record header{
      text-align: center;
    }
  }
</style>
<template>
  <div class="user-manage">
    <el-dialog
      title="裁决申诉"
      :visible.sync="desideDialog"
      :fullscreen="true"
      :before-close="handleClose">
      <div class="content">
        <release-info :data="currentDialogData"></release-info>
        <div class="order-progress">
          <header>项目进度</header>
          <div>
            <div class="progress-block">
              <el-progress type="circle" :percentage="orderData.progress" color="#8e71c7" :width="180" ></el-progress>
              <div>提交进度</div>
            </div>
            <div class="progress-block">
              <el-progress type="circle" :percentage="orderData.hasComplete" :color="progressColor" :width="180" ></el-progress>
              <div>时间进度</div>
            </div>
          </div>
        </div>
        <div class="submit-record">
          <header>提交记录</header>
          <el-table
            :data="updateLists"
            style="width: 100%">
            <el-table-column
              fixed
              prop="updateTime"
              label="日期">
            </el-table-column>
            <el-table-column
              prop="title"
              label="标题">
            </el-table-column>
            <el-table-column
              prop="desc"
              label="内容描述">
            </el-table-column>
            <el-table-column
              prop="progress"
              label="目标进度">
            </el-table-column>
            <el-table-column
              label="提交文件">
              <template slot-scope="scope">
                <a :href="baseUrl +'static/' + scope.row.fileDir">{{scope.row.fileDir}}</a>
              </template>
            </el-table-column>
            <el-table-column
              label="拒收理由"
              prop="rejectReason"
              width="180">
            </el-table-column>
          </el-table>
        </div>
      </div>
      <span slot="footer" class="dialog-footer">
    <el-button @click="desideDialog = false">取 消</el-button>
    <el-button type="primary" @click="desideDialog = false">确 定</el-button>
    </span>
    </el-dialog>

    <el-table
      :data="tableData"
      style="width: 100%">
      <el-table-column
        prop="beginTime"
        label="申诉时间"
        width="180">
      </el-table-column>
      <el-table-column
        prop="complainant.userName"
        label="原告">
      </el-table-column>
      <el-table-column
        prop="defendanter.userName"
        label="被告">
      </el-table-column>
      <el-table-column
        prop="orderId"
        label="订单ID">
      </el-table-column>
      <el-table-column
        prop="reason"
        label="申诉理由">
      </el-table-column>
      <el-table-column
        prop="status"
        label="状态">
      </el-table-column>
      <el-table-column
        label="操作">
        <template slot-scope="scope">
          <el-button  @click="handleAppeal(scope.row)" type="text" size="small">裁决</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-pagination
      layout="prev, pager, next"
      :page-count="Math.ceil(totalPage/3)"
      :current-page="currentPage"
      @current-change="currentChange">
    </el-pagination>
  </div>
</template>
<script>
  import {baseUrl} from '@/config/config'
  import ReleaseInfo from '@/components/share/ReleaseInfo'

  export default {
    data () {
      return {
        currentPage: 1,
        type: '处理中',
        tableData: [],
        totalPage: 1,
        desideDialog: false,
        currentDialogData: {}, //todo 项目信息
        orderData: {},  // 订单信息
        updateLists: [],
        baseUrl: baseUrl,
        progressColor: ''

      }
    },
    components: {
      ReleaseInfo
    },

    mounted () {
      this.getData();
    },

    methods : {
      parseOrderData (data) {
        this.orderData = data
        let beginTime = new Date(data.beginTime.replace(/-/g,'/')).getTime()
        let deadlineTime = new Date(data.deadlineTime.replace(/-/g,'/')).getTime()
        this.orderData.hasComplete = parseInt((new Date().getTime() - beginTime)/(deadlineTime - beginTime) * 100);
        if (this.orderData.hasComplete >= 100) {
          this.orderData.hasComplete = 100
        } else {
          this.orderData.hasComplete = this.orderData.hasComplete.toFixed(2)
        }
        switch (this.orderData.status) {
          case '进行中':
            this.progressColor = '#8e71c7'
            break

          case '已完成':
            this.progressColor = '#0AAD38'
            break

          case '已逾期':
            this.progressColor = '#AD120F'
            break

          default:
            this.progressColor = '#8e71c7'

        }
      },
      handleClose(done) {
        this.$confirm('确认关闭？')
          .then(_ => {
            done();
          })
          .catch(_ => {});
      },
      currentChange (currentPage) {
        this.currentPage = currentPage
        this.getData()
      },
      handleAppeal (row) {
        this.desideDialog = true;
        this.currentDialogData = row.releasePro
        this.updateLists = row.updateLists
        console.log( this.updateLists)
        this.parseOrderData(row.proOrder)
      },
      getData () {
        this.$ajax.get(baseUrl + 'showAppeals', {
          params: {
            page: this.currentPage,
            type: this.type
          }
        })
          .then(res => {
            this.tableData = res.data.resultList
            this.totalPage = res.data.totalPage
          })
      }
    }
  }
</script>

