// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import resource from 'vue-resource'
import router from './router'
import Vuex from 'vuex'
import 'bootstrap-webpack'
import $ from 'jquery'
import {testToken} from '@/js/testToken'
import {baseUrl} from "./config/config";

window.$ = $
router.beforeEach((to, from, next) => {
  // let xhr = null
  // let store = window.localStorage
  // if(window.XMLHttpRequest)
  //   xhr = new XMLHttpRequest()
  // else
  //   xhr = new ActiveXObject()
  // xhr.onreadystatechange = () => {
  //   if(xhr.readyState == 4 && xhr.status == 200){
  //     console.log(xhr.responseText,996699)
  //     next()
  //   }
  // }
  // xhr.open('POST', 'http://127.0.0.1:8081/tokenCheck')
  // xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded;charset=UTF-8");
  // xhr.send("token="+store['token'])
  if(!store.state.hasLogin){
    // let store = window.localStorage
    // let xhr = null
    // if(window.XMLHttpRequest)
    //   xhr = new XMLHttpRequest()
    // else
    //   xhr = new ActiveXObject()
    // xhr.onreadystatechange = () => {
    //   if(xhr.readyState != 4)
    //     return;
    //   if(xhr.status == 200){
    //     if(xhr.responseText){
    //       console.log(xhr.responseText)
    //       next()
    //     }else{
    //       next()
    //     }
    //   }else
    //     next()
    // }
    // xhr.open('POST', baseUrl+'tokenCheck')
    // xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded;charset=UTF-8");
    // xhr.send("token="+store['token'])

    console.log('111')
    new Promise(function (resolve, reject) {
      let store = window.localStorage
      let xhr = null
      if(window.XMLHttpRequest)
        xhr = new XMLHttpRequest()
      else
        xhr = new ActiveXObject()
      xhr.open('POST', 'http://127.0.0.1:8081/tokenCheck')
      xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded;charset=UTF-8");
      xhr.send("token="+store['token'])
      console.log('222')
      xhr.onreadystatechange = () => {
        console.log('333')
        if(xhr.readyState != 4)
          return;
        if(xhr.status == 200)
          resolve(xhr.responseText)
        else
          reject()
      }
    }).then((result) => {
      console.log(result,898989)
      if(result){
        console.log(result,66)
        store.commit('changeHasLogin', true)
        next()
      }
      else
        next()
    },() => {
      console.log('fail22')
      next()
    })
  }else{
    next()
  }
})


Vue.use(Vuex)
Vue.use(resource)
Vue.config.productionTip = false
const store = new Vuex.Store({
  state: {
    curtain: false,
    myHeader: false,
    showLogin: false,
    showRegister: false,
    hasLogin: false
  },
  mutations: {
    changeSinger (state, stateName) {
      state[stateName] = !state[stateName]
    },
    changeMyHeader (state, value) {
      state['myHeader'] = value
    },
    changeHasLogin (state, value) {
      state['hasLogin'] = value
    }
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})
