<style lang="less" rel="stylesheet/less" scoped>
  @import '../css/theme.less';
  .pro-manage{
    min-height: calc(100vh - 63px);
    background-color: #fff;
    padding-top: 30px;
    margin-left: 30px;
  }
</style>
<template>
  <div class="pro-manage">
    <el-radio v-model="nowStatus" label="招募中">招募中</el-radio>
    <el-radio v-model="nowStatus" label="已冻结">已冻结</el-radio>
    <el-table
      :data="tableData"
      style="width: 100%">
      <el-table-column
        prop="releaseTime"
        label="发布时间"
        width="180">
      </el-table-column>
      <el-table-column
        prop="id"
        label="发布人">
      </el-table-column>
      <el-table-column
        prop="firstType"
        label="一级分类">
      </el-table-column>
      <el-table-column
        prop="secondType"
        label="二级分类">
      </el-table-column>
      <el-table-column
        prop="projectName"
        label="标题">
      </el-table-column>
      <el-table-column
        prop="budget"
        label="预算">
      </el-table-column>
      <el-table-column
        prop="cycle"
        label="项目周期">
      </el-table-column>
      <el-table-column
        prop="status"
        label="状态">
      </el-table-column>
      <el-table-column
        label="操作">
        <template slot-scope="scope">
          <el-button :disabled="scope.row.status !== '招募中'" @click="handlePro(scope.row, 'lock')" type="text" size="small">冻结</el-button>
          <el-button :disabled="scope.row.status === '招募中'" type="text" size="small" @click="handlePro(scope.row, 'unlock')">解冻</el-button>
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

  export default {
    data() {
      return {
        tableData: [],
        currentPage: 1,
        baseUrl: baseUrl,
        totalPage: 0,
        nowStatus: '招募中'
      }
    },
    mounted () {
      this.getData()
    },
    watch: {
      nowStatus () {
        this.getData()
      }
    },
    methods: {
      handlePro (data, type) {
        this.$ajax.get(baseUrl + 'handlePro', {
          params: {
            releaseId: data.id,
            type: type
          }
        })
          .then(res => {
            this.getData()
            this.$notify({
              title: '成功',
              message: '操作成功',
              offset: 75,
              type: 'success'
            })
          }, res => {
            this.$notify.error({
              title: '错误',
              message: '网络连接失败',
              offset: 75
            })
          })
      },
      getData () {
        this.$ajax.get(baseUrl + 'showPro', {
          params: {
            page: this.currentPage,
            status: this.nowStatus
          }
        })
          .then(res => {
            this.tableData = res.data.resultList
            this.totalPage = res.data.totalPage
          }, res => {
            this.$notify.error({
              title: '错误',
              message: '网络连接失败',
              offset: 75
            })
          })
      },
      currentChange (currentPage) {
        this.currentPage = currentPage
        this.getData()
      }
    }
  }
</script>
