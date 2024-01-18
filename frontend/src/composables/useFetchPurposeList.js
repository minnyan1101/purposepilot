import { ref, watch } from "vue";
import { usePullFetch } from "./usePullFetch";

export function useFetchPurposeList() {
  const { json, err } = usePullFetch(30 * 1000, "/api/purposes", {method: "GET"})
  const purpose_list = ref(null)

  watch(json, () => {
    purpose_list.value = json.value.map((d) => {
      return {
        purpose_id: d.purpose_id,
        user_id: d.user_id,
        title: d.title,
        description: d.description,
        created_at: new Date(d.created_at),
        due_at: new Date(d.due_at),
        status: d.status,
        completed_at: new Date(d.completed_at)
      }
    })
  })

  return { purpose_list, err }
}