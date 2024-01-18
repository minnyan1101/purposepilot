import { onMounted, onUnmounted, ref } from "vue";

export function usePullFetch(delay_ms, url, options) {
  const data = ref(null)
  const error = ref(null)
  const intervalId = ref(null)

  function pullFetch() {
    fetch(url, options)
    .then(res => {
      return res.json()
    }).then(json => {
      console.log(json)
      data.value = json
    }).catch(err => {
      error.value = err
    })
  }

  pullFetch()
/*
  onMounted(() => {
    pullFetch()
    intervalId.value = setInterval(pullFetch, delay_ms)
  })

  onUnmounted(() => {
    clearInterval(intervalId.value)
  })
*/
  return { data , error }
}