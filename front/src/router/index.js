import Vue from 'vue'
import Router from 'vue-router'
const Index = () => import('@/pages/Index')
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: Index
    }
  ]
})
