<script setup>
</script>

<template>
  <div class="w-screen h-screen grid grid-cols-[auto_1fr] grid-rows-[auto_1fr] bg-neutral-100">
    <header class="col-start-1 col-end-3 row-start-1 row-end-2 ">
      <slot name="header" />
    </header>
    <nav class="col-start-1 col-end-2 row-span-1">
      <slot name="side" />
    </nav>
    <main class="col-start-2 col-end-3 row-span-1 overflow-y-scroll flex flex-col items-center">
      <slot name="main" class="" />
    </main>
  </div>
</template>

<style scoped></style>