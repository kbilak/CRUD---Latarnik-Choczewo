<template>
    <section id="login" class="flex flex-col items-center justify-center w-full h-[100vh] text-black bg-gray-50">
        <div class="xs:max-w-screen-[450px] sm:max-w-screen-sm md:max-w-screen-md lg:max-w-screen-lg xl:max-w-screen-xl 2xl:max-w-screen-xl w-full h-auto flex flex-col justify-center items-center">
            <form class="bg-white h-[600px] w-[500px] rounded-lg flex flex-col items-center justify-center border-[1px] border-gray-300">
                <h2 class="text-2xl ">{{ this.t.auth_login }}</h2>
                <!-- <span>{{ languageStore.selectedTranslations }}</span> -->
            </form>
        </div>
    </section>
</template>

<script lang="ts">
import { useLanguageStore } from '../../stores/translations';

interface Translation {
  code: string;
  translation: string;
}

export default{
    data() {
        return {
            languageStore: useLanguageStore(),
            neededCodes: ['auth_login', 'auth_sign_up'],
            t: {},
        }
    },
    created() {
        this.populateTranslations();
    },
    methods: {
        populateTranslations() {
            this.neededCodes.forEach((code: string) => {
                this.t[`${code}`] = this.getTranslation(code);
            })
        },
        getTranslation(code: string): string {
            const translation = this.languageStore.selectedTranslations.find(
                (item: Translation) => item.code === code
            );

            return translation ? translation.translation : '';
        }
    }
};
</script>