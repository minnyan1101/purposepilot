<script setup>
import PurposePageBackButton from '@/components/PurposePageBackButton.vue';
import PurposeCreateForm from '@/components/PurposeCreateForm.vue'


import { useAuth } from '@/composables/useAuth'
import { ref } from 'vue';
import { useRouter } from 'vue-router';
const currentUser = useAuth()
const router = useRouter()

const title = ref('')
const description = ref('')
const due_at = ref('')

function handleSubmit() {
  let _due_at = due_at.value
  if (_due_at !== "") {
    _due_at = (new Date(_due_at)).toISOString()
  } else {
    _due_at = null
  }

  console.log(_due_at)
  const purpose = {
    user_id: currentUser.value,
    title: title.value,
    description: description.value,
    created_at: (new Date()).toISOString(),
    due_at: _due_at,
    status: 'uncompleted',
    completed_at: undefined,
  }

  fetch("/api/purposes", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(purpose)
  }).then(res => {
    if (!res.ok) {
      throw new Error('正常に作成できませんでした')
    }
    router.push('/purposes')
  }).catch(err => {})
}
</script>
<template>
  <div class="px-8 py-4 max-w-4xl w-full flex flex-col gap-4">
    <PurposePageBackButton class="self-start"></PurposePageBackButton>
    <PurposeCreateForm v-model:title="title" v-model:description="description" v-model:due_at="due_at" @submitEvent="handleSubmit" />
  </div>
</template>