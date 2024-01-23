<script setup>
import { computed, ref, watch } from 'vue';
import PurposeCreateButton from '@/components/PurposeCreateButton.vue';
import PurposeCardList from '@/components/PurposeCardList.vue';

import { useAuth } from '@/composables/useAuth'
import { useFetchPurposeList } from '@/composables/useFetchPurposeList';
const { currentUser } = useAuth()
const { purpose_list, err } = useFetchPurposeList()

const completed_purposes = computed(() => {
  return purpose_list.value.filter(p => p.status === "completed")
})
const uncompleted_purposes = computed(() => {
  return purpose_list.value.filter(p => p.status === "uncompleted")
})
</script>

<template>
  <div class="px-8 py-4 max-w-4xl w-full flex flex-col gap-4">
    <PurposeCreateButton class="self-end" />
    <PurposeCardList :purpose_list="uncompleted_purposes" />
    <PurposeCardList :purpose_list="completed_purposes" />
  </div>
</template>