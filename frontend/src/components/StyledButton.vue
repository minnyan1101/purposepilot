<script setup>
const props = defineProps(['text'])
</script>

<template>
  <button class=" px-2 block border-2 rounded border-pink-500 hover:border-pink-700 bg-neutral-50 hover:bg-neutral-200 ">{{ props.text }}</button>
</template>