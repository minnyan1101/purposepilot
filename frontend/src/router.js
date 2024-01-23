import { createRouter, createWebHashHistory } from 'vue-router'

import ActionPage from '@/components/pages/ActionPage.vue'
import PurposePage from '@/components/pages/PurposePage.vue'
import PurposeCreatePage from '@/components/pages/PurposeCreatePage.vue'
import PurposeEditPage from '@/components/pages/PurposeEditPage.vue'
import LoginPage from '@/components/pages/LoginPage.vue'
import RegisterPage from '@/components/pages/RegisterPage.vue'
import SideMenu from '@/components/SideMenu.vue'
import ReviewPage from './components/pages/ReviewPage.vue'
import ReviewCreatePage from './components/pages/ReviewCreatePage.vue'


const routes = [
  { path: '/login', component: LoginPage },
  { path: '/register', component: RegisterPage },
  { path: '/', redirect: '/purposes'},
  {
    path: '/actions',
    components: {
      default: ActionPage,
      side: SideMenu
    }
  },
  {
    path: '/purposes',
    components: {
      default: PurposePage,
      side: SideMenu
    }
  },
  {
    path: '/purposes/new',
    components: {
      default: PurposeCreatePage,
      side: SideMenu
    }
  },
  {
    path: '/purposes/:id/edit',
    components: {
      default: PurposeEditPage,
      side: SideMenu
    }
  },
  {
    path: '/reviews',
    components: {
      default: ReviewPage,
      side: SideMenu
    }
  },
  {
    path: '/reviews/new/:id',
    components: {
      default: ReviewCreatePage,
      side: SideMenu
    }
  },
]


export const router = createRouter({
  history: createWebHashHistory(),
  routes,
})