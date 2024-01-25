<script setup>
import LabeledTextInput from '@/components/LabeledTextInput.vue';
import LabeledSecretInput from '@/components/LabeledSecretInput.vue';
import StyledButton from '@/components/StyledButton.vue';

const emit = defineEmits('submit')
const user_id = defineModel("user_id")
const password = defineModel("password")
const password_confirm = defineModel("password_confirm")

function handleSubmit() {
  emit('submitEvent')
}
</script>

<template>
  <div class="border-2 border-neutral-300 rounded-lg bg-neutral-50 px-6 py-6">
    <h1 class="text-2xl font-bold mb-4">ユーザー登録</h1>
    <form class="flex flex-col gap-4" @submit.prevent="handleSubmit">
      <LabeledTextInput v-model="user_id" label="ユーザーID" />
      <LabeledSecretInput v-model="password" label="パスワード" />
      <LabeledSecretInput v-model="password_confirm" label="再確認" />
      <div class="flex justify-between items-center">
        <RouterLink to="/login"><p class="text-blue-500 text-xs hover:text-blue-800">ログイン</p></RouterLink>
        <StyledButton class="self-end">登録</StyledButton>
      </div>
    </form>
  </div>
</template>