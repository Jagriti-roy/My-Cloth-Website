<template>
    <div v-if="isLoading" class="loading-bar"></div>
  </template>
  
  <script setup>
  import { ref, onMounted, onUnmounted } from 'vue';
  
  const props = defineProps({
    startLoading: Boolean,  // Determines if the loading should start
  });
  
  // State to control loading
  const isLoading = ref(false);
  const width = ref(0);
  
  // Start loading if prop is set
  onMounted(() => {
    if (props.startLoading) start();
  });
  
  // Start loading function
  const start = () => {
    isLoading.value = true;
    width.value = 0;
    const interval = setInterval(() => {
      if (width.value >= 100) {
        clearInterval(interval);
        finish(); // Call finish when it reaches 100%
      } else {
        width.value += 1;  // Adjust speed by changing the increment value
      }
    }, 20);
  };
  
  // Finish loading function
  const finish = () => {
    isLoading.value = false;
  };
  
  // Expose methods to be controlled by parent component
  const stop = () => finish();
  </script>
  
  <style scoped>
  .loading-bar {
    position: fixed;
    top: 0;
    left: 0;
    height: 4px;
    background-color: #ff0000; /* Red color like YouTube */
    transition: width 0.2s;
    z-index: 1000;
  }
  </style>
  