<script setup>
const props = defineProps(['label'])
const model = defineModel()
</script>

<template>
  <div class="flex flex-col gap-1">
    <label class="text-neutral-600 text-sm"> {{ props.label }}</label>
    <input class="px-1 border-2 border-neutral-300 focus-visible:border-red-500 rounded" type="password"  v-model="model">
  </div>
</template>