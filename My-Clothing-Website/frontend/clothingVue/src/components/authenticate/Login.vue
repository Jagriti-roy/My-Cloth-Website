<template>
    <div class="bg-stone-900 min-h-screen flex justify-center items-center text-gray-200">
      <div class="max-w-md w-full bg-stone-800 rounded-lg shadow-lg p-6">
        <h1 class="text-3xl font-bold text-amber-600 text-center mb-8">Log In</h1>
        <form @submit.prevent="handleLogin" class="space-y-6">
          <!-- Email -->
          <div>
            <label for="email" class="block text-sm font-medium mb-1">Email Address</label>
            <input
              v-model="form.email"
              type="email"
              id="email"
              class="w-full px-4 py-2 rounded-md bg-stone-700 text-gray-200 focus:outline-none focus:ring focus:ring-amber-600"
              placeholder="Enter your email address"
              required
            />
          </div>
  
          <!-- Password -->
          <div>
            <label for="password" class="block text-sm font-medium mb-1">Password</label>
            <input
              v-model="form.password"
              type="password"
              id="password"
              class="w-full px-4 py-2 rounded-md bg-stone-700 text-gray-200 focus:outline-none focus:ring focus:ring-amber-600"
              placeholder="Enter your password"
              required
            />
          </div>
  
          <!-- Submit Button -->
          <button
            type="submit"
            class="w-full bg-amber-600 text-gray-900 hover:bg-amber-700 font-semibold rounded-lg px-4 py-2"
          >
            Log In
          </button>
        </form>
  
        <!-- Redirect to Sign Up -->
        <p class="text-center text-gray-400 text-sm mt-6">
          Don't have an account? 
          <router-link to="/signup" class="text-amber-600 hover:underline">Sign Up</router-link>
        </p>
      </div>
    </div>
  </template>
  
  <script setup>
  import { reactive } from "vue";
  import { useRouter } from "vue-router";
  import { useMainStore } from "../../store";
  import { onMounted,onBeforeUnmount } from "vue";
  const form = reactive({
    email: "",
    password: "",
  });
  
  const router = useRouter();
  const store = useMainStore();
  
  function handleLogin() {
    // Basic validation (optional)
    if (!form.email || !form.password) {
      alert("Please fill out all fields.");
      return;
    }
  
    // Mock login action (replace with API call)
    console.log("Login form submitted:", form);
  
    // Clear the form
    form.email = "";
    form.password = "";
  
    alert("Login successful! Redirecting to the dashboard...");
    router.push("/dashboard"); // Redirect to a dashboard or homepage
  }
  
  // Simulate mounted lifecycle hook

  onMounted(() => {
    store.setAppToken(1);
    
  });

  onBeforeUnmount(() => {
    store.setAppToken(0);
  });
  </script>
  
  
  <style scoped>
  /* Custom styles for the login page */
  </style>
  