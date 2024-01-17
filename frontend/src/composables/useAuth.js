import { onMounted, onUnmounted, ref, watch } from "vue";
import { useRouter, useRoute } from "vue-router";

export function useAuth() {
  const currentUser = ref(null)
  const router = useRouter()
  const route = useRoute()
  const intervalId = ref(null)

  function checkAuth() {
    currentUser.value = null

    fetch("/api/users/me")
      .then(res => {
        if (!res.ok) {
          throw new Error('Auth Error try login');
        }

        return res.json()
      })
      .then(res => {
        currentUser.value = res["user_id"]
      })
      .catch(err => {
        currentUser.value = null
        router.push("/login")
      })
  }

  watch(route, async () => {
    checkAuth()
  })

  onMounted(() => {
    checkAuth()
    intervalId.value = setInterval(checkAuth, 30 * 1000)
  })
  onUnmounted(() => {
    clearInterval(intervalId.value)
  })

  return currentUser
}