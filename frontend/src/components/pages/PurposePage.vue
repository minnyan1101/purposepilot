<script setup>
import { ref, watch } from 'vue';
import PurposeCreateButton from '@/components/PurposeCreateButton.vue';
import PurposeCardList from '@/components/PurposeCardList.vue';

import { useAuth } from '@/composables/useAuth'
import { useFetchPurposeList } from '@/composables/useFetchPurposeList';
const { currentUser } = useAuth()
const { purpose_list, err } = useFetchPurposeList()
</script>

<template>
  <div class="px-8 py-4 max-w-4xl w-full flex flex-col gap-4">
    <PurposeCreateButton class="self-end" />
    <PurposeCardList :purpose_list="purpose_list" />
  </div>
</template>