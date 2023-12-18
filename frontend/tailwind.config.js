/** @type {import('tailwindcss').Config} */
module.exports = {
    important: true,
    content: [
        "./components/**/*.{js,vue,ts}",
        "./layouts/**/*.vue",
        "./pages/**/*.vue",
        "./plugins/**/*.{js,ts}",
        "./nuxt.config.{js,ts}",
        "./app.vue",
    ],
    theme: {
        extend: {
            screens: {
                'xs': '1px'
            },
            transitionProperty: {
                'width': 'width',
                'heigth': 'height'
            },
            colors: {

            },
            fontFamily: {
                'libre': ["'Libre Baskerville', sans-serif"],
                'inter': ["'Inter', sans-serif"],
            }
        },
    },
    // plugins: [require("daisyui")],
}
