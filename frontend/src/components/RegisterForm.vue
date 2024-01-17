<script setup>
import LabeledTextInput from '@/components/LabeledTextInput.vue';
import LabeledSecretInput from '@/components/LabeledSecretInput.vue';
import StyledButton from '@/components/StyledButton.vue';
import { reactive, ref } from 'vue';

const emit = defineEmits('submit')

const data = reactive({
  user_id: "",
  password: "",
  password_confirm: "",
})

function handleSubmit() {
  emit('submitEvent', data)
  data.user_id = ''
  data.password = ''
  data.password_confirm = ''
}
</script>

<template>
  <div class="border-2 border-neutral-300 rounded-lg bg-neutral-50 px-6 py-6">
    <h1 class="text-2xl font-bold mb-4">ユーザー登録</h1>
    <form class="flex flex-col gap-4" action="" @submit="handleSubmit">
      <LabeledTextInput v-model="data.user_id" label="ユーザーID" />
      <LabeledSecretInput v-model="data.password" label="パスワード" />
      <LabeledSecretInput v-model="data.password_confirm" label="再確認" />
      <div class="flex justify-between items-center">
        <RouterLink to="/login"><p class="text-blue-500 text-xs hover:text-blue-800">ログイン</p></RouterLink>
        <StyledButton class="self-end" text="登録"></StyledButton>
      </div>
    </form>
  </div>
</template>