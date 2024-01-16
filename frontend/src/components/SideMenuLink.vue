<script setup>
    defineProps({
        link: String,
        text: String,
        isActive: Boolean,
    })

</script>

<template>
        <RouterLink :to=link>
            <div class="py-3 px-8 w-full flex hover:bg-neutral-300" :class="{'bg-neutral-300': isActive}">
                <p class="text-xl text-neutral-800">{{ text  }}</p>
            </div>
        </RouterLink>
</template>