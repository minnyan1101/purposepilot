<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import LabeledTextInput from '@/components/LabeledTextInput.vue'
import LabeledSecretInput from '@/components/LabeledSecretInput.vue'
import StyledButton from '@/components/StyledButton.vue';
</script>

<template>
    <div class="flex size-full justify-center items-center">
    <div class="border-2 border-neutral-300 bg-neutral-50 px-6 py-6 rounded-lg flex flex-col gap-4">
      <h1 class="text-2xl font-bold text-neutral-800">アカウント新規登録</h1>
      <form class="flex flex-col gap-4" action="" @submit="login">
        <LabeledTextInput label="ユーザーID" v-model="user_id" />
        <LabeledSecretInput label="パスワード" v-model="password" />
        <StyledButton>新規登録</StyledButton>
      </form>
    </div>
  </div>
</template>