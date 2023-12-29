<template>
    <section id="login" class="flex flex-col items-center justify-center w-full h-[100vh] min-h-[700px] text-black bg-white">
        <div class="xs:max-w-screen-[450px] sm:max-w-screen-sm md:max-w-screen-md lg:max-w-screen-lg xl:max-w-screen-xl 2xl:max-w-screen-xl w-full h-full flex flex-col justify-between items-center">
            <div class="mt-[44px]"></div>
            <v-form @submit.prevent ref="form" v-model="valid" class="bg-white h-[500px] 2xl:w-[450px] xl:w-[450px] lg:w-[450px] md:w-[450px] sm:w-[450px] xs:w-[350px] rounded-lg flex flex-col items-center justify-center 2xl:p-10 xl:p-10 lg:p-10 md:p-8 sm:p-8 xs:p-5 font-inter">
                <img src="/logo/logo_latarnik.png" alt="Logo Latarnika Choczewo" class="h-[120px] mb-[1rem]">
                <span class="text-dark text-[1.5rem] font-medium tracking-[0.02em] leading-[1.333]">Latarnik Choczewo</span>
                <span class="mb-[3rem]">{{this.languageStore.t.nav_list}}</span>
                <div class="w-full text-right">
                    <v-text-field v-model="this.email" :rules="this.emailRules" variant="outlined" class="max-h-[56px] w-full" :placeholder="this.languageStore.t.placeholder_email" :label="this.languageStore.t.placeholder_email" type="email"></v-text-field>
                    <v-text-field v-model="this.password" :rules="this.passwordRules" variant="outlined" class="max-h-[56px] w-full mt-8 mb-6" :placeholder="this.languageStore.t.placeholder_password" :label="this.languageStore.t.placeholder_password" type="password"></v-text-field>
                    <button @click="this.login()" :disabled="!valid" :class="{ 'button-disabled': !valid }" type="button" class="btn h-[56px] text-white bg-black hover:bg-[#101010] transition ease-in-out duration-300 font-medium rounded-[0.5rem] text-[1.2rem] px-5 py-2.5 mt-8 w-full font-inter flex items-center justify-center leading-[1.5] tracking-[0.005em]">
                        <template v-if="loading">
                            <div class="spinner"></div>
                        </template>
                        <template v-else>
                            {{this.languageStore.t.auth_login_action}}
                        </template>
                    </button> 
                    <div class="text-center text-[1rem] font-[400] leading-[1.5] mt-[3rem]">
                        <span class="text-blackish text-[1rem] font-[400] leading-[1.5]">{{this.languageStore.t.auth_login_account_not}} <NuxtLink to="/auth/sign-up" class="transition ease-in-out duration-300 text-[1rem] font-medium leading-[1.5] hover:text-black">{{this.languageStore.t.auth_login_account_not_sign_up}}</NuxtLink></span>
                    </div>
                </div>
            </v-form>
            <div class="mb-5">
                <span v-if="this.languageStore.language.code !== 'PL'" @click="this.changeLanguage('Polski', 'PL')" class="cursor-pointer">🇵🇱 PL</span>
                <span v-if="this.languageStore.language.code !== 'EN'" @click="this.changeLanguage('English', 'EN')" class="cursor-pointer">🇬🇧 EN</span>
            </div>
            <ClientOnly>
                <v-snackbar v-model="snackbar" :timeout="snackbarTimeout" variant="outlined" color="rgba(1, 1, 1, 0)">
                    <div class="p-4 my-4 w-[350px] text-sm text-red-600 border-[1px] border-red-900 rounded-lg bg-red-50 text-center flex items-start justify-between" role="alert">
                        <span class="font-medium font-inter">{{ this.languageStore.t.auth_login_mess_error }}</span>
                        <v-icon @click="this.snackbar = false;">mdi-close</v-icon>
                    </div>
                </v-snackbar>
                <v-snackbar v-model="snackbar2" :timeout="snackbarTimeout" variant="outlined" color="rgba(1, 1, 1, 0)">
                    <div class="p-4 my-4 w-[350px] text-sm text-green-600 border-[1px] border-green-900 rounded-lg bg-green-50 text-center flex items-start justify-between" role="alert">
                        <span class="font-medium font-inter">{{ this.languageStore.t.auth_sign_up_mess_success }}</span> 
                        <v-icon @click="this.snackbar2 = false;">mdi-close</v-icon>
                    </div>
                </v-snackbar>
                <v-snackbar v-model="snackbar3" :timeout="snackbarTimeout" variant="outlined" color="rgba(1, 1, 1, 0)">
                    <div class="p-4 my-4 w-[350px] text-sm text-green-600 border-[1px] border-green-900 rounded-lg bg-green-50 text-center flex items-start justify-between" role="alert">
                        <span class="font-medium font-inter">{{ this.languageStore.t.auth_logout_mess_success }}</span> 
                        <v-icon @click="this.snackbar3 = false;">mdi-close</v-icon>
                    </div>
                </v-snackbar>
                <v-snackbar v-model="snackbar4" :timeout="snackbarTimeout" variant="outlined" color="rgba(1, 1, 1, 0)">
                    <div class="p-4 my-4 w-[350px] text-sm text-red-600 border-[1px] border-red-900 rounded-lg bg-red-50 text-center flex items-start justify-between" role="alert">
                        <span class="font-medium font-inter">{{ this.languageStore.t.auth_login_not_login }}</span> 
                        <v-icon @click="this.snackbar4 = false;">mdi-close</v-icon>
                    </div>
                </v-snackbar>
            </ClientOnly>
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
            loading: false,
            snackbar2: false,
            snackbar3: false,
            snackbar4: false,
        };
    },
    created() {
        if (this.authStore.loggedIn) {
            this.$router.push('/players');
        }

        if (this.$route.query.action === 'signup') {
            this.snackbar2 = true;
            setTimeout(() => {
                this.snackbar2 = false;
            }, 5000);
        }

        if (this.$route.query.action === 'logout') {
            this.snackbar3 = true;
            setTimeout(() => {
                this.snackbar3 = false;
            }, 5000);
        }

        if (this.$route.query.action === 'login') {
            this.snackbar4 = true;
            setTimeout(() => {
                this.snackbar4 = false;
            }, 5000);
        }

        this.emailRules = [
            (v: string) => !!v || this.languageStore.t.rules_email_not,
            (v: string) => (v && v.length >= 5) || this.languageStore.t.rules_email_length,
            (v: string) => /.+@.+\..+/.test(v) || this.languageStore.t.rules_email_wrong,
        ];
        this.passwordRules = [
            (v: string) => !!v || this.languageStore.t.rules_password_not,
            (v: string) => (v && v.length >= 8) || this.languageStore.t.rules_password_length,
        ]
    },
    methods: {
        changeLanguage(lang: string, code: string) {
            return this.languageStore.changeLanguage(lang, code);
        },
        async login() {
            this.loading = true;
            this.$refs.form.validate().then(async (valid: boolean) => {
                if (valid) {
                    let response = await this.authStore.login(this.email, this.password);
                    if (response) {
                        this.$router.push('/players');
                        this.loading = false;
                    } else {
                        this.snackbar = true;
                        setTimeout(() => {
                            this.snackbar = false;
                        }, 5000);
                        this.loading = false;
                    }
                } else {
                    this.snackbar = true;
                    setTimeout(() => {
                        this.snackbar = false;
                    }, 5000);
                    this.loading = false;
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
  border: 4px solid rgba(255, 255, 255, 0.3);
  border-top: 4px solid #fff;
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