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
      xhr.open('POST', 'http://192.168.0.101:8081/tokenCheck')
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
      if (result === 'yes') {
        store.commit('changeSingerState', {stateName: 'hasLogin', value: true})
      } else {
        webStore.removeItem('token')
        console.log('过期')
      }
      next()
    }, () => {
      next()
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
    hasLogin: false
  },
  mutations: {
    changeSingerState (state, obj) {
      state[obj.stateName] = obj.value
    },
    changeSinger (state, stateName) {
      state[stateName] = !state[stateName]
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
