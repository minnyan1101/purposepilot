<script setup>
import { useAuth } from '@/composables/useAuth'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { useFetchPurposeList } from '@/composables/useFetchPurposeList';
import { computed, onMounted, ref } from 'vue';
const currentUser = useAuth()
const { purpose_list, err } = useFetchPurposeList()

const purpose_accordion_data = computed(() => {
  return purpose_list.value.map((purpose) => {
    return {id: purpose.purpose_id, title: purpose.title}
  })
})

const action_detail = ref("")
const select_id = ref()
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

onMounted(() => {
  const step = (t) => {
    if (recode_state.value === "begin") {
      started_at.value = new Date()
      finished_at.value = new Date()
    }

    if (recode_state.value === "start") {
      finished_at.value = new Date()
    }
  }
  setInterval(step, 100)
})

function handleStart() {
  if (recode_state.value !== "begin") {
    return
  }
  recode_state.value = "start"
}

function handleFinish(){
  if (recode_state.value !== "start") {
    return
  }
  recode_state.value = "end"
}

function changeSelect(e) {
  select_id.value = e.target.value
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
  }).then(() => {

  }).catch()
}
</script>

<template>
  <div class="m-auto grid grid-cols-2 grid-rows-3">
    <div class="col-span-1 row-start-1 row-end-4">
      <div class="">
        <h1 class="text-5xl">{{ display_elasped }}</h1>
      </div>
      <button @click="handleStart">
        <FontAwesomeIcon icon="fa-solid fa-circle-play"></FontAwesomeIcon>
      </button>
      <button @click="handleFinish">
        <FontAwesomeIcon icon="fa-solid fa-circle-stop"></FontAwesomeIcon>
      </button>
    </div>
    <div class="col-start-2 col-end-3 row-start-1 row-end-4">
      <select name="purposes" required=true @change="changeSelect">
        <option v-for="data in purpose_accordion_data" :value="data.id" :key="data.id">{{ data.title }}</option>
      </select>
    </div>
    <div class="col-start-2 col-end-3 row-start-2 row-end-3">
      <textarea v-model="action_detail"></textarea>
    </div>
    <div class="col-start-2 col-end-3 row-start-3 row-end-4">
      <button @click="handleSubmit">送信</button>
    </div>
  </div>
</template>