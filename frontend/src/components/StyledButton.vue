<script setup>
const props = defineProps(['disabled'])
</script>

<template>
  <button :disabled="props.disabled" class=" px-2 block border-2 rounded  bg-neutral-50" :class="{'border-pink-500 hover:border-pink-700 hover:bg-neutral-200': !props.disabled ,'border-neutral-300 ': props.disabled}" >
    <slot></slot>  
  </button>
</template>