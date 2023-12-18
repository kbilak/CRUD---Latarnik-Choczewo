<template>
    <section id="login" class="flex flex-col items-center justify-center w-full text-black bg-gray-50">
        <div class="xs:max-w-screen-[450px] sm:max-w-screen-sm md:max-w-screen-md lg:max-w-screen-lg xl:max-w-screen-xl 2xl:max-w-screen-xl w-full h-full flex flex-col justify-between items-center">
            <div class="flex items-center justify-between h-[100px] w-full">
                <div class="flex flex-row">
                    <img src="/logo/logo_latarnik.png" alt="Logo Latarnika Choczewo" class="h-[80px]">
                    <span>Latarnik Choczewo</span>
                </div>
                <div class="flex flex-row border-[1px] border-gray-300 rounded-md">
                    <select @change="this.changeLanguage()" v-model="selectedLanguage" class="py-3 px-4 block w-full bg-white rounded-lg text-sm h-[50px]">
                        <option v-for="lang in this.languageStore.languages" :key="lang.code" :value="lang">{{ this.getFlagEmoji(lang.code) }} {{ lang.name }}</option>
                    </select>
                </div>
            </div>
        </div>
    </section>
</template>

<script lang="ts">
import { useLanguageStore } from '../../stores/translations';

export default {
    data() {
        return {
            languageStore: useLanguageStore(),
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
    },
};
</script>