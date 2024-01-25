<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import LabeledTextInput from '@/components/LabeledTextInput.vue'
import LabeledSecretInput from '@/components/LabeledSecretInput.vue'
import StyledButton from '@/components/StyledButton.vue';

import { useValidate } from '@/composables/useValidate';
import { userIdValidate, passwordValidate } from '@/validators';
import AlertMessage from '../AlertMessage.vue';

const router = useRouter()

const user_id = ref("")
const password = ref("")


const [userIdOk, userIdMsg] = useValidate(userIdValidate, user_id)
const [passwordOk, passwordMsg] = useValidate(passwordValidate, password)

function login() {
  fetch(
    "/api/auth/login",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        user_id: user_id.value,
        password: password.value
      })
    }
  ).then(res => {
    if (!res.ok) {
      throw new Error('入力したユーザーIDかパスワードが間違っています。')
    }
    router.push("/purposes")
  }).catch(() => {
    user_id.value = ""
    password.value = ""
  })
}
</script>

<template>
  <div class="m-auto relative">
    <div class="border-2 border-neutral-300 bg-neutral-50 px-6 py-6 rounded-lg flex flex-col gap-4">
      <h1 class="text-2xl font-bold text-neutral-800">ログイン</h1>
      <form class="flex flex-col gap-4" @submit.prevent="login">
        <LabeledTextInput label="ユーザーID" v-model="user_id" />
        <LabeledSecretInput label="パスワード" v-model="password" />
        <StyledButton>ログイン</StyledButton>
      </form>
      <RouterLink class="self-start" to="/register">
        <p class="block self-start text-xs text-blue-600 hover:text-blue-800">+ 新規登録</p>
      </RouterLink>
    </div>
    <div class="flex flex-col w-80 absolute left-full top-0">
      <AlertMessage v-if="!userIdOk" :message="userIdMsg" />
      <AlertMessage v-if="!passwordOk" :message="passwordMsg" />
    </div>
  </div>
</template>