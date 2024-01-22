import { createApp } from 'vue'
import '@/style.css'
import App from '@/App.vue'
import { router } from '@/router'

import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faAngleLeft, faCirclePlay, faCircleStop, faEllipsisVertical, faPenToSquare, faPlus, faUser } from '@fortawesome/free-solid-svg-icons'

library.add(faPlus, faCirclePlay, faCircleStop, faEllipsisVertical, faAngleLeft, faPenToSquare, faUser)

const app = createApp(App)
app.component('font-awesome-icon', FontAwesomeIcon)
app.use(router)
app.mount('#app')
