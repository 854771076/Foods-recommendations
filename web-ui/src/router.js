import { createRouter, createWebHistory  } from 'vue-router'

import Home from './components/Home.vue'
import  Login  from './components/user/Login.vue'
import Resume from './components/user/Resume.vue'
import FoodsDetail from './components/detail/FoodsDetail.vue'
import Stars from './components/sublist/Stars.vue'
import BigView from './components/sublist/BigView.vue'
import Like from './components/sublist/Like.vue'

// 创建路由对象
const router = createRouter({
  history: createWebHistory (),
  routes: [
    { path: '/', name:'首页',component: Home },
    { path: '/recommend', name:'推荐',component: Home },
    { path: '/Foods', name:'职位',component: Home },
    { path: '/mine', name:'我的',component: Home },
    { path: '/login', name:'登录',component: Login },
    { path: '/resume', name:'喜好',component: Resume },
    { path: '/star', name:'收藏',component: Stars },
    { path: '/bigview', name:'大屏',component: BigView },
    { path: '/like', name:'点赞',component: Like },
    { path: '/Foods/detail/:id', name:'食谱详细',component: FoodsDetail  },
  ],
})

// 全局路由导航守卫
router.beforeEach((to, from, next) => {
const accessToken = localStorage.getItem('accessToken')
  if ((to.path ==='/mine' ) && !accessToken) {
    // 证明用户要访问后台主页
    next('/login')
  } else {
    // 访问的不是后台主页
    next()
  }
})

export default router
