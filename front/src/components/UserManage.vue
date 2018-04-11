<style lang="less" rel="stylesheet/less" scoped>
  @import '../css/theme.less';
  .user-manage{
    min-height: calc(100vh - 63px);
    background-color: #fff;
    padding-top: 30px;
    margin-left: 30px;
    img {
      width: 60px;
    }
  }
</style>
<template>
  <div class="user-manage">
    <el-radio v-model="nowSort" label="id">全部</el-radio>
    <el-radio v-model="nowSort" label="employerScore">雇主分排序</el-radio>
    <el-radio v-model="nowSort" label="totalScore">专家分排序</el-radio>
    <el-table
      :data="tableData"
      style="width: 100%">
      <el-table-column
        prop="registerTime"
        label="注册时间"
        width="180">
      </el-table-column>
      <el-table-column
        prop="userName"
        label="姓名">
      </el-table-column>
      <el-table-column
        prop="phone"
        label="手机">
      </el-table-column>
      <el-table-column
        prop="email"
        label="邮箱">
      </el-table-column>
      <el-table-column
        prop="gender"
        label="性别">
      </el-table-column>
      <el-table-column
        prop="employerScore"
        label="雇主分">
      </el-table-column>
      <el-table-column
        prop="totalScore"
        label="专家总评分">
      </el-table-column>
      <el-table-column
        prop="status"
        label="帐号状态">
      </el-table-column>
      <el-table-column
        label="头像">
        <template slot-scope="scope">
          <img v-bind:src="baseUrl+ 'static/imgs/' + scope.row.headImg" alt="">
        </template>
      </el-table-column>
      <el-table-column
        label="操作">
        <template slot-scope="scope">
          <el-button :disabled="scope.row.status !== '正常'" @click="handleUser(scope.row, 'lock')" type="text" size="small">冻结</el-button>
          <el-button :disabled="scope.row.status === '正常'" type="text" size="small" @click="handleUser(scope.row, 'unlock')">解冻</el-button>
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
        nowSort: 'id'
      }
    },
    watch: {
      nowSort () {
        this.currentPage = 1
        this.getData()
      }
    },
    mounted () {
      this.getData()
    },
    methods: {
      handleUser (data, type) {
        this.$ajax.get(baseUrl + 'handleUser', {
          params: {
            id: data.id,
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
        this.$ajax.get(baseUrl + 'showUsers', {
          params: {
            page: this.currentPage,
            sort: this.nowSort
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
