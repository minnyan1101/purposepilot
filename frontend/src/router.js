import { createRouter, createWebHashHistory } from 'vue-router'

import HomePage from '@/components/pages/HomePage.vue'
import ActionPage from '@/components/pages/ActionPage.vue'
import PurposePage from '@/components/pages/PurposePage.vue'
import PurposeCreatePage from '@/components/pages/PurposeCreatePage.vue'
import PurposeEditPage from '@/components/pages/PurposeEditPage.vue'
import LoginPage from '@/components/pages/LoginPage.vue'
import RegisterPage from '@/components/pages/RegisterPage.vue'


const routes = [
    { path: '/', component: HomePage },
    { path: '/action', component: ActionPage },
    { path: '/purpose', component: PurposePage },
    { path: '/purpose/new', component: PurposeCreatePage },
    { path: '/purpose/:id/edit', component: PurposeEditPage},
    { path: '/login', component: LoginPage},
    { path: '/register', component: RegisterPage}
]


export const router = createRouter({
    history: createWebHashHistory(),
    routes,
})