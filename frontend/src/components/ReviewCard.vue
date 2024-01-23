<script setup>
import { ref } from 'vue';

const props = defineProps(["purpose_id"])
const purpose = ref({title: null})

fetch(`/api/purposes/${props.purpose_id}`)
.then((res) => {return res.json()})
.then((json) => {
  purpose.value = json
})
</script>

<template>
  <RouterLink :to="`/reviews/new/${props.purpose_id}`">
  <div class="flex flex-col justify-stretch py-4 px-4 gap-2 bg-neutral-50 rounded-md border-2 border-neutral-300 divide-y ">
    <h1 class="text-xl font-bold">{{ purpose.title }}</h1>
    <p class="">{{ purpose.description }}</p>
  </div>
</RouterLink>
</template>