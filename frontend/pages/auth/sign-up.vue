<template>
    <div class="flex flex-col items-center justify-center w-full">
		<NuxtLayout class="hidden"></NuxtLayout>
        <AuthSignUp></AuthSignUp>
    </div>
</template>

<script setup>
definePageMeta({
    layout: false,
});
</script>