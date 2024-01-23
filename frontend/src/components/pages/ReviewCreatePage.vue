<script setup>
import { computed, ref } from 'vue';
import ReviewQuestionSlider from '../ReviewQuestionSlider.vue';
import { useRoute } from 'vue-router';

const route = useRoute()
const target_purpose_id = computed(() => route.params.id)

const questions = ref({
  q1: 0,
  q2: 0,
  q3: 0,
})

</script>

<template>
  <div class="flex flex-col w-full max-w-xl py-4 gap-4">
    <div  class="self-start">
      <RouterLink to="/reviews">
        <div class="border-2 rounded-md w-fit py-1 px-2 border-neutral-500 hover:border-neutral-700 bg-neutral-50 hover:bg-neutral-300">Back</div>
      </RouterLink>
    </div>
    <ReviewQuestionSlider v-model="questions.q1" label="Q1"/>
    <ReviewQuestionSlider v-model="questions.q2" label="Q2"/>
    <ReviewQuestionSlider v-model="questions.q3" label="Q3"/>
  </div>
</template>