<template>
    <div>
        <v-text-field variant="outlined" placeholder="ddd"></v-text-field>
        <span>sds</span>
    </div>
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
        // this.languageStore = useLanguageStore();
        let r = await this.languageStore.getTranslations();
        console.log(r);
    }
};
</script>