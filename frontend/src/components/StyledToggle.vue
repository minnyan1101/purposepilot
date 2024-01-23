<script setup>
const props = defineProps(["isToggled"])
</script>

<template>
  <button type="button" class="w-12 h-6 relative">
    <div class="absolut w-full h-3 rounded-full bg-neutral-50 border border-neutral-300"></div>
    <div class="absolute border border-neutral-300 rounded-full size-6 top-0" :class="{'bg-pink-500 left-0': props.isToggled, 'bg-neutral-300 right-0': !props.isToggled}"></div>
  </button>
</template>