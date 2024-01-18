<script setup>
import LabeledTextInput from '@/components/LabeledTextInput.vue';
import LabeledTextArea from '@/components/LabeledTextArea.vue';
import StyledButton from '@/components/StyledButton.vue';

const emit = defineEmits('submitEvent')

const title = defineModel('title')
const description = defineModel('description')
const due_at = defineModel('due_at')

</script>
<template>
  <form  class="flex flex-col gap-4" action="">
    <LabeledTextInput label="タイトル" v-model="title" class="text-3xl" />
    <div class="flex flex-col items-start gap-1">
      <label class="text-neutral-600 text-sm">期限</label>
      <input type="datetime-local" v-model="due_at">
    </div>
    <LabeledTextArea label="詳細" v-model="description" />
    <StyledButton type="button" @click="emit('submitEvent')" text="作成"></StyledButton>
  </form>
</template>