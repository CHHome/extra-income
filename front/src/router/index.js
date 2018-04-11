import Vue from 'vue'
import Router from 'vue-router'
const Index = () => import('@/pages/Index')
const Projects = () => import('@/pages/Projects')
const Expert = () => import('@/pages/Expert')
const UserInfo = () => import('@/pages/UserInfo')
const ShowUserInfo = () => import('@/pages/ShowUserInfo')
const ReleasePro = () => import('@/pages/ReleasePro')
const ShowReleasePro = () => import('@/pages/ShowReleasePro')
const ShowMoreRelease = () => import('@/pages/ShowMoreRelease')
const ProjectOrder = () => import('@/pages/ProjectOrder')
const Account = () => import('@/pages/Account')
const Admin = () => import('@/pages/Admin')
const AdminLogin = () => import('@/pages/AdminLogin')
const AdminIndex = () => import('@/pages/AdminIndex')










Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: Index
    },
    {
      path: '/myProjects',
      name: 'projects',
      component: Projects
    },
    {
      path: '/expert',
      name: 'expert',
      component: Expert
    },
    {
      path: '/userInfo',
      name: 'userInfo',
      component: UserInfo
    },
    {
      path: '/showUserInfo/:id',
      name: 'showUserInfo',
      component: ShowUserInfo,
      props: true,
    },
    {
      path: '/releasePro',
      name: 'releasePro',
      component: ReleasePro
    },
    {
      path: '/showReleasePro/:id',
      name: 'showReleasePro',
      component: ShowReleasePro,
      props: true,
    },
    {
      path: '/showMoreRelease',
      name: 'showMoreRelease',
      component: ShowMoreRelease
    },
    {
      path: '/projectOrder/:id',
      name: 'projectOrder',
      component: ProjectOrder,
      props: true,
    },
    {
      path: '/account',
      name: 'account',
      component: Account,
    },
    {
      path: '/admin/',
      name: 'admin',
      component: Admin,
      redirect: '/admin/login',
      children: [
        {
          path: 'login',
          name: 'adminLogin',
          component:AdminLogin
        },
        {
          path: 'dashboard',
          name: 'dashboard',
          component: AdminIndex
        }
      ]
    }
  ]
})
