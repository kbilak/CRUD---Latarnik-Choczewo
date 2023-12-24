<template>
    <section id="login" class="flex flex-col items-center justify-center w-full text-black bg-white">
        <div class="xs:max-w-screen-[450px] sm:max-w-screen-sm md:max-w-screen-md lg:max-w-screen-lg xl:max-w-screen-xl 2xl:max-w-screen-xl w-full h-full flex flex-col justify-between items-center">
            <div class="flex items-center justify-between h-[55px] w-full 2xl:p-0 xl:p-0 lg:p-0 md:p-0 sm:p-0 xs:p-5">
                <NuxtLink to="/" class="flex flex-row items-center justify-start">
                    <img src="/logo/logo_latarnik.png" alt="Logo Latarnika Choczewo" class="h-[45px]">
                    <span class="ml-5 2xl:text-xl xl:text-xl lg:text-xl md:text-xl sm:text-xl xs:text-md font-inter flex flex-col"><span class="text-dark text-[1rem] font-medium tracking-[0.02em] leading-[1.333]">Latarnik Choczewo</span><span class="text-[0.825rem] leading-[1] tracking-[0.02em]">Lista zawodników</span></span>
                </NuxtLink>
                <div class="2xl:flex xl:flex lg:flex md:hidden sm:hidden xs:hidden flex-row items-center justify-end">
                    <div v-if="this.authStore.loggedIn" class="dropdown dropdown-bottom dropdown-end rounded-full mr-5 p-1 h-[44px] w-[44px] flex items-center justify-center">
                        <v-icon tabindex="0" role="button" class="text-black" style="font-size: 30px !important;">mdi-account</v-icon>
                        <ul class="dropdown-content z-[1] menu p-2 bg-white rounded-[0.5rem] w-[250px]">
                            <li v-if="this.authStore.user.user" class="text-left">
                                <span class="flex flex-col text-left">Zalogowano jako <span class="font-bold">{{ this.authStore.user.user.email }}</span></span>
                            </li>
                            <li><NuxtLink to="/auth/login?action=logout" @click="this.logout()" class="text-red-400">
                                <v-icon>mdi-logout</v-icon> Wyloguj
                            </NuxtLink></li>
                        </ul>
                    </div>
                    <NuxtLink v-if="!this.authStore.loggedIn" to="/auth/login" class="mr-5 cursor-pointer">
                        <MainButton :buttonText="this.languageStore.t.auth_login" type="black" />
                    </NuxtLink>
                    <div class="flex flex-row rounded-[0.5rem] items-center justify-center">
                        <select @change="this.changeLanguage()" v-model="selectedLanguage" class="py-3 px-4 block w-full bg-[#f5f5f5] rounded-md text-sm h-[40px]">
                            <option v-for="lang in this.languageStore.languages" :key="lang.code" :value="lang" class="font-inter">{{ this.getFlagEmoji(lang.code) }} {{ lang.name }}</option>
                        </select>
                    </div>
                </div>
                <v-app-bar-nav-icon size="x-large" elevation="0" class="2xl:hidden xl:hidden lg:hidden md:flex sm:flex xs:flex text-main2 md:ml-20 sm:ml-10 xs:ml-0" @click="this.drawer = !this.drawer"></v-app-bar-nav-icon>
                <v-navigation-drawer v-model="drawer" temporary class="flex flex-col">
                    <span>drawer</span>
                </v-navigation-drawer>
            </div>
        </div>
    </section>
</template>

<script lang="ts">
import { useLanguageStore } from '../../stores/translations';
import { useAuthStore } from '../../stores/auth';

import MainButton from '../elements/MainButton.vue'

export default {
    components: {
        MainButton
    },
    data() {
        return {
            languageStore: useLanguageStore(),
            authStore: useAuthStore(),
            selectedLanguage: {},
            flags: [
                { 'code': 'pl', 'emoji': '🇵🇱'},
                { 'code': 'en', 'emoji': '🇬🇧'}
            ],
            drawer: null,
        };
    },
    created() {
        this.selectedLanguage = this.languageStore.language;
    },
    methods: {
        async changeLanguage() {
            await this.languageStore.changeLanguage(this.selectedLanguage.name, this.selectedLanguage.code);
        },
        getFlagEmoji(code: string) {
            const foundFlag = this.flags.find(flag => flag.code === code);
            return foundFlag ? foundFlag.emoji : '';
        },
        async logout() {
            await this.authStore.logout();
        }
    },
};
</script>