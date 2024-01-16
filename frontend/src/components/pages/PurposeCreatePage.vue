<script setup>
import PurposePageBackButton from '@/components/PurposePageBackButton.vue';
import PurposeForm from '@/components/PurposeForm.vue'
</script>
<template>
  <div class="px-8 py-4 max-w-4xl w-full flex flex-col gap-4">
    <PurposePageBackButton class="self-start"></PurposePageBackButton>
    <PurposeForm></PurposeForm>
  </div>
</template>