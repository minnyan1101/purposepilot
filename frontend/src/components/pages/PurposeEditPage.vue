<script setup>
import { useAuth } from '@/composables/useAuth'
import PurposePageBackButton from '@/components/PurposePageBackButton.vue';
import PurposeEditForm from '@/components/PurposeEditForm.vue';
import { useRoute } from 'vue-router';
import { computed, ref } from 'vue';
const currentUser = useAuth()
const route = useRoute()

const purpose_id = computed(() => route.params["id"])
const purpose = ref()

fetch(`/api/purposes/${purpose_id.value}`)
.then(res => {
  if (!res.ok) {
    throw new Error(res.status)
  }
  return res.json()
}).then(json => {
  purpose.value = json
}).catch(err => {
})

function update() {
  console.log(purpose.value)
}
</script>
<template>
  <div class="px-8 py-4 max-w-4xl w-full flex flex-col gap-4">
    <PurposePageBackButton class="self-start"></PurposePageBackButton>
    <PurposeEditForm
      @submitEvent="update"
      v-model:title="purpose.title"
      v-model:description="purpose.description"
      v-model:due_at="purpose.due_at"
      v-model:status="purpose.status"
      v-model:completed_at="purpose.completed_at"
    />
  </div>
</template>