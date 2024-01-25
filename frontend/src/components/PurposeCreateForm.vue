<script setup>
import LabeledTextInput from '@/components/LabeledTextInput.vue';
import LabeledTextArea from '@/components/LabeledTextArea.vue';
import StyledButton from '@/components/StyledButton.vue';
import LabeledDateTimeInput from './LabeledDateTimeInput.vue';

const emit = defineEmits('submitEvent')

const title = defineModel('title')
const description = defineModel('description')
const due_at = defineModel('due_at')
</script>
<template>
  <form  class="flex flex-col gap-4" >
    <LabeledTextInput label="タイトル" v-model="title" class="text-3xl" />
    <LabeledDateTimeInput label="期限" v-model="due_at" />
    <LabeledTextArea label="詳細" v-model="description" />
    <StyledButton type="button" @click="emit('submitEvent')">作成</StyledButton>
  </form>
</template>