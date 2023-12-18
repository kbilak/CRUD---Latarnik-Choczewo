import { defineStore } from "pinia";
import { fetchTranslations } from "../services/i18n/translations"

interface Translation {
  code: string;
  translation: string;
}

export const useLanguageStore = defineStore({
	id: "languageStore",
	state: () => ({
		language: {},
		languages: {},
		translations: [],
		selectedTranslations: [],
		translationLoading: false,
		t: {},
		neededCodes: [],
	}),
	actions: {
		changeLanguage(name: string, code: string) {
			this.translationLoading = true;
			this.language = {"name": name, "code": code};
			this.changeTranslations();
			this.translationLoading = false;
		},
		async getTranslations() {
			const translations = await fetchTranslations();

			this.translations = translations;
			this.languages = translations.map(entry => {return {'name': entry.name, 'code': entry.code};});

			this.neededCodes = translations[0].translations.map(item => item.code);

			if (Object.keys(this.language).length === 0) {
				this.language = this.languages[0];
			}

			await this.changeTranslations();
			
			return translations;
		},
		changeTranslations() {
			let foundTranslations = this.translations.find(item => item.code === this.language.code);
			this.selectedTranslations = foundTranslations.translations;
			this.populateTranslations();
		},
		async populateTranslations() {
            const selectedTranslations = this.selectedTranslations;

            this.neededCodes.forEach((code: string) => {
                const translation = selectedTranslations.find((item: Translation) => item.code === code);
                this.t[code] = translation ? translation.translation : '';
            });
        },
	},
});
