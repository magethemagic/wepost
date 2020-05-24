import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/user/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/user/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/article/detail',
    name: 'Detail',
    component: () => import('../views/Detail.vue')
  },
  {
    path: '/search',
    name: 'Search',
    component: () => import('../views/Search.vue')
  },
  {
    path: '/user/profile',
    name: 'Profile',
    component: () => import('../views/UserProfile.vue')
  },
  {
    path: '/user/resetpwd',
    name: 'Reset',
    component: () => import('../views/resetpwd.vue')
  },
  {
    path: '/user/forgetpwd',
    name: 'ForgetPwd',
    component: () => import('../views/ForgetPwd.vue')
  }
]

const router = new VueRouter({
  routes: routes,
  mode: 'history'
})

export default router
