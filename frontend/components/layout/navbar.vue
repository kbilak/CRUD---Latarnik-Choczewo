<template>
    <section id="login" class="flex flex-col items-center justify-center w-full text-black bg-gray-50">
        <div class="xs:max-w-screen-[450px] sm:max-w-screen-sm md:max-w-screen-md lg:max-w-screen-lg xl:max-w-screen-xl 2xl:max-w-screen-xl w-full h-full flex flex-col justify-between items-center">
            <div class="flex items-center justify-between h-[100px] w-full">
                <NuxtLink to="/" class="flex flex-row items-center justify-start">
                    <img src="/logo/logo_latarnik.png" alt="Logo Latarnika Choczewo" class="h-[70px]">
                    <span class="ml-5 text-xl font-inter font-raleway">Latarnik Choczewo - panel zarządzania</span>
                </NuxtLink>
                <div class="flex flex-row items-center justify-end">
                    <div v-if="this.authStore.loggedIn" class="dropdown dropdown-bottom dropdown-end border-[1px] border-black rounded-full mr-5 p-1 h-[44px] w-[44px] flex items-center justify-center">
                        <v-icon tabindex="0" role="button" class="text-black" style="font-size: 30px !important;">mdi-account</v-icon>
                        <ul class="dropdown-content z-[1] menu p-2 shadow bg-base-100 rounded-box w-[250px]">
                            <li v-if="this.authStore.user.user" class="text-left">
                                <span class="flex flex-col text-left">Zalogowano jako <span class="font-bold">{{ this.authStore.user.user.email }}</span></span>
                            </li>
                            <li><NuxtLink to="/auth/login?action=logout" @click="this.logout()" class="text-red-400">
                                <v-icon>mdi-logout</v-icon> Wyloguj
                            </NuxtLink></li>
                        </ul>
                    </div>
                    <NuxtLink v-if="!this.authStore.loggedIn" to="/auth/login" class="mr-5 cursor-pointer">
                        <button type="button" class="btn h-[44px] border-[1px] border-black text-white bg-black hover:bg-[#101010] transition ease-in-out duration-300 font-medium rounded-md text-sm px-5 py-2.5 w-full uppercase flex items-center justify-center">{{this.languageStore.t.auth_login}}</button>
                    </NuxtLink>
                    <div class="flex flex-row border-[1px] border-gray-300 rounded-md">
                        <select @change="this.changeLanguage()" v-model="selectedLanguage" class="py-3 px-4 block w-full bg-white rounded-md text-sm h-[44px]">
                            <option v-for="lang in this.languageStore.languages" :key="lang.code" :value="lang">{{ this.getFlagEmoji(lang.code) }} {{ lang.name }}</option>
                        </select>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script lang="ts">
import { useLanguageStore } from '../../stores/translations';
import { useAuthStore } from '../../stores/auth';

export default {
    data() {
        return {
            languageStore: useLanguageStore(),
            authStore: useAuthStore(),
            selectedLanguage: {},
            flags: [
                { 'code': 'pl', 'emoji': '🇵🇱'},
                { 'code': 'en', 'emoji': '🇬🇧'}
            ]
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