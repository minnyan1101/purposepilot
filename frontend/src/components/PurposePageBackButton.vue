<script setup>
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

</script>

<template>
  <RouterLink
    to="/purpose"
    class="px-2 py-1 bg-neutral-50 rounded-lg border-2 border-neutral-500 hover:bg-neutral-300"
    @click="handleCreatePurpose"
  >
    <FontAwesomeIcon icon="fa-solid fa-angle-left" class="text-neutral-800 text-sm" />
    <span class="pl-2 text-neutral-800 text-sm">New</span>
  </RouterLink>
</template>