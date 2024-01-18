<script setup>
import { useAuth } from '@/composables/useAuth'
import PurposePageBackButton from '@/components/PurposePageBackButton.vue';
const currentUser = useAuth()

</script>
<template>
  <div class="px-8 py-4 max-w-4xl w-full flex flex-col gap-4">
    <PurposePageBackButton class="self-start"></PurposePageBackButton>
  </div>
</template>