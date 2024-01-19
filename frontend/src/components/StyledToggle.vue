<script setup>
const props = defineProps("isToggled")
console.log(props.isToggled)
</script>

<template>
  <button type="button" class="size-6 bg-red-500 bg-green-500" :class="{'bg-blue-500': props.isToggled}"></button>
</template>