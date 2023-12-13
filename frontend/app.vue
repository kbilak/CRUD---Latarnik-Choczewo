<template>
    <v-app id="app" class="flex items-center justify-center w-full">
        <NuxtLayout class="min-w-full">
            <div class="flex flex-col justify-center items-center w-full">
                <NuxtPage />
            </div>
        </NuxtLayout>
    </v-app>
</template>

<script>
import axios from 'axios';
export default {
    async created() {
        
    }
}
</script>

<style lang="scss">
    @import url('https://fonts.googleapis.com/css2?family=Albert+Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Oooh+Baby&family=Questrial&family=Raleway:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
    #app {
        font-family: 'Montserrat', sans-serif;
    }
	.v-application__wrap {
		display: flex;
		align-items: center;
	}
    .v-overlay__content {
        justify-content: center;
        align-items: center;
    }
    html {
        scroll-behavior: smooth;
    }
    @media screen {
        html:not(.no-js) body [data-aos="fade-up"] {
            -webkit-transform: translate3d(0, 10px, 0);
            transform: translate3d(0, 10px, 0);
        }

        html:not(.no-js) body [data-aos="fade-down"] {
            -webkit-transform: translate3d(0, -10px, 0);
            transform: translate3d(0, -10px, 0);
        }

        html:not(.no-js) body [data-aos="fade-right"] {
            -webkit-transform: translate3d(-10px, 0, 0);
            transform: translate3d(-10px, 0, 0);
        }

        html:not(.no-js) body [data-aos="fade-left"] {
            -webkit-transform: translate3d(10px, 0, 0);
            transform: translate3d(10px, 0, 0);
        }

        html:not(.no-js) body [data-aos="fade-up-right"] {
            -webkit-transform: translate3d(-10px, 10px, 0);
            transform: translate3d(-10px, 10px, 0);
        }

        html:not(.no-js) body [data-aos="fade-up-left"] {
            -webkit-transform: translate3d(10px, 10px, 0);
            transform: translate3d(10px, 10px, 0);
        }

        html:not(.no-js) body [data-aos="fade-down-right"] {
            -webkit-transform: translate3d(-10px, -10px, 0);
            transform: translate3d(-10px, -10px, 0);
        }

        html:not(.no-js) body [data-aos="fade-down-left"] {
            -webkit-transform: translate3d(10px, -10px, 0);
            transform: translate3d(10px, -10px, 0);
        }

        html:not(.no-js) body [data-aos="zoom-in-up"] {
            -webkit-transform: translate3d(0, 10px, 0) scale(0.6);
            transform: translate3d(0, 10px, 0) scale(0.6);
        }

        html:not(.no-js) body [data-aos="zoom-in-down"] {
            -webkit-transform: translate3d(0, -10px, 0) scale(0.6);
            transform: translate3d(0, -10px, 0) scale(0.6);
        }

        html:not(.no-js) body [data-aos="zoom-in-right"] {
            -webkit-transform: translate3d(-10px, 0, 0) scale(0.6);
            transform: translate3d(-10px, 0, 0) scale(0.6);
        }

        html:not(.no-js) body [data-aos="zoom-in-left"] {
            -webkit-transform: translate3d(10px, 0, 0) scale(0.6);
            transform: translate3d(10px, 0, 0) scale(0.6);
        }

        html:not(.no-js) body [data-aos="zoom-out-up"] {
            -webkit-transform: translate3d(0, 10px, 0) scale(1.2);
            transform: translate3d(0, 10px, 0) scale(1.2);
        }

        html:not(.no-js) body [data-aos="zoom-out-down"] {
            -webkit-transform: translate3d(0, -10px, 0) scale(1.2);
            transform: translate3d(0, -10px, 0) scale(1.2);
        }

        html:not(.no-js) body [data-aos="zoom-out-right"] {
            -webkit-transform: translate3d(-10px, 0, 0) scale(1.2);
            transform: translate3d(-10px, 0, 0) scale(1.2);
        }

        html:not(.no-js) body [data-aos="zoom-out-left"] {
            -webkit-transform: translate3d(10px, 0, 0) scale(1.2);
            transform: translate3d(10px, 0, 0) scale(1.2);
        }
    }
</style>
