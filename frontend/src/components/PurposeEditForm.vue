<script setup>
import LabeledTextInput from '@/components/LabeledTextInput.vue';
import LabeledTextArea from '@/components/LabeledTextArea.vue';
import StyledButton from '@/components/StyledButton.vue';
import StyledToggle from '@/components/StyledToggle.vue';
import LabeledDateTimeInput from './LabeledDateTimeInput.vue';
import { computed, watch, ref } from 'vue';
import PurposeCompleteSwitch from './PurposeCompleteSwitch.vue';

const emit = defineEmits('submitEvent')

const title = defineModel("title")
const description = defineModel("description")
const due_at = defineModel("due_at")
const status = defineModel("status")
const completed_at = defineModel("completed_at")

const isCompleted = computed(() => {
  return status.value === "completed"
})


function toogleStatus() {
  if (status.value === "completed") {
    status.value = "uncompleted"
    completed_at.value = null
  } else {
    status.value = "completed"
    completed_at.value = (new Date()).toISOString()
  }

  console.log(status, completed_at)
}
</script>
<template>
  <form  class="flex flex-col gap-4" action="">
    <LabeledTextInput label="タイトル" v-model="title" class="text-3xl" />
    <PurposeCompleteSwitch :isCompleted="isCompleted" @onSwitch="toogleStatus" class="self-start"/>
    <LabeledDateTimeInput label="期限" v-model="due_at" />
    <LabeledTextArea label="詳細" v-model="description" />
    <StyledButton type="button" @click="emit('submitEvent')">更新</StyledButton>
  </form>
</template>