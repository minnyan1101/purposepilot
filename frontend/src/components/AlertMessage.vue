<script setup>
const props = defineProps(["message"])

</script>

<template>
  <div class="bg-neutral-50 border-2 text-sm p-2 border-red-600 rounded-md">
    {{ props.message }}
  </div>
</template>