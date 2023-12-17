import { defineStore } from "pinia";
import { fetchTranslations } from "../services/i18n/translations"

export const useLanguageStore = defineStore({
	id: "languageStore",
	state: () => ({
		language: 'pl',
		languages: '',
		translations: [],
	}),
	actions: {
		changeLanguage(language: string) {
			this.language = language;
		},
		async getTranslations() {
			const translations = await fetchTranslations();
			this.translations = translations;
			this.languages = translations.map(entry => entry.language);
			return translations;
		}
	},
});
