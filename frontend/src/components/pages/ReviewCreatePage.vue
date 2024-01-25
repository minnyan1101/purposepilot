<script setup>
import { computed, reactive, ref } from 'vue';
import ReviewQuestionSlider from '../ReviewQuestionSlider.vue';
import { useRoute, useRouter } from 'vue-router';
import StyledButton from '../StyledButton.vue';
import { useAuth } from '@/composables/useAuth';
import ReviewCard from '../ReviewCard.vue';
import ReviewActionCardList from '../ReviewActionCardList.vue';

const currentUser = useAuth()
const route = useRoute()
const router = useRouter()
const targetPurposeId = computed(() => parseInt(route.params.id))
const actionData = ref([])
const questions = ref({
  q1: 0,
  q2: 0,
  q3: 0,
})

function fetchActionData() {

  const now = new Date()
  const to = new Date(now.getFullYear(), now.getMonth(), now.getDate())
  to.setDate(to.getDate() - to.getDay())

  const from = new Date(now.getFullYear(), now.getMonth(), now.getDate())
  from.setDate(from.getDate() + 7 - from.getDay())

  const params = {
    to: to.toISOString(),
    _from: from.toISOString(),
    purpose_ids: [targetPurposeId.value]
  }

  fetch(`/api/actions?${new URLSearchParams(params)}`)
    .then(res => res.json())
    .then(json => {
      actionData.value = json
    })
}
function handleSubmit() {
  const send = {
    user_id: currentUser.value,
    purpose_id: targetPurposeId.value,
    review_at: (new Date()).toISOString(),
    first_question_rating: questions.value.q1,
    second_question_rating: questions.value.q2,
    third_question_rating: questions.value.q3,
  }

  fetch("/api/reviews", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(send)
  }).then(res => {
    if (!res.ok) {
      throw new Error("ふりかえりの投稿ができませんでした。")
    }
    router.push("/reviews")
  })
}

fetchActionData()
</script>

<template>
  <div class="flex flex-col w-full max-w-xl py-4 gap-4">
    <div class="self-start">
      <RouterLink to="/reviews">
        <div
          class="border-2 rounded-md w-fit py-1 px-2 border-neutral-500 hover:border-neutral-700 bg-neutral-50 hover:bg-neutral-300">
          Back</div>
      </RouterLink>
    </div>
    <ReviewCard :purpose_id="targetPurposeId"></ReviewCard>
    <ReviewActionCardList :actions="actionData"></ReviewActionCardList>
    <ReviewQuestionSlider v-model="questions.q1" label="総行動時間に満足していますか？" />
    <ReviewQuestionSlider v-model="questions.q2" label="行動内容は目標達成に十分ですか？" />
    <ReviewQuestionSlider v-model="questions.q3" label="目標は達成可能ですか？" />
    <StyledButton @click="handleSubmit">ふりかえり</StyledButton>
  </div>
</template>