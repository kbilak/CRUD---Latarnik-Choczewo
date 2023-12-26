<template>
    <NuxtLayout :name="'404'">
        <div class="container">
            <img src="/logo/logo_latarnik.png" alt="Logo Latarnika Choczewo" class="h-[120px] mb-[1rem]">
            <span class="text-dark text-[1.5rem] font-medium tracking-[0.02em] leading-[1.333]">Latarnik Choczewo</span>
            <span class="mb-[3rem]">Lista zawodników</span>
            <div class="font-inter text-[1.5rem]">Podana strona nie istnieje.</div>
            <button @click="goBack" type="button" class="font-inter h-[50px] mt-8 bg-main hover:bg-main2 transition ease-in-out font-medium rounded text-sm px-5 py-2.5 w-[300px] uppercase">Powrót na stronę główną</button>
        </div>
    </NuxtLayout>
</template>

<script>
export default {
  methods: {
    goBack() {
      this.$router.push('/');
    },
  },
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 500px;
}

.text-4xl {
  text-align: center;
  margin-bottom: 20px;
}

.button {
  padding: 4px 6px;
  margin: 10px 0px;
  background: black;
  color: white;
}
</style>
