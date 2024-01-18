import { onMounted, onUnmounted, ref } from "vue";
import { usePullFetch } from "./usePullFetch";

export function useFetchPurposeList() {
  const { data, err } = usePullFetch(30 * 100, "/api/purposes")
  return data
}