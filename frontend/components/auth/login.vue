<template>
    <section id="login" class="flex flex-col items-center justify-center w-full h-[calc(100vh-200px)] text-black bg-gray-50">
        <div class="xs:max-w-screen-[450px] sm:max-w-screen-sm md:max-w-screen-md lg:max-w-screen-lg xl:max-w-screen-xl 2xl:max-w-screen-xl w-full h-full flex flex-col justify-center items-center">
            <form class="bg-white h-[600px] w-[500px] rounded-lg flex flex-col items-center justify-center border-[1px] border-gray-300 p-10">
                <div class="bg-white mt-[-150px] mb-[75px] z-[2] w-[150px] h-[150px] flex items-center justify-center rounded-full border-[1px] border-gray-300">
                    <img src="/logo/logo_latarnik.png" alt="Logo Latarnika Choczewo" class="h-[115px]">
                </div>
                <h2 class="text-3xl">{{ this.languageStore.t.auth_login }}</h2>
                <div class="mt-10 w-full">
                    <v-text-field variant="outlined" class="max-h-[56px] w-full" placeholder="Email" label="Email"></v-text-field>
                    <v-text-field variant="outlined" class="max-h-[56px] w-full my-5" placeholder="Hasło" label="Hasło"></v-text-field>
                    <button type="button" class="btn h-[50px] text-white bg-black hover:bg-[#101010] transition ease-in-out font-medium rounded text-sm px-5 py-2.5 w-full uppercase flex items-center justify-center">
                        Zaloguj się
                    </button>
                </div>
                <span class="italic mt-20">Nie pamiętasz hasła?</span>
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
