<script setup>
import { ref } from 'vue';
import PurposeCreateButton from '@/components/PurposeCreateButton.vue';
import PurposeCardList from '@/components/PurposeCardList.vue';

const fake_data = ref([
{
    "purpose_id": 1,
    "user_id": "fake_1",
    "title": "てすとよう目標１",
    "description": "1ヶ月目\nPythonの基礎を学ぶ\nアプリ開発の流れを学ぶ\n\n2ヶ月目\nJavaScriptの基礎を学ぶ\nアプリの構造を学ぶ\n\n3ヶ月目\nJavaの基礎を学ぶ\nアプリのリリース方法を学ぶ",
    created_at: new Date(),
    due_at: new Date(),
    status: false,
    completed_at:  new Date(),
  },  {
    "purpose_id": 2,
    "user_id": "fake_1",
    "title": "てすとよう目標２",
    "description": "3年以内に、営業成績でトップ10に入る\n5年以内に、部署リーダーに昇進する",
    created_at: new Date(),
    due_at: undefined,
    status: false,
    completed_at:  new Date(),
  },  {
    "purpose_id": 3,
    "user_id": "fake_1",
    "title": "てすとよう目標３",
    "description": "適当オブ適当さむしんぐ",
    "created_at": new Date(),
    "due_at": new Date(),
    "status": false,
    "completed_at":  new Date(),
  },
])
</script>

<template>
  <div class="px-8 py-4 max-w-4xl w-full flex flex-col gap-4">
    <PurposeCreateButton class="self-end"/>
    <PurposeCardList :purpose_list="fake_data" />
  </div>
</template>