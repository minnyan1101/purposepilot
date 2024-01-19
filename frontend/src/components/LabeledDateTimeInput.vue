<script setup>
const props = defineProps(["label"])
const due_at = defineModel()
</script>

<template>
  <div class="flex flex-col items-start gap-1">
    <label class="text-neutral-600 text-sm">{{ props.label }}</label>
    <input type="datetime-local" v-model="due_at">
  </div>
</template>