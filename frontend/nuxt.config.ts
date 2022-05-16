import { defineNuxtConfig } from 'nuxt'

// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
    ssr: false,
    srcDir: "src",
    components: {
        "dirs": ["~/components"]
    },
    css: ["@/assets/css/index.css"],
    modules: [
        "@vueuse/nuxt",
        "@unocss/nuxt",
        "@pinia/nuxt",
    ],
    unocss: {
        uno: true,
        attributify: true,
        preflight: true,
        icons: {
            scale: 1.2,
            extraProperties: {
                'display': 'inline-block',
                'vertical-align': 'middle'
            }
        },
        shortcuts: [
            
        ],
        rules: [],
    },
})
