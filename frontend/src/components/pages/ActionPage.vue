<script setup>
import { useAuth } from '@/composables/useAuth'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { useFetchPurposeList } from '@/composables/useFetchPurposeList';
import { computed, onMounted, ref, watch } from 'vue';
import StyledButton from '../StyledButton.vue';
import LabeledTextArea from '../LabeledTextArea.vue';
import { useRoute, useRouter } from 'vue-router';

const currentUser = useAuth()
const { purpose_list, err } = useFetchPurposeList()
const route = useRoute()
const router = useRouter()

const purpose_accordion_data = computed(() => {
  return purpose_list.value
  .filter((purpose) => purpose.status === "uncompleted")
  .map((purpose) => {
    return { id: purpose.purpose_id, title: purpose.title }
  })
})

const action_detail = ref("")
const select_id = ref(route.query["purpose_id"])
const recode_state = ref("begin")
const started_at = ref()
const finished_at = ref()


const elapsed_ms = computed(() => {
  return finished_at.value - started_at.value
})

const display_elasped = computed(() => {
  const base = elapsed_ms.value / 1000
  const sec = Math.floor(base % 60)
  const minute = Math.floor(base / 60 % 60)
  const hour = Math.floor(base / 3600)

  return `${hour.toString().padStart(2, "0")}h ${minute.toString().padStart(2, "0")}m ${sec.toString().padStart(2, "0")}s`
})

const canRecode = computed(() => {
  return recode_state.value === "begin"
})

const canFinish = computed(() => {
  return recode_state.value === "start"
})

const canSubmit = computed(() => {
  return recode_state.value === "end"
})

onMounted(() => {
  const step = () => {
    if (recode_state.value === "begin") {
      started_at.value = new Date()
      finished_at.value = new Date()
    }

    if (recode_state.value === "start") {
      finished_at.value = new Date()
    }
  }
  setInterval(step, 100)

  if ("purpose_id" in route.query) {
    select_id.value = parseInt(route.query.purpose_id)
  }
})

function handleStart() {
  if (recode_state.value !== "begin") {
    return
  }
  recode_state.value = "start"
}

function handleFinish() {
  if (recode_state.value !== "start") {
    return
  }
  recode_state.value = "end"
}

function changeSelect(e) {
  select_id.value = parseInt(e.target.value)
}

function handleSubmit() {
  if (recode_state.value !== "end") {
    return
  }

  const send_data = {
    user_id: currentUser.value,
    purpose_id: select_id.value,
    action_detail: action_detail.value,
    started_at: started_at.value,
    finished_at: finished_at.value
  }

  fetch("/api/actions", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(send_data),
  }).then((res) => {
    if (!res.ok) {
      throw new Error("Error")
    }
    router.push("/purposes")
  }).catch()
}
</script>

<template>
  <div class="m-auto grid grid-cols-2 grid-rows-[auto_1fr_auto] gap-6 bg-neutral-50 rounded-md border-2 border-neutral-300 p-8">
    <div class="col-span-1 row-start-1 row-end-4 flex flex-col justify-around">
      <div class="">
        <h1 class="text-5xl font-mono">{{ display_elasped }}</h1>
      </div>
      <div class="flex justify-around">
        <button @click="handleStart" :disabled="!canRecode">
          <FontAwesomeIcon icon="fa-solid fa-circle-play" class="text-4xl" :class="{'text-pink-500': canRecode,'text-neutral-300': !canRecode}"></FontAwesomeIcon>
        </button>
        <button @click="handleFinish" :disabled="!canFinish">
          <FontAwesomeIcon icon="fa-solid fa-circle-stop" class="text-4xl" :class="{'text-pink-500': canFinish,'text-neutral-300': !canFinish}"></FontAwesomeIcon>
        </button>
      </div>
    </div>
    <div class="col-start-2 col-end-3 row-start-1 row-end-2">
      <select name="purposes" required=true @change="changeSelect">
        <option disabled value="select purpose title" selected>---Select purpose title---</option>
        <option v-for="data in purpose_accordion_data" :value="data.id" :key="data.id" :selected="data.id === select_id">{{ data.title }}</option>
      </select>
    </div>
    <div class="col-start-2 col-end-3 row-start-2 row-end-3">
      <LabeledTextArea v-model="action_detail"></LabeledTextArea>
    </div>
    <div class="col-start-2 col-end-3 row-start-3 row-end-4">
      <StyledButton @click="handleSubmit" :disabled="!canSubmit">送信</StyledButton>
    </div>
  </div>
</template>