<template>
    <section id="login" class="flex flex-col items-center justify-center w-full h-[calc(100vh-200px)] text-black bg-gray-50">
        <div class="xs:max-w-screen-[450px] sm:max-w-screen-sm md:max-w-screen-md lg:max-w-screen-lg xl:max-w-screen-xl 2xl:max-w-screen-xl w-full h-full flex flex-col justify-center items-center">
            <form class="bg-white h-[600px] w-[500px] rounded-lg flex flex-col items-center justify-center border-[1px] border-gray-300 p-10 font-inter">
                <div class="bg-white mt-[-150px] mb-[75px] z-[2] w-[150px] h-[150px] flex items-center justify-center rounded-full border-[1px] border-gray-300">
                    <img src="/logo/logo_latarnik.png" alt="Logo Latarnika Choczewo" class="h-[115px]">
                </div>
                <h2 class="text-4xl font-inter font-bold">{{ this.languageStore.t.auth_login }}</h2>
                <div class="mt-10 w-full text-right">
                    <v-text-field variant="outlined" class="max-h-[56px] w-full" :placeholder="this.languageStore.t.placeholder_email" :label="this.languageStore.t.placeholder_email"></v-text-field>
                    <v-text-field variant="outlined" class="max-h-[56px] w-full mt-5 mb-3" :placeholder="this.languageStore.t.placeholder_password" :label="this.languageStore.t.placeholder_password"></v-text-field>
                    <NuxtLink to="/auth/forgot-password" class="italic text-gray-600 transition ease-in-out duration-300 hover:text-black">{{this.languageStore.t.auth_forgot_password}}</NuxtLink>
                    <button type="button" class="btn h-[56px] text-white bg-black hover:bg-[#101010] transition ease-in-out duration-300 font-medium rounded text-sm px-5 py-2.5 mt-8 w-full uppercase flex items-center justify-center">
                        {{this.languageStore.t.auth_login_action}}
                    </button>
                    <hr class="mt-5 mb-3.5">
                    <div class="text-center">
                        <span class="text-gray-600">Nie masz jeszcze konta? <NuxtLink to="/auth/sign-up" class="italic transition ease-in-out duration-300 hover:text-black">Zarejestruj się</NuxtLink></span>
                    </div>
                </div>
            </form>
            <div class="h-[100px]"></div>
        </div>
    </section>
</template>

<script lang="ts">
import { useLanguageStore } from '../../stores/translations';

export default {
    data() {
        return {
            languageStore: useLanguageStore(),
            email: '',
            password: '',
        };
    },
};
</script>
