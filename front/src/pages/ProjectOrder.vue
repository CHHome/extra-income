<style lang="less" rel="stylesheet/less" scoped>
  @import '../css/theme.less';
  .project-order{
    padding-top: 60px;
    img{
      width: 100%;
    }
    & > div, & > img{
      margin: 30px auto;
    }
    & > div{
      header{
        font-size: 16px;
        font-weight: 600;
        padding: 30px;
      }
      background-color: #fff;
      width: 90%;
      .participants{
       display: inline-block;
        & > div{
          width: 300px;
          margin: 0 auto;
          display: inline-block;
          border: 1px solid #ccc;
        }
      }
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
  }
  .el-dialog__wrapper .el-upload {
    display: none;
  }
  .upload-demo {
    text-align: left;
    input[type="file"]{
      display: none;
    }
  }
  .el-table .pending {
    background: oldlace;
  }
  .el-table .accept {
    background: #f0f9eb;
  }
  .el-table .reject {
    background: rgba(173,44,42,0.94);
  }
</style>
<template>
  <div class="project-order">
    <div v-if="employerDialog">
      <my-dialog :title="'给雇主评分'">
        <employer-score
          @showDialog="showDialog"
        @submit="submitProgress"></employer-score>
      </my-dialog>
    </div>
    <div v-if="employeeDialog">
      <my-dialog :title="'给专家评分'">
        <employee-score
          @showDialog="showDialog"
          @submit="submitComplete"></employee-score>
      </my-dialog>
    </div>
    <img src="../assets/releaseBanner.jpg" alt="banner">
    <release-info
      :data="releaseProData"
      v-if="!showModify">
      <!--运用slot实现实现组件的复用，防止组件强依赖-->
      <i slot="icon"
         class="glyphicon glyphicon-pencil"
         title="修改"
         @click="modify"
         v-if="modifyIcon"></i>
    </release-info>
    <release-form
      :type="'showReleasePro'"
      v-if="showModify"
      @cancelModify="modify"
      :itemData="releaseProData"></release-form>
    <div class="participant-info">
      <header>参与者信息</header>
      <div class="participants clearfix">
        <div v-for="item in Object.keys(participantInfo)">
          <apply-card :item="participantInfo[item]" ></apply-card>
        </div>
      </div>
    </div>
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
        <div>
          <el-dialog
            title="提示"
            :visible.sync="employerSubmit"
            width="30%"
            :before-close="handleClose"
            append-to-body>
            <span>进度已达100%，通过将结束项目， 确定验收通过?</span>
            <span slot="footer" class="dialog-footer">
            <el-button @click="employerSubmit = false">取 消</el-button>
            <el-button type="primary" @click="employerConfirm">确 定</el-button>
            </span>
          </el-dialog>
          <el-dialog
            title="发起申诉"
            :visible.sync="appealDialog"
            width="45%"
            :before-close="handleClose">
            <el-alert
              center
              title="警告"
              type="warning"
              description="申诉的项目将被冻结，且不可恢复，详情请阅读服务指南"
              show-icon>
            </el-alert>
            <el-input
              type="textarea"
              :autosize="{ minRows: 4, maxRows: 8}"
              placeholder="请输入申诉理由"
              v-model="appealReason">
            </el-input>
            <span slot="footer" class="dialog-footer">
            <el-button @click="appealDialog = false">取 消</el-button>
            <el-button type="primary" @click="sendAppeal">确 定</el-button>
            </span>
          </el-dialog>
          <el-popover
            ref="updatePopover"
            title="提交记录"
            placement="top"
            width="1082"
            trigger="click">
            <el-table
              v-loading="updateLoading"
              :data="fileList"
              :row-class-name="tableRowClassName"
              style="width: 100%">
              <el-table-column
                fixed
                prop="updateTime"
                label="日期"
                width="100">
              </el-table-column>
              <el-table-column
                prop="title"
                label="标题"
                width="120">
              </el-table-column>
              <el-table-column
                prop="desc"
                label="内容描述"
                width="350">
              </el-table-column>
              <el-table-column
                prop="currentProgress"
                label="当前进度"
                width="100">
              </el-table-column>
              <el-table-column
                prop="progress"
                label="目标进度"
                width="100">
              </el-table-column>
              <el-table-column
                label="提交文件"
                width="180">
                <template slot-scope="scope">
                  <a :href="baseUrl +'static/' + scope.row.fileDir">{{scope.row.fileName}}</a>
                </template>
              </el-table-column>
              <el-table-column
                label="拒收理由"
                prop="rejectReason"
                width="180"
                v-if="!modifyIcon">
              </el-table-column>
              <el-table-column
                fixed="right"
                :label="modifyIcon ? '操作' : '状态'"
                width="100">
                <template slot-scope="scope">
                  <div v-if="modifyIcon && scope.row.status === 'pending'">
                    <el-button @click="handleClick(scope.row, 1)" type="text" size="small">通过</el-button>
                    <el-dialog
                      title="提示"
                      :visible.sync="rejectDialog"
                      width="30%"
                      :modal="false"
                      :before-close="handleClose">
                      <el-input
                        type="textarea"
                        :autosize="{ minRows: 2, maxRows: 4}"
                        placeholder="请输入拒绝理由"
                        v-model="rejectReason">
                      </el-input>
                          <span slot="footer" class="dialog-footer">
                          <el-button @click="rejectDialog = false">取 消</el-button>
                          <el-button type="primary" @click="handleClick(scope.row, 0, {reason: rejectReason})">确 定</el-button>
                          </span>
                    </el-dialog>
                    <el-button  @click="rejectDialog = true" type="text">拒收</el-button>
                  </div>
                  <div v-if="!modifyIcon && scope.row.status === 'pending'">
                    <el-button type="warning" size="mini">等待验收</el-button>
                  </div>
                  <div v-if="scope.row.status === 'accept'">

                    <el-button type="success" size="mini">已通过</el-button>
                  </div>
                  <div v-if="scope.row.status === 'reject'">
                    <el-button type="danger" size="mini">已拒收</el-button>
                  </div>
                </template>
              </el-table-column>
            </el-table>
          </el-popover>
          <el-button type="primary" round v-popover:updatePopover @click="showFiles">提交记录</el-button>
          <el-button type="primary" round v-if="orderData.status=='进行中' && !modifyIcon" @click="dialogVisible = true" >更新进度</el-button>
          <el-button  type="danger" round v-if="orderData.status=='进行中' || orderData.status=='交付中'" @click="confirmAppeal" >发起申诉</el-button>
          <el-button  type="danger" round v-if="orderData.status=='已冻结'">申诉中</el-button>
        </div>
        <div v-if="!modifyIcon">

          <el-dialog
            title="更新进度"
            :visible.sync="dialogVisible"
            width="500"
            :before-close="handleClose">

            <el-dialog
              title="提示"
              :visible.sync="employeeSubmit"
              width="30%"
              :before-close="handleClose"
              append-to-body>
              <span>期望进度已达100%，将进入验收阶段，确定提交?</span>
              <span slot="footer" class="dialog-footer">
            <el-button @click="employeeSubmit = false">取 消</el-button>
            <el-button type="primary" @click="employeeConfirm">确 定</el-button>
            </span>
            </el-dialog>
            <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
              <el-form-item label="更新主题" prop="title">
                <el-input v-model="ruleForm.title"></el-input>
              </el-form-item>
              <el-form-item label="更新描述" prop="desc">
                <el-input v-model="ruleForm.desc" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm"
                  type="textarea"
                  :autosize="{ minRows: 2, maxRows: 4}"
                  placeholder="请输入本次更新内容描述">
                </el-input>
              </el-form-item>
              <el-form-item label="更新进度" prop="progress">
                <el-input v-model.number="ruleForm.progress" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm"
                          placeholder="请输入本次更新内容描述">
                </el-input>
              </el-form-item>
              <el-form-item label="附件" >
                <el-upload
                  class="upload-demo"
                  drag
                  action="#"
                  :auto-upload="false"
                  accept=".rar,.zip"
                  :on-change="saveFile"
                  :show-file-list="false"
                  >
                  <i class="el-icon-upload"></i>
                  <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
                  <div class="el-upload__tip" slot="tip">只能上传zip/rar文件</div>
                </el-upload>
              </el-form-item>
            </el-form>
            <span slot="footer" class="dialog-footer">
             <el-button @click="dialogVisible = false">取 消</el-button>
             <el-button type="primary" @click="submitForm('ruleForm')">确 定</el-button>
            </span>
          </el-dialog>


          <!--<el-button type="primary" round v-if="orderData.status=='进行中'" @click="dialogVisible = true" >更新进度</el-button>-->
          <!--<el-button  type="danger" round v-if="orderData.status=='进行中' || orderData.status=='交付中'" >发起申诉</el-button>-->
          <!--<span v-if="orderData.status=='进行中'" @click="showDialog('employerDialog')">交付项目</span>-->
          <span v-if="orderData.status=='交付中'">交付中</span>

        </div>
        <!--<div v-if="modifyIcon">-->
          <!--<span v-if="orderData.status=='交付中'" @click="showDialog('employeeDialog')">验收通过</span>-->
          <!--<span v-if="orderData.status=='交付中'" @click="unCheck">验收不通过</span>-->
        <!--</div>-->
        <span v-if="orderData.status=='已完成'">已完成</span>
      </div>
    </div>
  </div>
</template>
<script>
  import {baseUrl, updateRules} from '@/config/config'
  import ReleaseForm from '@/components/share/ReleaseForm'
  import ReleaseInfo from '@/components/share/ReleaseInfo'
  import ApplyCard from '@/components/share/ApplyCard'
  import MyProgress from '@/components/share/MyProgress'
  import EmployerScore from '@/components/EmployerScore'
  import EmployeeScore from '@/components/EmployeeScore'
  import MyDialog from '@/components/share/MyDialog'



  export default {
    props: ['id'],   //todo releaseId
    data () {
      return{
        baseUrl: baseUrl,
        releaseData: {}, //todo 项目信息
        orderData: {
          hasComplete: 0
        },
        dialogVisible: false,
        showModify: false,
        modifyIcon: false,
        releaseProData: {},
        participantInfo: {},
        employerDialog: false,
        employeeDialog: false,
        rules: updateRules,
        updateLoading: false,
        rejectDialog: false,
        rejectReason: '',
        progressColor: '',
        employeeSubmit: false,
        employerSubmit: false,
        appealDialog: false,
        appealReason: '',
        ruleForm: {
          title: '',
          desc: '',
          progress: null,
          file: null

        },

        fileList: []
      }
    },
    components: {
      ReleaseForm,
      ReleaseInfo,
      ApplyCard,
      MyProgress,
      EmployerScore,
      EmployeeScore,
      MyDialog
    },
    methods: {
      confirmAppeal () {
//        if (this.orderData.hasComplete < 30) {
//          this.$notify.error({
//            title: '错误',
//            message: '项目时间还未过30%，不能发起申诉！',
//            offset: 75
//          })
//          return
//        }
          this.appealDialog = true
      },
      sendAppeal () {
        if (this.appealReason) {
          if (this.appealReason.length > 200) {
          this.$notify.error({
            title: '错误',
            message: '理由过长，请限制在200字以内.',
            offset: 75
          })
          return
          }
          this.$ajax.get(baseUrl + 'sendAppeal', {
            params: {
              orderId: this.orderData.id,
              complainantId: this.$store.state.loginId,
              reason: this.appealReason
            }
          })
            .then(res => {
              this.$notify({
                title: '成功',
                message: '提交申诉成功，系统将在五天内审核，请耐心等待.',
                offset: 75
              })
              this.appealDialog = false
            }, res => {
              this.$notify.error({
                title: '错误',
                message: '获取数据失败， 请检查网络链接',
                offset: 75
              })
            })
        } else {
          this.$notify.error({
            title: '错误',
            message: '请填写申诉理由.',
            offset: 75
          })
        }
      },
      employerConfirm () {
        this.employerSubmit = false
        this.employeeDialog = true
      },
      employeeConfirm () {
        this.employeeSubmit = false
        this.sendProgress();
        this.employerDialog = true
      },
      tableRowClassName ({row, index}) {
        console.log(row.status)
        return row.status
      },
      saveFile (file) {
        this.ruleForm.file = file
      },
      submitForm (ruleForm) {
        this.$refs[ruleForm].validate((valid) => {
          if (valid) {
            if (!this.ruleForm.file) {
              this.alertTip('请上传文件')
              return
            }
            if (this.ruleForm.progress > 100 || this.ruleForm.progress < 0) {
              this.alertTip('进度必须在0-100之内')
              return
            } else {
              if (this.ruleForm.progress < this.orderData.progress) {
                this.alertTip('进度必须大于等于当前进度')
                return
              }
            }

            if (this.ruleForm.progress === 100) {
              this.employeeSubmit = true
              return;
            }
            this.sendProgress()
          } else {
            return false;
          }
        })
      },
      sendProgress () {
        let formData = new FormData()
        formData.append('title', this.ruleForm.title)
        formData.append('releaseId', this.id)
        formData.append('desc', this.ruleForm.desc)
        formData.append('file', this.ruleForm.file.raw)
        formData.append('progress', this.ruleForm.progress)
        this.$ajax.post(baseUrl + 'updateProgress', formData)
          .then((res) => {
            console.log(res.data)
          }, res =>{
            console.log(res.data)
          })
        this.dialogVisible = false
      },
      alertTip (content) {
        this.$confirm(content)
          .then(() => {})
          .catch(_ => {})
      },
      handleClose (done) {
        this.alertTip('确认关闭', done)
      },
      parseData (data) {
        this.orderData = data
        let beginTime = new Date(this.orderData.beginTime.replace(/-/g,'/')).getTime()
        let deadlineTime = new Date(this.orderData.deadlineTime.replace(/-/g,'/')).getTime()
        this.orderData.hasComplete = 100
        if (this.orderData.hasComplete >= 100) {
          this.orderData.hasComplete = parseInt((new Date().getTime() - beginTime)/(deadlineTime - beginTime) * 100);
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
      getData () {
        this.$ajax.get(baseUrl + 'showOrderData', {
          params: {
            releaseId: this.id,
          }
        })
          .then(
            res => {
              this.parseData(res.data)
              return this.orderData
            }, res => {
              this.$notify.error({
                title: '错误',
                message: '获取数据失败， 请检查网络链接',
                offset: 75
              })
              return
            }
          )
          .then(
            data => {
              if (parseInt(this.$store.state.loginId !== data.employeeId) || parseInt(this.$store.state.loginId !== data.employerId)) {
                alert('非法访问，请立即退出!')
                this.$router.push({name: 'index'})
              } else {
                return this.$ajax.get(baseUrl + 'showReleasePro', {
                  params:{
                    id: data.releaseId
                  }
                })
              }
            }
          )
          .then(
            res => {
              this.releaseProData = res.data
              if (parseInt(this.$store.state.loginId) === res.data.employerId) {
                this.modifyIcon = true
              } else {
                this.modifyIcon = false
              }
            }, res => {
              this.$notify.error({
                title: '错误',
                message: '获取数据失败， 请检查网络链接',
                offset: 75
              })
              return
            }
          )
          .then(() => {
            return this.$ajax.get(baseUrl + 'participantInfo', {
              params:{
                employerId: this.orderData.employerId,
                employeeId: this.orderData.employeeId
              }
            })
            }
          )
          .then(res => {
            this.participantInfo = res.data
          }, res => {
            this.$notify.error({
              title: '错误',
              message: '获取数据失败， 请检查网络链接',
              offset: 75
            })
            return
          })
          .catch((ex) =>{})
      },
      showFiles () {
        this.updateLoading = true;
        this.$ajax.get(baseUrl + 'showUpdateList', {
          params: {
            releaseId: this.id
          }
        })
          .then(res => {
            this.updateLoading = false
            this.fileList = res.data.map((item, index) => {
              item.currentProgress = this.orderData.progress
              item.fileName = item.fileDir.split(/\/\d+-/)[1]
              return item
            })
          }, res => {
            this.$notify.error({
              title: '错误',
              message: '获取数据失败， 请检查网络链接',
              offset: 75
            })
          })
      },
      modify () {
        this.showModify = !this.showModify
      },
      sendApply () {},
      updateProgress () {
        this.$ajax.get(baseUrl + 'updateProgress' ,{
          params: {
            orderId: this.orderData.id,
            value: this.orderData.progress
          }
        }).then(res => {
          if (res.data === 10003) {
            this.getData()
            alert('更新成功')
          } else {
            alert('更新失败')
          }
        }, res => {
          this.$notify.error({
            title: '错误',
            message: '获取数据失败， 请检查网络链接',
            offset: 75
          })
        })
      },
      showDialog (dialogName) {
        this[dialogName] = !this[dialogName]
        this.$store.commit('changeSinger', 'curtain')
      },
      submitProgress (score, employerEvaluate) {
        this.$ajax.get(baseUrl + 'employeeEvaluate' ,{
          params: {
            orderId: this.orderData.id,
            value: 100,
            type: '交付项目',
            score: score,
            employerEvaluate: employerEvaluate
          }
        }).then(res => {
          if (res.data === 10004) {
            this.showDialog('employerDialog')
            this.getData()
            this.$notify({
              title: '成功',
              message: '交付成功，请等待最后的验证收',
              offset: 75,
              type: 'success'
            })
          } else {
            this.$notify.error({
              title: '错误',
              message: '交付失败',
              offset: 75
            })
          }
        }, res => {
          this.$notify.error({
            title: '错误',
            message: '获取数据失败， 请检查网络链接',
            offset: 75
          })
        })
      },
      unCheck () {
        this.$ajax.get(baseUrl + 'checkProject', {
          params: {
            orderId: this.orderData.id,
            type: 'no'
          }
        }).then(res => {
          if (res.data === 10005) {
            this.getData()
          }
        }, res => {
          this.$notify.error({
            title: '错误',
            message: '获取数据失败， 请检查网络链接',
            offset: 75
          })
        })
      },
      sendAgree (row, agress, params = {}) {
        this.$ajax.get(baseUrl + 'updateHandle',{
          params: $.extend(true, {}, {
            updateId: row.id,
            agress: agress
          }, params)})
          .then( res => {
            this.$notify({
              title: '操作成功',
              message: '进度更新',
              type: 'success',
              offset: 75
            });
            this.getData()
            this.showFiles()

          }, res => {
            this.$notify.error({
              title: '错误',
              message: '获取数据失败， 请检查网络链接',
              offset: 75
            })
          })
      },
      handleClick(row, agress, params = {}) {
        this.row = row
        this.agress = agress
        this.params = params
        if (row.progress === 100 && agress ) {
          this.employerSubmit = true
          return;
        }
        if (row.progress === 100 && !agress ) {
          this.unCheck()
        }
        this.sendAgree(row, agress, params)
      },
      submitComplete (credit, quality, onTime, employeeEvaluate) {
        this.sendAgree(this.row, this.agress, this.params)
        this.$ajax.get(baseUrl + 'checkProject', {
          params: {
            orderId: this.orderData.id,
            type: 'yes',
            credit: credit,
            quality: quality,
            onTime: onTime,
            employeeEvaluate: employeeEvaluate
          }
        }).then(res => {
          if (res.data === 10006) {
            alert('项目已完成')
            this.showDialog('employeeDialog')
            this.getData()
          }
        }, res => {
          this.$notify.error({
            title: '错误',
            message: '获取数据失败， 请检查网络链接',
            offset: 75
          })
        })
      }
    },
    beforeRouteEnter (to, from, next) {
      next(vm => {
        if (!vm.$store.state.hasLogin) {
          alert('请先登录')
          vm.$router.push({name: 'index'})
        }
        vm.getData()
        vm.$store.commit('changeSingerState', {stateName: 'myHeader', value: true})
      })
    },
  }
</script>
