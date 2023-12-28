// Importing necessary modules and functions
import { defineStore } from "pinia";
import { fetchTranslations } from "../services/i18n/translations"

// Defining the Translation interface for type checking
interface Translation {
  code: string;
  translation: string;
}

// Defining the store using Pinia's defineStore function
export const useLanguageStore = defineStore({
	id: "languageStore", // Unique ID of the store
	state: () => ({ // Initial state of the store
		language: {}, // Current selected language
		languages: [], // List of available languages
		translations: [], // List of all translations
		selectedTranslations: [], // Translations for the selected language
		translationLoading: false, // Loading state for translations
		t: {}, // Object to hold the translations for the selected language
		neededCodes: [], // List of translation codes that are needed
	}),
	actions: { // Actions that can be performed on the state
		// Action to change the current language
		changeLanguage(name: string, code: string) {
			this.translationLoading = true; // Set loading state to true
			this.language = {"name": name, "code": code}; // Update the current language
			this.changeTranslations(); // Update the translations for the new language
			this.translationLoading = false; // Set loading state to false
		},
		// Async action to fetch translations from the API
		async getTranslations() {
			const translations = await fetchTranslations(); // Fetch translations

			this.translations = translations; // Update the translations state
			this.languages = translations.map(entry => {return {'name': entry.name, 'code': entry.code};}); // Extract the languages from the translations

			this.neededCodes = translations[0].translations.map(item => item.code); // Extract the needed translation codes

			// If no language is selected, select the first one
			if (Object.keys(this.language).length === 0) {
				this.language = this.languages[0];
			}

			await this.changeTranslations(); // Update the translations for the selected language
			
			return translations; // Return the fetched translations
		},
		// Action to update the selected translations based on the current language
		changeTranslations() {
			let foundTranslations = this.translations.find(item => item.code === this.language.code); // Find the translations for the current language
			this.selectedTranslations = foundTranslations.translations; // Update the selected translations
			this.populateTranslations(); // Populate the t object with the selected translations
		},
		// Async action to populate the t object with the selected translations
		async populateTranslations() {
			const selectedTranslations = this.selectedTranslations; // Get the selected translations

			// For each needed code, find the corresponding translation and add it to the t object
			this.neededCodes.forEach((code: string) => {
				const translation = selectedTranslations.find((item: Translation) => item.code === code);
				this.t[code] = translation ? translation.translation : '';
			});
		},
	},
});