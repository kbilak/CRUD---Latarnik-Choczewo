<template>
    <div></div>
</template>

<script lang="ts">
import { useAuthStore } from '../stores/auth'
export default{
    data() {
        return {
            authStore: useAuthStore(),
        }
    },
    created() {
        if (this.authStore.loggedIn) {
            this.$router.push('/players');
        } else {
            this.$router.push('/auth/login');
        }
    }
};
</script>