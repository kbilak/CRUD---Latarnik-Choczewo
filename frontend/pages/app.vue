<template>
    <div>
        <h1>app</h1>
    </div>
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
        if (!this.authStore.loggedIn) {
            this.$router.push('/auth/login?action=login');
        }
    }
};
</script>