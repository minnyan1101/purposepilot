<script setup>
import LabeledTextInput from '@/components/LabeledTextInput.vue';
import LabeledTextArea from '@/components/LabeledTextArea.vue';
import StyledButton from '@/components/StyledButton.vue';
import StyledToggle from '@/components/StyledToggle.vue';
import LabeledDateTimeInput from './LabeledDateTimeInput.vue';
import { computed, watch, ref } from 'vue';

const emit = defineEmits('submitEvent')

const props = defineProps(['title', 'description', 'due_at', 'status', 'completed_at'])

const isToggled = ref(false)


function toogleStatus() {
  console.log(isToggled)
  
}
</script>
<template>
  <form  class="flex flex-col gap-4" action="">
    <LabeledTextInput label="タイトル" v-model="props.title" class="text-3xl" />
    <StyledToggle :isToggled="true" @click="toogleStatus"></StyledToggle>
    <LabeledDateTimeInput label="期限" v-model="props.due_at" />
    <LabeledTextArea label="詳細" v-model="props.description" />
    <StyledButton type="button" @click="emit('submitEvent')" text="更新"></StyledButton>
  </form>
</template>