<script setup>
import { ref } from 'vue';
import ReviewQuestionSlider from '../ReviewQuestionSlider.vue';

const questions = ref({
  q1: 0,
  q2: 0,
  q3: 0,
})

</script>

<template>
  <div class="flex flex-col w-full max-w-xl py-4">
    <div>
      <RouterLink to="/reviews">
        <div class="border-2 rounded-md w-fit py-1 px-2 border-neutral-500 hover:border-neutral-700 bg-neutral-50 hover:bg-neutral-300">Back</div>
      </RouterLink>
    </div>
    <ReviewQuestionSlider v-model="questions.q1" />
  </div>
</template>