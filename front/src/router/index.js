import Vue from 'vue'
import VueRouter from 'vue-router'
Vue.use(VueRouter)

import HomeView from '@/views/HomeView.vue'
import AddView from '@/views/AddView'
import ImportView from '@/views/ImportView'
import AboutView from '@/views/AboutView'
import TestView from '@/views/TestView'


const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/add',
    name: 'AddView',
    component: AddView
  },
  {
    path: '/import',
    name: 'ImportView',
    component: ImportView
  },
  {
    path: '/about',
    name: 'AboutView',
    component: AboutView
  },
  {
    path: '/test',
    name: 'TestView',
    component: TestView
  }
]

const router = new VueRouter({
  routes
})

const VueRouterPush = VueRouter.prototype.push
VueRouter.prototype.push = function push (to) {
  return VueRouterPush.call(this, to).catch(err => err)
}

export default router
