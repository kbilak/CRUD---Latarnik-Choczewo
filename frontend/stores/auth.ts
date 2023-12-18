import { defineStore } from "pinia";
import { login } from "../services/auth/login"
import { getToken } from "../services/token/getToken"

export const useAuthStore = defineStore({
	id: "authStore",
	state: () => ({
		user: {},
        token: '',
        loggedIn: false,
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
                this.loggedIn = true;
                return true;
            } else {
                this.user = {};
                return false;
            }
        },
		changeLanguage(language: string) {
			this.language = language;
		},
	},
});
