import {baseUrl} from "../config/config";
//      todo 验证登录状态token是否失效
let testToken = () => {
  let result = false
  let store = window.localStorage
  let xhr = null
  if(window.XMLHttpRequest)
    xhr = new XMLHttpRequest()
  else
    xhr = new ActiveXObject()
  xhr.onreadystatechange = () => {
    if (xhr.readyState == 4 && xhr.status == 200) {
      result = true
    }
  }
  xhr.open('POST', baseUrl+'tokenCheck')
  xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded;charset=UTF-8");
  xhr.send("token="+store['token'])
  return result
}

export {testToken}
