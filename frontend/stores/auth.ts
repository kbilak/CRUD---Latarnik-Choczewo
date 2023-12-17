import { defineStore } from "pinia";
import { login } from "../services/auth/login"
import { getToken } from "../services/token/getToken"

export const useAuthStore = defineStore({
	id: "authStore",
	state: () => ({
		user: {},
        token: '',
	}),
	actions: {
        async fetchToken() {
            this.token = await getToken();
        },
        async login(email: string, password: string) {
            await this.fetchToken();
            const response = await login(email, password, this.token);
            if (response) {
                this.user = response;
            } else {
                this.user = {};
            }
        },
		changeLanguage(language: string) {
			this.language = language;
		},
	},
});
