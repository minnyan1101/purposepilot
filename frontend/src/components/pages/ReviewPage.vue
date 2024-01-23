<script setup>
import { useAuth } from '@/composables/useAuth'
import ReviewCard from '@/components/ReviewCard.vue'
import { ref } from 'vue';
const currentUser = useAuth()

const unreview_purposes = ref()

fetch("/api/reviews/need_weekly_reviews")
.then(res => res.json())
.then((json) => {
  unreview_purposes.value = json
})
</script>

<template>
  <div class="flex flex-col gap-4 max-w-4xl w-full py-8 px-4">
    <h1 class="text-2xl">今週まだ振り返っていない目標</h1>
    <ReviewCard v-for="purpose_id in unreview_purposes" :key="purpose_id" :purpose_id="purpose_id" />
  </div>
</template>