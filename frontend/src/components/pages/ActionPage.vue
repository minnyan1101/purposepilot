<script setup>
import { useAuth } from '@/composables/useAuth'
import Timer from '@/components/Timer.vue'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
const currentUser = useAuth()

methods:{
  fetch("/api/purposes/", {
    method: "GET"
  })
}
</script>

<template>
  <div>
    <div>

    </div>
  </div>
</template>