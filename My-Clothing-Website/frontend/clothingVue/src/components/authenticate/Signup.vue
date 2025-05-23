<template>
    <div v-if="alert_token">
      <Alert message='Account created successfully! Redirecting to login...' color='info' time='2'/>
    </div>
    <div class="bg-stone-900 min-h-screen flex justify-center items-center text-gray-200">
      <div class="max-w-lg w-full bg-stone-800 rounded-lg shadow-lg p-6">
        <h1 class="text-3xl font-bold text-amber-600 text-center mb-8">Sign Up</h1>
        <div class="space-y-6">
          <div>
            <label for="name" class="block text-sm font-medium mb-1">Full Name</label>
            <input
              v-model="customer.name"
              type="text"
              id="name"
              class="w-full px-4 py-2 rounded-md bg-stone-700 text-amber-100 focus:outline-none focus:ring focus:ring-amber-600"
              placeholder="Enter your full name"
              required
            />
          </div>
  
          <div>
            <label for="email" class="block text-sm font-medium mb-1">Email Address</label>
            <input
              v-model="customer.email"
              type="email"
              id="email"
              class="w-full px-4 py-2 rounded-md bg-stone-700 text-amber-100 focus:outline-none focus:ring focus:ring-amber-600"
              placeholder="Enter your email address"
              required
            />
          </div>
  
          <div>
            <label for="password" class="block text-sm font-medium mb-1">Password</label>
            <input
              v-model="customer.password"
              type="password"
              id="password"
              class="w-full px-4 py-2 rounded-md bg-stone-700 text-amber-100 focus:outline-none focus:ring focus:ring-amber-600"
              placeholder="Create a password"
              required
            />
          </div>
  
          <div>
            <label for="confirmPassword" class="block text-sm font-medium mb-1">Confirm Password</label>
            <input
              v-model="customer.confirmPassword"
              type="password"
              id="confirmPassword"
              class="w-full px-4 py-2 rounded-md bg-stone-700 text-amber-100 focus:outline-none focus:ring focus:ring-amber-600"
              placeholder="Confirm your password"
              required
            />
          </div>
  
          <div>
            <label for="address" class="block text-sm font-medium mb-1">Address</label>
            <input
              v-model="customer.address"
              type="text"
              id="address"
              class="w-full px-4 py-2 rounded-md bg-stone-700 text-amber-100 focus:outline-none focus:ring focus:ring-amber-600"
              placeholder="Enter your address"
            />
          </div>
  
          <div>
            <label for="phoneNumber" class="block text-sm font-medium mb-1">Phone Number</label>
            <input
              v-model="customer.phoneNumber"
              type="text"
              id="phoneNumber"
              class="w-full px-4 py-2 rounded-md bg-stone-700 text-amber-100 focus:outline-none focus:ring focus:ring-amber-600"
              placeholder="Enter your phone number"
            />
          </div>
  
          <button
            type="submit"
            @click="handleSignup"
            class="w-full bg-amber-600 text-gray-900 hover:bg-amber-700 font-semibold rounded-lg px-4 py-2"
          >
            Sign Up
          </button>
        </div>
  
        <p class="text-center text-gray-400 text-sm mt-6">
          Already have an account?
          <router-link to="/login" @click="gotologin" class="text-amber-600 hover:underline">Log In</router-link>
        </p>
      </div>
    </div>
</template>
  
<script setup>
  import { onMounted, reactive,onBeforeUnmount,ref  } from "vue";
  import { useRouter } from "vue-router";
  import { useMainStore } from "../../store";
  import axiosInstance from "../../axios";
  import Alert from "../Alert.vue";

  const store = useMainStore();
  const message = ref(null);
  const error = ref(null);
  const alert_token = ref(false);
  const customer = reactive({
    name: "",
    email: "",
    password: "",
    confirmPassword: "",
    address: "",
    phoneNumber: "",
  });
  
  const router = useRouter();
  
  function gotologin() {
    router.push("/login");
  }
  
  const handleSignup = async () => {
    if (customer.password !== customer.confirmPassword) {
      alert("Passwords do not match!");
      return;
    }

    const signupData = {
      name: customer.name,
      email: customer.email,
      password: customer.password,
      address: customer.address,
      phone_number: customer.phoneNumber,
    };

    console.log("Signup form submitted:", signupData);

    const message = ref(null);
    const error = ref(null);

    try {
      const response = await axiosInstance.post('/postUsers', signupData); 
      
      if (response.status === 200) { 
        message.value = 'Account created successfully!';
        
        customer.name = "";
        customer.email = "";
        customer.password = "";
        customer.confirmPassword = "";
        customer.address = "";
        customer.phoneNumber = "";

        alert_token.value = true;
        router.push("/login");
      } else {
        throw new Error("Unexpected response status.");
      }
    } catch (err) {
      error.value = 'Failed to create an account. Please try again later.';
      message.value = null;
      console.error('Error:', err);

      alert("Failed to create an account. Please try again later.");
    }
  };



  onBeforeUnmount(() => {
    store.setAppToken(0);
  });

  onMounted(() => {
    store.setAppToken(1);
  });

</script>
