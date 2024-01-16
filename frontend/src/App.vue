<script setup>
import BaseLayout from './components/BaseLayout.vue';
import AppHeader from './components/AppHeader.vue';
import SideMenu from './components/SideMenu.vue';
</script>

<template>
  <BaseLayout>
    <template v-slot:header>
      <AppHeader />
    </template>
    
    <template v-slot:side>
      <SideMenu/>
    </template>
    
    <template v-slot:main>
      <RouterView />
    </template>
  </BaseLayout>
</template>

