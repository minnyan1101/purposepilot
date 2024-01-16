<template>
  <div class="w-screen h-screen overflow-clip flex flex-col bg-neutral-100">
    <header class="w-full">
      <slot name="header" />
    </header>
    <div class="h-full flex flex-1">
      <div class="side h-full">
        <slot name="side" />
      </div>
      <main class="flex-1 overflow-auto flex justify-center">
        <slot name="main" />
      </main>
    </div>
  </div>
</template>

<style scoped></style>