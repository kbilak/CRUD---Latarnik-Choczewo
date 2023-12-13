// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: false },
  css: ['~/assets/css/main.css', 'vuetify/lib/styles/main.sass', '@mdi/font/css/materialdesignicons.min.css',],
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
  modules: [
    '@pinia-plugin-persistedstate/nuxt',
    [
      '@pinia/nuxt',
      {
          autoImports: ['defineStore', 'acceptHMRUpdate'],
      },
    ],
  ],
  build: {
    transpile: ['vuetify'],
  },
  routeRules: {
    '/**': { isr: true }
  },

  imports: {
    dirs: ['stores'],
  },

  plugins: [{ src: "@/plugins/aos", ssr: false, mode: "client" }],

})