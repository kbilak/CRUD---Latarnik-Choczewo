<template>
    <section id="login" class="flex flex-col items-center justify-center w-full h-[calc(100vh-200px)] min-h-[700px] text-black bg-gray-50">
        <div class="xs:max-w-screen-[450px] sm:max-w-screen-sm md:max-w-screen-md lg:max-w-screen-lg xl:max-w-screen-xl 2xl:max-w-screen-xl w-full h-full flex flex-col justify-center items-center">
            <v-form @submit.prevent ref="form" v-model="valid" class="bg-white h-[500px] w-[450px] rounded-lg flex flex-col items-center justify-center border-[1px] border-gray-300 p-10 font-inter">
                <h2 class="text-4xl font-inter font-bold">{{ this.languageStore.t.auth_login }}</h2>
                <div class="mt-10 w-full text-right">
                    <v-text-field v-model="this.email" :rules="this.emailRules" variant="outlined" class="max-h-[56px] w-full" :placeholder="this.languageStore.t.placeholder_email" :label="this.languageStore.t.placeholder_email" type="email"></v-text-field>
                    <v-text-field v-model="this.password" :rules="this.passwordRules" variant="outlined" class="max-h-[56px] w-full mt-8 mb-6" :placeholder="this.languageStore.t.placeholder_password" :label="this.languageStore.t.placeholder_password" type="password"></v-text-field>
                    <NuxtLink to="/auth/forgot-password" class="italic text-gray-600 transition ease-in-out duration-300 hover:text-black">{{this.languageStore.t.auth_forgot_password}}</NuxtLink>
                    <button @click="this.login()" :disabled="!valid" :class="{ 'button-disabled': !valid }" type="button" class="btn h-[56px] text-white bg-black hover:bg-[#101010] transition ease-in-out duration-300 font-medium rounded text-sm px-5 py-2.5 mt-8 w-full uppercase flex items-center justify-center">
                        {{this.languageStore.t.auth_login_action}}
                    </button>
                    <hr class="mt-5 mb-3.5">
                    <div class="text-center">
                        <span class="text-gray-600">Nie masz jeszcze konta? <NuxtLink to="/auth/sign-up" class="italic transition ease-in-out duration-300 hover:text-black">Zarejestruj się</NuxtLink></span>
                    </div>
                </div>
            </v-form>
            <ClientOnly>
                <v-snackbar v-model="snackbar" :timeout="snackbarTimeout" variant="outlined" color="rgba(1, 1, 1, 0)">
                    <div class="p-4 my-4 w-[350px] text-sm text-red-600 border-[1px] border-red-900 rounded-lg bg-red-50 text-center" role="alert">
                        <span class="font-medium font-inter">{{ this.languageStore.t.auth_login_mess_error }}</span> 
                    </div>
                </v-snackbar>

            </ClientOnly>
            <div class="h-[100px]"></div>
        </div>
    </section>
</template>

<script lang="ts">
import { useAuthStore } from '../../stores/auth';
import { useLanguageStore } from '../../stores/translations';

export default {
    data() {
        return {
            languageStore: useLanguageStore(),
            authStore: useAuthStore(),
            email: '',
            password: '',
            emailRules: [],
            passwordRules: [],
            valid: false,
            snackbar: false,
            snackbarTimeout: 5000,
        };
    },
    created() {
        if (this.authStore.loggedIn) {
            this.$router.push('/app');
        }
        this.emailRules = [
            (v) => !!v || this.languageStore.t.rules_email_not,
            (v) => (v && v.length >= 5) || this.languageStore.t.rules_email_length,
            (v) => /.+@.+\..+/.test(v) || this.languageStore.t.rules_email_wrong,
        ];
        this.passwordRules = [
            (v) => !!v || this.languageStore.t.rules_password_not,
            (v) => (v && v.length >= 8) || this.languageStore.t.rules_password_length,
        ]
    },
    methods: {
        async login() {
            this.$refs.form.validate().then(async valid => {
                if (valid) {
                    let response = await this.authStore.login(this.email, this.password);
                    if (response) {
                        this.$router.push('/app');
                    } else {
                        this.snackbar = true;
                        setTimeout(() => {
                            this.snackbar = false;
                        }, 5000);
                    }
                } else {
                    this.snackbar = true;
                    setTimeout(() => {
                        this.snackbar = false;
                    }, 5000);
                }
            })
        }
    }
};
</script>

<style lang="scss" scoped>
@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

// Spinner class
.spinner {
  border: 4px solid rgba(255, 255, 255, 0.3); // Light gray border
  border-top: 4px solid #fff; // White top border
  border-radius: 50%;
  width: 20px;
  height: 20px;
  animation: spin 1s linear infinite;
}
.button-disabled {
    background-color: grey !important;
    cursor: auto !important;
}
.button-disabled:hover {
    background-color: grey !important;
}
</style>