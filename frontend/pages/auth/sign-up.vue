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
useSeoMeta({
    title: 'Lista zawodników - Latarnik Choczewo | Rejestracja',
    description: 'Dodawanie, usuwanie, edycja i wyświetlanie zawodników i trenerów Latarnika Choczewo.',
    ogTitle: 'Lista zawodników - Latarnik Choczewo',
    ogDescription: 'Dodawanie, usuwanie, edycja i wyświetlanie zawodników i trenerów Latarnika Choczewo.',
    ogImage: 'hhttps://crud-latarnik-choczewo.vercel.app/meta/meta.png',
    ogUrl: 'https://crud-latarnik-choczewo.vercel.app/auth/sign-up/',
    twitterTitle: 'Lista zawodników - Latarnik Choczewo',
    twitterDescription: 'Dodawanie, usuwanie, edycja i wyświetlanie zawodników i trenerów Latarnika Choczewo.',
    twitterImage: 'https://crud-latarnik-choczewo.vercel.app/meta/meta.png',
    twitterCard: 'summary'
})
useHead({
    htmlAttrs: {
        lang: 'pl'
    },
    link: [
        {
            rel: 'icon',
            type: 'image/ico',
            href: '/favicon.ico'
        }
    ]
})
</script>