import Vue from 'vue'

import axios from 'axios'
import VueAxios from 'vue-axios'
axios.defaults.headers.common['Content-Type'] = 'application/json'
axios.defaults.timeout = 3000
axios.defaults.withCredentials = false
axios.defaults.responseType = 'json'
axios.defaults.responseEncoding = 'utf8'
Vue.use(VueAxios, axios)

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI)

import 'echarts';
import ECharts from 'vue-echarts';
Vue.component('ECharts', ECharts);
import { use } from 'echarts/core'

// import ECharts modules manually to reduce bundle size
import {
  CanvasRenderer
} from 'echarts/renderers'
import {
  BarChart
} from 'echarts/charts'
import {
  GridComponent,
  TooltipComponent
} from 'echarts/components'

use([
  CanvasRenderer,
  BarChart,
  GridComponent,
  TooltipComponent
]);

// register globally (or you can do it locally)
Vue.component('v-chart', ECharts)

Vue.config.productionTip = false

import router from './router'
import store from './store'
import App from './App.vue'

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
