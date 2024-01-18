<script setup>
import { onMounted, ref } from 'vue';

const textAreaRef = ref()
const props = defineProps(['label'])
const model = defineModel()

function handleInput() {
  textAreaRef.value.style.height = 'auto'
  textAreaRef.value.style.height = textAreaRef.value.scrollHeight + 10 + 'px'
}

</script>

<template>
  <div class="flex flex-col gap-1">
    <label class="text-neutral-600 text-sm"> {{ props.label }}</label>
    <textarea ref="textAreaRef" spellcheck="false" rows="3" @input="handleInput" class="resize-none w-full px-4 py-2 rows leading-6 border-2 border-neutral-300 focus-visible:border-red-500 rounded" type="text"  v-model="model"></textarea>
  </div>
</template>