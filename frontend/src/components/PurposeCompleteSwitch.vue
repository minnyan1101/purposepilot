<script setup>
const props = defineProps(["isCompleted"])
const emit = defineEmits("onSwitch")
</script>

<template>
  <button type="button" @click="emit('onSwitch')">
    <div class="py-1 px-3 bg-neutral-50 hover:bg-neutral-300 rounded-md border-2" :class="{'border-pink-600': isCompleted, 'border-neutral-600': !isCompleted}">
      <p v-if="isCompleted">達成済</p>
      <p v-else>未達成</p>
    </div>
  </button>
</template>