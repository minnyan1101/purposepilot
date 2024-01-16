<script setup>
import PurposeCard from './PurposeCard.vue';

const props = defineProps(['purpose_list'])
console.log(props.purpose_list)
</script>

<template>
  <PurposeCard 
    v-for="item of props.purpose_list"
    :key="item.purpose_id"
    :purpose="item"
  />
</template>