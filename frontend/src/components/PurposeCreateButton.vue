<script setup>
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

</script>

<template>
  <RouterLink
    to="/purposes/new"
    class="px-2 py-1 bg-neutral-50 rounded-lg border-2 border-pink-500 hover:bg-neutral-300"
  >
    <FontAwesomeIcon icon="fa-solid fa-plus" class="text-neutral-800 text-sm" />
    <span class="pl-2 text-neutral-800 text-sm">New</span>
  </RouterLink>
</template>