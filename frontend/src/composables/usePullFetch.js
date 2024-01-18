import { onMounted, onUnmounted, ref } from "vue";

export function usePullFetch(delay_ms, url, options) {
  const json = ref(null)
  const error = ref(null)
  const intervalId = ref(null)

  function pullFetch() {
    fetch(url, options)
    .then(res => {
      return res.json()
    }).then(res_json => {
      json.value = res_json
    }).catch(err => {
      error.value = err
    })
  }

  onMounted(() => {
    pullFetch()
    intervalId.value = setInterval(pullFetch, delay_ms)
  })

  onUnmounted(() => {
    clearInterval(intervalId.value)
  })

  return { json , error }
}