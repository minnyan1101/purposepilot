import { createApp } from 'vue'
import '@/style.css'
import App from '@/App.vue'
import { router } from '@/router'

import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faAngleLeft, faCirclePlay, faEllipsisVertical, faPlus } from '@fortawesome/free-solid-svg-icons'

library.add(faPlus, faCirclePlay, faEllipsisVertical, faAngleLeft)

const app = createApp(App)
app.component('font-awesome-icon', FontAwesomeIcon)
app.use(router)
app.mount('#app')
