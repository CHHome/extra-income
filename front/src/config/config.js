let baseUrl = 'http://127.0.0.1:5000/'
let tokenKey = 'JD98Dskw=23njQndW9D'
export {baseUrl, tokenKey, updateRules, commonRules}


const updateRules = {
  title: [
    { required: true, message: '请输入更新主题', trigger: 'blur' },
    { min: 3, max: 12, message: '长度在 3 到 12 个字符', trigger: 'blur' }
  ],
  desc: [
    { required: true, message: '请填更新描述', trigger: 'blur' },
    { min: 1, max: 30, message: '长度在 3 到 30 个字符', trigger: 'blur' }
  ],
  progress: [
    { required: true, message: '进度不能为空'},
    { type: 'number', message: '进度必须为数字值'},
  ]
}

const commonRules = {
  number (message) {
    return [
      { required: true, message: message + '不能为空'},
      { type: 'number', message: message + '必须为数字值'},
    ]
  }
}
