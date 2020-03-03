// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import VueResource from 'vue-resource'
import VueRouter from 'vue-router'
import Routers from './routers'

Vue.config.productionTip = false

Vue.use(VueResource)

Vue.use(VueRouter)

// 自定义指令(无参数)
Vue.directive('rainbow', {
  bind(el, binding,  vnode) {
    el.style.color='#' + Math.random().toString(16).slice(2,8);
  }
})

// 自定义指令(有参数)有arg
Vue.directive('theme', {
  bind(el, binding, vnode) {
    if(binding.value == 'wide'){
      el.style.maxWidth='560px'
    }
    if(binding.arg == 'color') {
      el.style.background='#6677cc';
      el.style.padding='20px';
    }
  }
})

// 自定义过滤器
Vue.filter('snippet', function(value) {
  return value.slice(0, 100) + "...";
})

// 自定义路由
const router = new VueRouter({
  routes:Routers,
  mode:"history"
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: { App },
  template: '<App/>',
  router:router
})
