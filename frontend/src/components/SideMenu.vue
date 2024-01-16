<script setup>
import SideMenuLink from './SideMenuLink.vue';
</script>

<template>
  <div class="flex flex-col w-48 h-full py-4 border-r-2 border-neutral-300">
    <SideMenuLink link="/purpose" text="目標"/>
    <SideMenuLink link="/action" text="行動"/>
    <SideMenuLink link="/review" text="ふりかえり"/>
  </div>
</template>