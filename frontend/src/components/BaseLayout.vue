<script setup>
import { useAuth } from '@/composables/useAuth'
const currentUser = useAuth()
</script>

<template>
  <div class="w-screen h-screen overflow-clip flex flex-col bg-neutral-100">
    <header class="w-full">
      <slot name="header" />
    </header>
    <div class="h-full flex flex-1">
      <slot name="side" />
      <slot name="main" />
    </div>
  </div>
</template>

<style scoped></style>