<script setup>
import { useRoute } from 'vue-router';
import SideMenuLink from './SideMenuLink.vue';
import SideMenuLogout from './SideMenuLogout.vue';
import SideMenuUser from './SideMenuUser.vue';

const route = useRoute()
</script>

<template>
  <div class="flex flex-col w-48 h-full py-4 border-r-2 border-neutral-300">
    <SideMenuLink link="/purposes" :is-active="route.path === '/purposes'" text="目標"/>
    <SideMenuLink link="/actions" :is-active="route.path === '/actions'" text="行動"/>
    <SideMenuLink link="/reviews" :is-active="route.path === '/reviews'" text="ふりかえり"/>
    <div class="grow"></div>
    <SideMenuUser />
    <SideMenuLogout />
  </div>
</template>