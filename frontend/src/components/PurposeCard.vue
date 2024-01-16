<script setup>
import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'
const props = defineProps(['purpose'])

function formatDate(date){
  if (date === undefined) {
    return 'なし'
  }
  const year = date.getFullYear().toString()
  const month = (date.getMonth() + 1).toString().padStart(2, '0')
  const day = date.getDate().toString().padStart(2, '0')
  const hours = date.getHours().toString().padStart(2, '0')
  const minutes = date.getMinutes().toString().padStart(2, '0')
  return `${year}/${month}/${day} - ${hours}:${minutes}`
}
</script>

<template>
  <div class="bg-neutral-50 rounded-lg border-2 border-neutral-300 py-2 px-4 flex gap-4">
    <FontAwesomeIcon icon="fa-solid fa-circle-play" class="text-pink-500 text-4xl hover:text-pink-700 self-center" />

    <div class="flex-grow flex flex-col divide-y-2 divide-neutral-200 gap-1">
      <div class="text-xl">
        {{ props.purpose.title }}
      </div>
      <div class="text-xs opacity-50">
        <span>期限：</span>
        {{ formatDate(props.purpose.due_at) }}
      </div>
      <div class="whitespace-pre-wrap text-sm leading-6">
        {{ props.purpose.description }}
      </div>
    </div>
    <div class="">
      <FontAwesomeIcon icon="fa-solid fa-ellipsis-vertical" class="text-neutral-800" fixed-width />
    </div>
  </div>
</template>