import Vue from 'vue'
import VueRouter from 'vue-router'
Vue.use(VueRouter)

import HomeView from '@/views/HomeView.vue'
import AddView from '@/views/AddView'
import ImportView from '@/views/ImportView'
import AboutView from '@/views/AboutView'
import TestView from '@/views/TestView'
import StatisticView1 from '@/views/StatisticView1'
import StatisticView2 from '@/views/StatisticView2'
import StatisticView3 from '@/views/StatisticView3'
import StatisticView4 from '@/views/StatisticView4'
import StatisticView5 from '@/views/StatisticView5'
import StatisticView6 from '@/views/StatisticView6'
import SignView from '@/views/SignView'
import PasswdView from '@/views/PasswdView'

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/login',
    name: 'SignView',
    component: SignView
  },
  {
    path: '/passwd',
    name: 'PasswdView',
    component: PasswdView
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
    path: '/statistic1',
    name: 'StatisticView1',
    component: StatisticView1
  },
  {
    path: '/statistic2',
    name: 'StatisticView2',
    component: StatisticView2
  },
  {
    path: '/statistic3',
    name: 'StatisticView3',
    component: StatisticView3
  },
  {
    path: '/statistic4',
    name: 'StatisticView4',
    component: StatisticView4
  },
  {
    path: '/statistic5',
    name: 'StatisticView5',
    component: StatisticView5
  },
  {
    path: '/statistic6',
    name: 'StatisticView6',
    component: StatisticView6
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

// token跨页面传递
router.beforeEach((to, from, next) => {
  if (to.name == 'SignView') {
    next()
  }
  else if ((!to.query || !to.query.token) && from.query && from.query.token) {
    next({
      name: to.name,
      query: from.query
    })
  }
  else {
    next()
  }
})

const VueRouterPush = VueRouter.prototype.push
VueRouter.prototype.push = function push (to) {
  return VueRouterPush.call(this, to).catch(err => err)
}

export default router
