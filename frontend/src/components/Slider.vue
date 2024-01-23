<script setup>
const value = defineModel()
const props = defineProps(["min", "max", "step"])
</script>

<template>
  <div>
    <input type="range" v-model="value" :step="step" :max="max" :min="min" class="w-full">
  </div>
</template>