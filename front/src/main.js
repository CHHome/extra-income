// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import resource from 'vue-resource'
import router from './router'
import Vuex from 'vuex'
import 'bootstrap-webpack'
import $ from 'jquery'
import Vuelidate from 'vuelidate'
import axios from 'axios'
import {baseUrl} from "./config/config";

Vue.prototype.$ajax = axios

window.$ = $

router.beforeEach((to, from, next) => {
  let webStore = window.localStorage
  if (!store.state.hasLogin && 'token' in webStore) {
    new Promise(function (resolve, reject) {
      let xhr = null
      if (window.XMLHttpRequest) {
        xhr = new XMLHttpRequest()
      } else {
        xhr = new ActiveXObject()
      }
      xhr.open('POST', baseUrl + 'tokenCheck')
      xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded;charset=UTF-8')
      xhr.send('token=' + webStore['token'])
      xhr.onreadystatechange = () => {
        if (xhr.readyState !== 4) {
          return
        }
        if (xhr.status === 200) {
          resolve(xhr.responseText)
        } else {
          reject()
        }
      }
    }).then((result) => {
      result = parseInt(result)
      if (result === 10000) {
        store.commit('changeSingerState', {stateName: 'hasLogin', value: true})
      } else {
        webStore.removeItem('token')
        console.log('过期')
        next()
      }
      next()
      return axios.get(baseUrl + 'showBase', {
        params: {
          id: webStore['token'].split('-')[0]
        }
      })
    }, () => {
      next()
    }).then(res => {
      store.commit('changeHead', res.data.headImg)
    })
  } else {
    next()
  }
})
Vue.use(Vuelidate)
Vue.use(Vuex)
Vue.use(resource)
Vue.config.productionTip = false
const store = new Vuex.Store({
  state: {
    curtain: false,
    myHeader: false,
    hasLogin: false,
    headPic: 'default_head.jpg'
  },
  mutations: {
    changeSingerState (state, obj) {
      state[obj.stateName] = obj.value
    },
    changeSinger (state, stateName) {
      state[stateName] = !state[stateName]
    },
    changeHead (state, headPic) {
      state.headPic = headPic
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
