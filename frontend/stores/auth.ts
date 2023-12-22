import { defineStore } from "pinia";;
import { login } from "../services/auth/login";
import { signUp } from "../services/auth/sign-up";
import { getToken } from "../services/token/getToken";


export const useAuthStore = defineStore({
	id: "authStore",
	state: () => ({
		user: {},
        token: '',
        loggedIn: false,
	}),
	actions: {
        logout() {
            this.token = '';
            this.user = {};
            this.loggedIn = false;
        },
        async fetchToken() {
            this.token = await getToken();
        },
        async login(email: string, password: string) {
            await this.fetchToken();
            const response = await login(email, password, this.token);
            this.token = '';
            if (response) {
                this.user = response;
                this.loggedIn = true;
                return true;
            } else {
                this.user = {};
                return false;
            }
        },
        async signUp(email: string, password: string) {
            const response = await signUp(email, password, this.token);
            this.token = '';
            if (response) {
                return true;
            } else {
                return false;
            }
        },
	},
});
