<template>
    <section id="lokalizacja" class="flex flex-col items-center justify-center w-full h-auto text-black xl:mt-20 lg:mt-20 md:mt-10 sm:mt-10 xs:mt-5 bg-white">
        <div class="xs:max-w-screen-[450px] sm:max-w-screen-sm md:max-w-screen-md lg:max-w-screen-lg xl:max-w-screen-xl 2xl:max-w-screen-xl w-full h-auto flex flex-col justify-center items-center 2xl:p-0 xl:p-0 lg:p-0 md:p-0 sm:p-0 xs:p-3">
            {{languageStore.translations}}
        </div>
        <br><br>
        {{ languageStore.languages }}
    </section>
</template>

<script lang="ts">
import { useLanguageStore } from '../stores/translations'
export default{
    data() {
        return {
            languageStore: useLanguageStore(),
        }
    },
    async created() {
        let r = await this.languageStore.getTranslations();
    }
};
</script>