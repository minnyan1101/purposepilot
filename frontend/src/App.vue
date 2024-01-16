<script setup>
import BaseLayout from '@/components/BaseLayout.vue';
import AppHeader from '@/components/AppHeader.vue';
import SideMenu from '@/components/SideMenu.vue';
</script>

<template>
  <BaseLayout>
    <template #header>
      <AppHeader />
    </template>
    
    <template #side>
      <SideMenu />
    </template>
    
    <template #main>
      <RouterView />
    </template>
  </BaseLayout>
</template>

