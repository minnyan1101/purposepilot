<script setup>
import SideMenuLink from './SideMenuLink.vue';
import SideMenuLogout from './SideMenuLogout.vue';
import SideMenuUser from './SideMenuUser.vue';
</script>

<template>
  <div class="flex flex-col w-48 h-full py-4 border-r-2 border-neutral-300">
    <SideMenuLink link="/purposes" text="目標"/>
    <SideMenuLink link="/actions" text="行動"/>
    <SideMenuLink link="/reviews" text="ふりかえり"/>
    <div class="grow"></div>
    <SideMenuUser />
    <SideMenuLogout />
  </div>
</template>