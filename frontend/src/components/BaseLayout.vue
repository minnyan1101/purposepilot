<template>
    <div class="w-screen h-screen overflow-clip flex flex-col bg-neutral-100">
        <header class="w-full">
            <slot name="header"></slot>
        </header>
        <div class="flex flex-1">
            <div class="side h-full">
                <slot name="side"></slot>
            </div>
            <main class="flex-1 overflow-y-auto">
                <slot name="main"></slot>
            </main>
        </div>
    </div>
</template>

<style scoped>

</style>