<script setup>
import { computed, ref } from 'vue';
import { useRouter } from 'vue-router';
import RegisterForm from '@/components/RegisterForm.vue';
import { useValidate } from '@/composables/useValidate';
import { userIdValidate, passwordValidate } from '@/validators';
import AlertMessage from '../AlertMessage.vue';

const router = useRouter()

const user_id = ref("")
const password = ref("")
const password_confirm = ref("")
const submitError = ref("")

const [userIdOk, userIdMsg] = useValidate(userIdValidate, user_id)
const [passwordOk, passwordMsg] = useValidate(passwordValidate, password)
const [password_confirmOK, password_confirmMsg] = useValidate(passwordValidate, password_confirm)


function handleRegisterData() {
  const data = {
    user_id: user_id.value,
    password: password.value,
    password_confirm: password_confirm.value
  }

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
      if (res.status === 409) {
        throw new Error("そのユーザーは既に存在します。")
      }
      throw new Error("送信時にエラーが発生しました。")
    }
    router.push("/login")
  }).catch(e => {
    submitError.value = e.toString()
    setTimeout(() => {
      submitError.value = ""
    }, 3000);
  })
}
</script>

<template>
  <div class="m-auto relative">

    <RegisterForm @submitEvent="handleRegisterData" v-model:user_id="user_id" v-model:password="password"
      v-model:password_confirm="password_confirm" />
    <div class="absolute left-full top-0 flex flex-col w-80">
      <AlertMessage v-if="!userIdOk" :message="userIdMsg" />
      <AlertMessage v-if="!passwordOk" :message="passwordMsg" />
      <AlertMessage v-if="submitError !== ''" :message="submitError" />
    </div>
  </div>
</template>