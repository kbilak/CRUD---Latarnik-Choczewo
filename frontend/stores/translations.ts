import { defineStore } from "pinia";
import { fetchTranslations } from "../services/translations"

export const useLanguageStore = defineStore({
	id: "languageStore",
	state: () => ({
		language: 'pl',
		translations: [],
	}),
	actions: {
		changeLanguage(language: string) {
			this.language = language;
		},
		updateTranslations(translations: []) {
			this.translations = translations;
		},
		async getTranslations() {
			const translations = await fetchTranslations(this.language);
			console.log(11, translations)
			this.updateTranslations(translations);
			return translations;
		}
	},
});
