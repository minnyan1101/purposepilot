import { createRouter, createWebHashHistory } from 'vue-router'

import HomePage from '@/components/pages/HomePage.vue'
import ActionPage from '@/components/pages/ActionPage.vue'
import PurposePage from '@/components/pages/PurposePage.vue'
import PurposeCreatePage from '@/components/pages/PurposeCreatePage.vue'
import PurposeEditPage from '@/components/pages/PurposeEditPage.vue'
import LoginPage from '@/components/pages/LoginPage.vue'
import RegisterPage from '@/components/pages/RegisterPage.vue'
import SideMenu from '@/components/SideMenu.vue'


const routes = [
  { path: '/login', component: LoginPage },
  { path: '/register', component: RegisterPage },
  {
    path: '/',
    components: {
      default: HomePage,
      side: SideMenu
    }
  },
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
]


export const router = createRouter({
  history: createWebHashHistory(),
  routes,
})