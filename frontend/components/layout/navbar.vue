<template>
    <section id="login" class="flex flex-col items-center justify-center w-full text-black bg-white">
        <div class="xs:max-w-screen-[450px] sm:max-w-screen-sm md:max-w-screen-md lg:max-w-screen-lg xl:max-w-screen-xl 2xl:max-w-screen-xl w-full h-full flex flex-col justify-between items-center">
            <div class="flex items-center justify-between h-[55px] w-full 2xl:p-0 xl:p-0 lg:p-0 md:p-0 sm:p-0 xs:p-5">
                <NuxtLink to="/" class="flex flex-row items-center justify-start 2xl:w-1/3 xl:w-1/3 lg:w-1/3 md:w-4/5 sm:w-4/5 xs:w-4/5">
                    <img src="/logo/logo_latarnik.png" alt="Logo Latarnika Choczewo" class="h-[45px]">
                    <span class="ml-5 2xl:text-xl xl:text-xl lg:text-xl md:text-xl sm:text-xl xs:text-md font-inter flex flex-col"><span class="text-dark text-[1rem] font-medium tracking-[0.02em] leading-[1.333]">Latarnik Choczewo</span><span class="text-[0.825rem] leading-[1] tracking-[0.02em]">{{this.languageStore.t.nav_list}}</span></span>
                </NuxtLink>
                <div class="2xl:flex xl:flex lg:flex md:hidden sm:hidden xs:hidden items-center justify-evenly w-1/4 font-inter uppercase">
                    <NuxtLink v-if="!this.isPlayersRoute" to="/players" class="px-5 py-2">
                        <button class="text-[1rem] leading-[1.5] tracking-[0.005em]">{{this.languageStore.t.nav_players}}</button>
                    </NuxtLink>
                    <NuxtLink v-else class="bg-[#f5f5f5] px-5 py-2 rounded-[0.5rem]">
                        <button class="text-[1rem] leading-[1.5] tracking-[0.005em]">{{this.languageStore.t.nav_players}}</button>
                    </NuxtLink>
                    <NuxtLink v-if="!this.isCoachesRoute && this.authStore.user !== null && this.authStore.user.user.user_type === 'admin'" to="/coaches" class="px-5 py-2">
                        <button class="text-[1rem] leading-[1.5] tracking-[0.005em]">{{this.languageStore.t.nav_coaches}}</button>
                    </NuxtLink>
                    <NuxtLink v-else-if="this.isCoachesRoute && this.authStore.user !== null && this.authStore.user.user.user_type === 'admin'" class="bg-[#f5f5f5] px-5 py-2 rounded-[0.5rem]">
                        <button class="text-[1rem] leading-[1.5] tracking-[0.005em]">{{this.languageStore.t.nav_coaches}}</button>
                    </NuxtLink>
                </div>
                <div class="2xl:flex xl:flex lg:flex md:hidden sm:hidden xs:hidden flex-row items-center justify-end w-1/3">
                    <div v-if="this.authStore.loggedIn" class="dropdown dropdown-center w-[50px] flex justify-end mr-5">
                        <v-icon tabindex="0" role="button" class="text-black" style="font-size: 30px !important;">mdi-account</v-icon>
                        <ul tabindex="0" class="dropdown-content z-[1] menu p-2 shadow bg-base-100 rounded-box w-[250px] mt-[30px]">
                            <li v-if="this.authStore.user.user" class="text-left cursor-default justify-start">
                                <span class="flex flex-col text-left"><span class="font-[500]">{{ this.authStore.user.user.email }}</span></span>
                            </li>
                            <li><NuxtLink to="/auth/login?action=logout" @click="this.logout()" class="text-red-500">
                                <v-icon>mdi-logout</v-icon> {{this.languageStore.t.nav_logout}}
                            </NuxtLink></li>
                        </ul>
                    </div>
                    <div class="dropdown dropdown-center w-[50px] flex justify-end">
                        <div tabindex="0" role="button">
                            <span>{{ this.getFlagEmoji(this.selectedLanguage.code)}} {{ this.selectedLanguage.code }}</span>
                        </div>
                        <ul tabindex="0" class="dropdown-content z-[1] menu p-2 shadow bg-base-100 rounded-box w-[100px] mt-[30px]">
                            <li v-for="lang in this.languageStore.languages"  :key="lang.code" :value="lang" class="text-left cursor-default justify-start">
                                <span @click="this.changeLanguage(lang)" class="text-[1rem]">{{ this.getFlagEmoji(lang.code) }} {{ lang.code }}</span>
                            </li>
                        </ul>
                    </div>
                </div>
                <v-app-bar-nav-icon size="x-large" elevation="0" class="2xl:hidden xl:hidden lg:hidden md:flex sm:flex xs:flex text-main2 md:ml-20 sm:ml-10 xs:ml-0" @click="this.drawer = !this.drawer"></v-app-bar-nav-icon>
                <v-navigation-drawer v-model="drawer" temporary class="flex flex-col p-5 items-left h-full justify-between">
                    <div class="flex flex-col h-full justify-between">
                        <div class="flex flex-col">
                            <div class="flex items-center">
                                <img src="/logo/logo_latarnik.png" alt="Logo Latarnika Choczewo" class="h-[45px]">
                                <span class="ml-5 2xl:text-xl xl:text-xl lg:text-xl md:text-xl sm:text-xl xs:text-md font-inter flex flex-col"><span class="text-dark text-[1rem] font-medium tracking-[0.02em] leading-[1.333]">Latarnik Choczewo</span><span class="text-[0.825rem] leading-[1] tracking-[0.02em]">{{this.languageStore.t.nav_list}}</span></span>
                            </div>
                            <hr class="w-full h-[1px] bg-black mt-5 mb-2">
                            <div class="flex flex-col">
                                <NuxtLink v-if="!this.isPlayersRoute" to="/players" class="text-gray-600 py-2 flex items-center">
                                    <v-icon class="mr-5">mdi-soccer</v-icon>
                                    <button class="text-[1.25rem] leading-[1.5] tracking-[0.005em]">{{this.languageStore.t.nav_players}}</button>
                                </NuxtLink>
                                <NuxtLink v-else class="py-2 rounded-[0.5rem] text-black flex items-center">
                                    <v-icon class="mr-5">mdi-soccer</v-icon>
                                    <button class="text-[1.25rem] leading-[1.5] tracking-[0.005em]">{{this.languageStore.t.nav_players}}</button>
                                </NuxtLink>
                                <NuxtLink v-if="!this.isCoachesRoute && this.authStore.user !== null && this.authStore.user.user.user_type === 'admin'" to="/coaches" class="text-gray-600 py-2 flex items-center">
                                    <v-icon class="mr-5">mdi-account</v-icon>
                                    <button class="text-[1.25rem] leading-[1.5] tracking-[0.005em]">{{this.languageStore.t.nav_coaches}}</button>
                                </NuxtLink>
                                <NuxtLink v-else-if="this.isCoachesRoute && this.authStore.user !== null && this.authStore.user.user.user_type === 'admin'" class="text-black py-2 rounded-[0.5rem] flex items-center">
                                    <v-icon class="mr-5">mdi-account</v-icon>
                                    <button class="text-[1.25rem] leading-[1.5] tracking-[0.005em]">{{this.languageStore.t.nav_coaches}}</button>
                                </NuxtLink>
                            </div>
                        </div>
                        <div>
                            <div class="mb-5">
                                <span v-if="this.selectedLanguage.code !== 'PL'" @click="this.changeLanguage({name: 'Polski', code: 'PL'})" class="mr-5 cursor-pointer"><span class="mr-5">🇵🇱</span> PL</span>
                                <span v-if="this.selectedLanguage.code !== 'EN'" @click="this.changeLanguage({name: 'English', code: 'EN'})" class="cursor-pointer"><span class="mr-5">🇬🇧</span> EN</span>
                            </div>
                            <hr class="w-full h-[1px] bg-black my-5">
                            <NuxtLink to="/auth/login?action=logout" @click="this.drawer = false, this.logout()" class="text-red-500 flex items-center">
                                <v-icon class="mr-5">mdi-logout</v-icon> {{this.languageStore.t.nav_logout}}
                            </NuxtLink>
                        </div>
                    </div>
                </v-navigation-drawer>
            </div>
        </div>
    </section>
</template>

<script lang="ts">
import { useLanguageStore } from '../../stores/translations';
import { useAuthStore } from '../../stores/auth';

interface Language {
    name: string;
    code: string;
}
interface Flag {
    code: string;
    emoji: string;
}

export default {
    computed: {
        isPlayersRoute() {
            return this.$route.path === '/players';
        },
        isCoachesRoute() {
            return this.$route.path === '/coaches';
        },
    },
    data() {
        return {
            languageStore: useLanguageStore(),
            authStore: useAuthStore(),
            selectedLanguage: {},
            flags: [
                { 'code': 'PL', 'emoji': '🇵🇱'},
                { 'code': 'EN', 'emoji': '🇬🇧'}
            ],
            drawer: null,
        };
    },
    created() {
        this.selectedLanguage = this.languageStore.language;
    },
    methods: {
        changeLanguage(lang: Language): Promise<void> {
            this.selectedLanguage = lang;
            return this.languageStore.changeLanguage(lang.name, lang.code);
        },
        getFlagEmoji(code: string): string {
            const foundFlag = this.flags.find((flag: Flag) => flag.code === code);
            return foundFlag ? foundFlag.emoji : '';
        },
        async logout(): Promise<void> {
            await this.authStore.logout();
        }
    },
};
</script>