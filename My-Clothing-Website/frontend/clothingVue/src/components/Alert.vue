<template>
    <div
      v-if="visible"
      :class="[
        'fixed top-5 right-5 max-w-sm flex items-center gap-3 p-4 rounded-lg shadow-lg transition-transform transform',
        alertColor,
        visible ? 'scale-100 opacity-100' : 'scale-90 opacity-0',
      ]"
    >
      <!-- Icon -->
      <div :class="[iconBgColor, 'flex items-center justify-center w-10 h-10 rounded-full']">
        <svg
          v-if="color === 'success'"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="2"
          stroke="currentColor"
          class="w-6 h-6 text-white"
        >
          <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
        </svg>
        <svg
          v-else-if="color === 'error'"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="2"
          stroke="currentColor"
          class="w-6 h-6 text-white"
        >
          <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
        </svg>
        <svg
          v-else-if="color === 'warning'"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="2"
          stroke="currentColor"
          class="w-6 h-6 text-white"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M12 8v4m0 4h.01M12 2.25c5.385 0 9.75 4.365 9.75 9.75s-4.365 9.75-9.75 9.75S2.25 17.385 2.25 12 6.615 2.25 12 2.25z"
          />
        </svg>
        <svg
          v-else
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="2"
          stroke="currentColor"
          class="w-6 h-6 text-white"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M12 2.25c5.385 0 9.75 4.365 9.75 9.75s-4.365 9.75-9.75 9.75S2.25 17.385 2.25 12 6.615 2.25 12 2.25z"
          />
        </svg>
      </div>
  
      <div class="text-white text-sm font-medium">{{ message }}</div>
  
      <button @click="visible = false" class="text-white hover:text-opacity-80">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="2"
          stroke="currentColor"
          class="w-5 h-5"
        >
          <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>
    </div>
  </template>
  
  <script setup>
    import { ref, computed, onMounted } from 'vue';
    
    const props = defineProps({
      message: {
        type: String,
        required: true,
      },
      color: {
        type: String,
        default: 'info',
      },
      time: {
        type: Number,
        default: 5,
      },
    });
    
    const visible = ref(true);
    
    onMounted(() => {
      setTimeout(() => {
        visible.value = false;
      }, props.time * 1000);
    });
    
    const alertColor = computed(() => {
      switch (props.color) {
        case 'success':
          return 'bg-green-500';
        case 'error':
          return 'bg-red-500';
        case 'warning':
          return 'bg-yellow-500';
        default:
          return 'bg-blue-500';
      }
    });
    
    const iconBgColor = computed(() => {
      switch (props.color) {
        case 'success':
          return 'bg-green-700';
        case 'error':
          return 'bg-red-700';
        case 'warning':
          return 'bg-yellow-700';
        default:
          return 'bg-blue-700';
      }
    });
  </script>
  
  <style>
  .transition-transform {
    transition: transform 0.2s ease-out, opacity 0.2s ease-out;
  }
  </style>
  