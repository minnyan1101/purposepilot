<script setup>
import Slider from './Slider.vue';
const model = defineModel()
const props = defineProps(["label"])
</script>

<template>
  <div class="grid grid-cols-[auto_1fr_auto] grid-rows-[auto_auto] gap-2">
      <p class="col-start-1 col-end-4 row-start-1 row-end-2">{{ props.label }}</p>
      <p class="col-start-1 col-end-2 row-start-2 row-end-3">悪い</p>
      <Slider max="1" min="-1" step="0.1" v-model="model"></Slider>
      <p class="col-start-3 col-end-4 row-start-2 row-end-3">良い</p>
    </div>
</template>