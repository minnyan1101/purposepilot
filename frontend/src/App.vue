<script setup>
import BaseLayout from '@/components/BaseLayout.vue';
import AppHeader from '@/components/AppHeader.vue';
</script>

<template>
  <BaseLayout>
    <template #header>
      <AppHeader />
    </template>
    <template #side>
      <RouterView name="side" />
    </template>
    <template #main>
      <RouterView />
    </template>
  </BaseLayout>
</template>

