<script setup>
</script>

<template>
  <div class="w-screen h-screen overflow-clip flex flex-col bg-neutral-100">
    <header class="w-full">
      <slot name="header" />
    </header>
    <div class="h-full flex flex-1">
      <slot name="side" />
      <div class="grow size-full flex flex-col items-center">
        <slot name="main" class=""/>
      </div>
    </div>
  </div>
</template>

<style scoped></style>