// Import necessary modules and functions
import { defineStore } from "pinia";
import { login } from "../services/auth/login";
import { signUp } from "../services/auth/sign-up";
import { getToken } from "../services/token/getToken";

// Define User interface
interface User {
    status: Number;
    user: Object;
}

// Define the authentication store
export const useAuthStore = defineStore({
    id: "authStore",
    // Define the initial state
    state: () => ({
        user: null as User | null, // User object, initially null
        token: '', // Token string, initially empty
        loggedIn: false, // Boolean to track if user is logged in, initially false
    }),
    actions: {
        // Action to log out the user
        logout() {
            this.token = ''; // Clear the token
            this.user = null; // Clear the user object
            this.loggedIn = false; // Set loggedIn to false
        },
        // Action to fetch the token
        async fetchToken() {
            this.token = await getToken(); // Fetch the token and assign it to state
        },
        // Action to log in the user
        async login(email: string, password: string) {
            try {
                await this.fetchToken(); // Fetch the token
                const response = await login(email, password, this.token); // Attempt to log in
                if (response) {
                    this.user = response; // If successful, assign the response to the user object
                    this.loggedIn = true; // Set loggedIn to true
                    return true;
                } else {
                    this.user = null; // If unsuccessful, clear the user object
                    return false;
                }
            } catch (error) {
                console.error(error); // Log any errors to the console
                return false;
            }
        },
        // Action to sign up a new user
        async signUp(email: string, password: string) {
            try {
                const response = await signUp(email, password, this.token); // Attempt to sign up
                if (response) {
                    return true; // If successful, return true
                } else {
                    return false; // If unsuccessful, return false
                }
            } catch (error) {
                console.error(error); // Log any errors to the console
                return false;
            }
        },
    },
});