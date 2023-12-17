import { defineStore } from "pinia";
import { fetchTranslations } from "../services/i18n/translations"

export const useLanguageStore = defineStore({
	id: "languageStore",
	state: () => ({
		language: '',
		languages: {},
		translations: [],
		selectedTranslations: [],
	}),
	actions: {
		changeLanguage(language: string) {
			this.language = language;
		},
		async getTranslations() {
			const translations = await fetchTranslations();

			this.translations = translations;
			this.languages = translations.map(entry => {return {'name': entry.name, 'code': entry.code};});

			this.language = this.languages[0];

			let foundTranslations = this.translations.find(item => item.code === this.language.code)
			this.selectedTranslations = foundTranslations.translations;

			return translations;
		}
	},
});
