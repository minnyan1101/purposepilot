<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import RegisterForm from '@/components/RegisterForm.vue';

const router = useRouter()

function handleRegisterData(data) {
  fetch(
    "/api/users",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    }
  ).then(res => {
    if (!res.ok) {
      throw new Error("入力したデータではユーザー登録ができません。")
    }
    router.push("/login")
  }).catch
}
</script>

<template>
  <div class="flex size-full justify-center items-center">
    <RegisterForm @submitEvent="handleRegisterData" />
  </div>
</template>