<script setup>
import { useAuth } from '@/composables/useAuth';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
const current_user = useAuth()
</script>

<template>
  <div class="h-8 flex items-center gap-2 py-4 px-8 overflow-hidden">
    <FontAwesomeIcon icon="fa-solid fa-user"/>
    <p>{{ current_user }}</p>
  </div>
</template>