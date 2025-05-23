<template>
    <div class="bg-gray-900 min-h-screen text-gray-200">
      <!-- Checkout Header -->
      <div class="bg-gray-800 py-6 px-8 shadow-md">
        <h1 class="text-3xl font-bold text-amber-600">Checkout</h1>
      </div>
  
      <div class="max-w-4xl mx-auto py-10 px-6 space-y-8">
        <!-- Cart Review -->
        <div class="bg-gray-800 p-6 rounded-lg shadow-lg">
          <h2 class="text-2xl font-semibold text-amber-500 mb-4">Your Cart</h2>
          <div v-for="item in cartItems" :key="item.id" class="flex justify-between items-center py-3 border-b border-gray-700">
            <div class="flex items-center space-x-4">
              <img :src="item.image" alt="Product" class="w-16 h-16 object-cover rounded-lg" />
              <div>
                <h3 class="text-lg font-medium">{{ item.name }}</h3>
                <p class="text-sm text-gray-400">Qty: {{ item.quantity }}</p>
              </div>
            </div>
            <p class="text-lg font-semibold text-amber-400">${{ (item.price * item.quantity).toFixed(2) }}</p>
          </div>
  
          <!-- Total Price -->
          <div class="flex justify-between items-center mt-6">
            <h3 class="text-xl font-semibold">Total:</h3>
            <p class="text-2xl font-bold text-amber-400">${{ totalPrice.toFixed(2) }}</p>
          </div>
        </div>
  
        <!-- Shipping Details -->
        <div class="bg-gray-800 p-6 rounded-lg shadow-lg">
          <h2 class="text-2xl font-semibold text-amber-500 mb-4">Shipping Details</h2>
          <form @submit.prevent="handleCheckout" class="space-y-4">
            <!-- Full Name -->
            <div>
              <label for="fullName" class="block text-sm font-medium mb-1">Full Name</label>
              <input
                v-model="shippingDetails.fullName"
                type="text"
                id="fullName"
                class="w-full px-4 py-2 rounded-md bg-gray-700 text-gray-200 focus:outline-none focus:ring focus:ring-amber-600"
                placeholder="Enter your full name"
                required
              />
            </div>
  
            <!-- Address -->
            <div>
              <label for="address" class="block text-sm font-medium mb-1">Address</label>
              <input
                v-model="shippingDetails.address"
                type="text"
                id="address"
                class="w-full px-4 py-2 rounded-md bg-gray-700 text-gray-200 focus:outline-none focus:ring focus:ring-amber-600"
                placeholder="Enter your shipping address"
                required
              />
            </div>
  
            <!-- City -->
            <div>
              <label for="city" class="block text-sm font-medium mb-1">City</label>
              <input
                v-model="shippingDetails.city"
                type="text"
                id="city"
                class="w-full px-4 py-2 rounded-md bg-gray-700 text-gray-200 focus:outline-none focus:ring focus:ring-amber-600"
                placeholder="Enter your city"
                required
              />
            </div>
  
            <!-- Postal Code -->
            <div>
              <label for="postalCode" class="block text-sm font-medium mb-1">Postal Code</label>
              <input
                v-model="shippingDetails.postalCode"
                type="text"
                id="postalCode"
                class="w-full px-4 py-2 rounded-md bg-gray-700 text-gray-200 focus:outline-none focus:ring focus:ring-amber-600"
                placeholder="Enter your postal code"
                required
              />
            </div>
  
            <!-- Phone Number -->
            <div>
              <label for="phoneNumber" class="block text-sm font-medium mb-1">Phone Number</label>
              <input
                v-model="shippingDetails.phoneNumber"
                type="text"
                id="phoneNumber"
                class="w-full px-4 py-2 rounded-md bg-gray-700 text-gray-200 focus:outline-none focus:ring focus:ring-amber-600"
                placeholder="Enter your phone number"
                required
              />
            </div>
  
            <!-- Submit Button -->
            <button
              type="submit"
              class="w-full bg-amber-600 text-gray-900 hover:bg-amber-700 font-semibold rounded-lg px-4 py-2"
            >
              Place Order
            </button>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        cartItems: [
          // Mock cart items; replace this with dynamic data from your store or API
          {
            id: 1,
            name: "Product 1",
            image: "https://via.placeholder.com/100",
            price: 50.0,
            quantity: 2,
          },
          {
            id: 2,
            name: "Product 2",
            image: "https://via.placeholder.com/100",
            price: 30.0,
            quantity: 1,
          },
        ],
        shippingDetails: {
          fullName: "",
          address: "",
          city: "",
          postalCode: "",
          phoneNumber: "",
        },
      };
    },
    computed: {
      totalPrice() {
        return this.cartItems.reduce((total, item) => total + item.price * item.quantity, 0);
      },
    },
    methods: {
      handleCheckout() {
        // Validate shipping details
        if (!this.shippingDetails.fullName || !this.shippingDetails.address || !this.shippingDetails.city || !this.shippingDetails.postalCode || !this.shippingDetails.phoneNumber) {
          alert("Please fill out all required fields.");
          return;
        }
  
        // Mock API call to place order
        const orderData = {
          cartItems: this.cartItems,
          shippingDetails: this.shippingDetails,
          totalPrice: this.totalPrice,
        };
  
        console.log("Order placed:", orderData);
        alert("Order placed successfully!");
        
        // Reset the form and cart
        this.shippingDetails = {
          fullName: "",
          address: "",
          city: "",
          postalCode: "",
          phoneNumber: "",
        };
        this.cartItems = [];
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add custom styles here if necessary */
  </style>
  