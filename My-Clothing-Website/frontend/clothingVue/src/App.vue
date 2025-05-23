<script setup>
  import { useMainStore } from './store';
  import Navbar from './components/Navbar.vue';
  import MainFoot from './components/MainFoot.vue';
import { onMounted } from 'vue';

  const store = useMainStore();

  function logout() {
    store.clearToken();
    store.clearUser();
    window.location.href = '/'; // Redirect to home page
  }
  onMounted(() => {
    store.setAppToken(0);
  });
</script>

<template>
  <div>
    <Navbar msg="Fabrics" v-if="store.apptoken===0" />
    <router-view></router-view>
    <MainFoot v-if="store.apptoken===0" />
  </div>
</template>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s ease-in-out;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>
