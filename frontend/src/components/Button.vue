<script setup>
defineEmits([
    'click'
])

defineProps({text: String})
</script>

<template>
  <div @click="$emit('click')" class="px-2 py-1 bg-neutral-50 rounded ring ring-pink-600">
    <span class="text-neutral-800 text-base">{{ text }}</span>
  </div>
</template>