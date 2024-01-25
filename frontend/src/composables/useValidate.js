import { ref, watchEffect, toValue } from 'vue'

export function useValidate(fn, target) {
  const result = ref(false)
  const message = ref("")

  function validate() {
    const [r, m] = fn(toValue(target))
    result.value = r
    message.value = m
  }

  watchEffect(() => {
    validate()
  })
  return [result, message] 
}