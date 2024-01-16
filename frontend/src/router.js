import { createRouter, createWebHashHistory } from 'vue-router'
/*
import HomeContent from './components/HomeContent.vue'
import ActionContent from './components/ActionContent.vue'
import PurposeContent from './components/PurposeContent.vue'
*/

import HomePage from './components/HomePage.vue'
import ActionPage from './components/ActionPage.vue'
import PurposePage from './components/PurposePage.vue'


const routes = [
    { path: '/', component: HomePage },
    { path: '/action', component: ActionPage },
    { path: '/purpose', component: PurposePage },
]


export const router = createRouter({
    history: createWebHashHistory(),
    routes,
})