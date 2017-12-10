// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import resource from 'vue-resource'
import router from './router'
import Vuex from 'vuex'
import 'bootstrap-webpack'
import $ from 'jquery'
window.$ = $

Vue.use(Vuex)
Vue.use(resource)
Vue.config.productionTip = false
const store = new Vuex.Store({
  state: {
    curtain: false
  },
  mutations: {
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
