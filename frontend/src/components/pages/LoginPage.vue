<script setup>
    import BaseLayout from '@/components/BaseLayout.vue';
    import AppHeader from '@/components/AppHeader.vue';
    import SideMenu from '@/components/SideMenu.vue';
    function login(){
        const responce = fetch(/api/auth/login)
        
    }
</script>
<template>
    <lavel for="user_id">
        ユーザID
        <input 
        id="user_id"
        autocomplete="off"
        type="text"
        v-model="user_id">
    </lavel>
    <lavel for="passward">
        パスワード
        <input 
        id="passward"
        autocomplete="off"
        type="text"
        v-model="passward">
    </lavel>
    <button class="login_button" @click=login()>認証</button>
</templete>