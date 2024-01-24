<script setup>
import { computed, ref } from 'vue';
import ReviewActionCard from './ReviewActionCard.vue';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

const props = defineProps({ actions: Array })
const isOpen = ref(false)

const totalActionTimeMs = computed(() => {
  return props.actions.reduce((accumulator, currentValue) => accumulator + (Date.parse(currentValue.finished_at) - Date.parse(currentValue.started_at)), 0)
}
)

const totalActionTimeMinute = computed(() => Math.floor(totalActionTimeMs.value / (1000 * 60)))
</script>

<template>
  <div class="flex flex-col bg-neutral-50 rounded-md border-2 border-neutral-300">
    <button @click="isOpen = !isOpen">
      <div class="w-full flex justify-end items-center gap-4 py-2 px-4">
        <div>
          <p class="text-neutral-600 self-start">行動一覧</p>
        </div>
        <div class="grow"></div>
        <div>
          <span class="text-neutral-600">合計：</span>
          <span>{{ totalActionTimeMinute }}分</span>
        </div>
        <FontAwesomeIcon v-if="isOpen" icon="fa-solid fa-angle-up" />
        <FontAwesomeIcon v-if="!isOpen" icon="fa-solid fa-angle-down" />
      </div>
    </button>
    <div v-if="isOpen" class="pl-8 divide-y-2">
      <ReviewActionCard v-for="action in actions" :action="action"></ReviewActionCard>
    </div>
  </div>
</template>