<script setup>
import { computed } from 'vue';

const props = defineProps(["action"])
const actionTimeMs = computed(() => Date.parse(props.action.finished_at) - Date.parse(props.action.started_at))
const actionTimeMinute = computed(() => Math.floor(actionTimeMs.value / (1000 * 60)))

const startDateTime = computed(() => {
  console.log(props.action)
  const start = new Date(props.action.started_at)
  return `${start.getFullYear()}/${start.getMonth()}/${start.getDate()}-${start.getHours()}:${start.getMinutes()}`
})
</script>

<template>
  <div class="py-2 px-4">
    <div class="flex justify-between items-center ">
      <p class="text-xs text-neutral-400">{{ startDateTime }}</p>
      <p>{{ actionTimeMinute }}分</p>
    </div>
    <div class="flex  gap-4">
      <div class="grow break-words whitespace-pre-line break-all">
        {{ props.action.action_detail }}
      </div>
    </div>
  </div>
</template>