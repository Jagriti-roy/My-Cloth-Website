<template>
    <div class="bg-stone-900 min-h-screen text-gray-200 font-sans">
      <div class="max-w-7xl mx-auto px-6 py-12">
        <h1 class="text-3xl font-bold mb-8 text-amber-700 text-center">Admin - Cart Management</h1>
        <div class="overflow-x-auto bg-stone-800 rounded-lg shadow-lg p-4">
          <table class="w-full border-collapse bg-stone-800">
            <thead>
              <tr class="text-left text-gray-300 bg-stone-900">
                <th class="py-3 px-4 border-b border-gray-600">Cart ID</th>
                <th class="py-3 px-4 border-b border-gray-600">User ID</th>
                <th class="py-3 px-4 border-b border-gray-600">Product ID</th>
                <th class="py-3 px-4 border-b border-gray-600">Product Name</th>
                <th class="py-3 px-4 border-b border-gray-600">Quantity</th>
                <th class="py-3 px-4 border-b border-gray-600">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="cart in carts"
                :key="cart.id"
                class="hover:bg-stone-700 transition duration-200"
              >
                <td class="py-3 px-4 border-b border-gray-600">{{ cart.id }}</td>
                <td class="py-3 px-4 border-b border-gray-600">{{ cart.user_id }}</td>
                <td class="py-3 px-4 border-b border-gray-600">{{ cart.product_id }}</td>
                <td class="py-3 px-4 border-b border-gray-600">{{ getProductName(cart.product_id) }}</td>
                <td class="py-3 px-4 border-b border-gray-600">{{ cart.quantity }}</td>
                <td class="py-3 px-4 border-b border-gray-600">
                  <div class="flex space-x-2">
                    <button
                      class="bg-red-600 hover:bg-red-500 text-gray-100 px-4 py-2 rounded-md shadow-md transition"
                      @click="removeFromCart(cart.id)"
                    >
                      Remove
                    </button>
                    <button
                      class="bg-yellow-600 hover:bg-yellow-500 text-gray-100 px-4 py-2 rounded-md shadow-md transition"
                      @click="updateQuantity(cart.id)"
                    >
                      Update Quantity
                    </button>
                  </div>
                </td>
              </tr>
              <tr v-if="carts.length === 0">
                <td colspan="6" class="py-4 px-4 text-center text-gray-400">
                  No cart records found.
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        carts: [], // Replace with your fetched cart data
      };
    },
    methods: {
      // Example method to remove item from cart
      removeFromCart(cartId) {
        console.log("Remove item from cart with ID:", cartId);
        // Logic to remove cart entry
      },
      // Example method to update quantity
      updateQuantity(cartId) {
        const newQuantity = prompt("Enter new quantity:");
        if (newQuantity && !isNaN(newQuantity) && newQuantity > 0) {
          console.log("Update cart item ID:", cartId, "with new quantity:", newQuantity);
          // Logic to update the cart quantity
        } else {
          alert("Invalid quantity entered.");
        }
      },
      // Placeholder method for retrieving product name based on product_id
      getProductName(productId) {
        // You can fetch this data from your products list or API
        const product = this.products.find((p) => p.id === productId);
        return product ? product.name : "Unknown Product";
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add custom styles if needed */
  </style>
  