<script setup>
import { useRouter } from 'vue-router';
const router = useRouter()
function logout() {
  fetch('/api/auth/logout', {
    method: "POST",
    headers: {
      "Content-Type": 'application/json'
    },
    body: JSON.stringify({})
  }).then(res => {
    if (!res.ok) {
      throw new Error("ログインしていません")
    }
    router.push('/login')
  })
}
</script>

<template>
  <div class="h-8 flex items-center gap-2 py-4 px-8 overflow-hidden">
    <button @click="logout" class="px-2 text-red-500 rounded-md ring-red-500 hover:ring">Log Out</button>
  </div>
</template>