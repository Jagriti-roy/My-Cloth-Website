<template>
    <div class="bg-stone-900 min-h-screen text-gray-200 font-sans">
      <div class="max-w-7xl mx-auto px-6 py-12">
        <h1 class="text-3xl font-bold mb-8 text-amber-700 text-center">Admin - Wishlist Management</h1>
        <div class="overflow-x-auto bg-stone-800 rounded-lg shadow-lg p-4">
          <table class="w-full border-collapse bg-stone-800">
            <thead>
              <tr class="text-left text-gray-300 bg-stone-900">
                <th class="py-3 px-4 border-b border-gray-600">ID</th>
                <th class="py-3 px-4 border-b border-gray-600">User ID</th>
                <th class="py-3 px-4 border-b border-gray-600">Product ID</th>
                <th class="py-3 px-4 border-b border-gray-600">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="wishlistItem in wishlist"
                :key="wishlistItem.id"
                class="hover:bg-stone-700 transition duration-200"
              >
                <td class="py-3 px-4 border-b border-gray-600">{{ wishlistItem.id }}</td>
                <td class="py-3 px-4 border-b border-gray-600">{{ wishlistItem.user_id }}</td>
                <td class="py-3 px-4 border-b border-gray-600">{{ wishlistItem.product_id }}</td>
                <td class="py-3 px-4 border-b border-gray-600">
                  <div class="flex space-x-2">
                    <button
                      class="bg-red-600 hover:bg-red-500 text-gray-100 px-4 py-2 rounded-md shadow-md transition"
                      @click="deleteWishlistItem(wishlistItem.id)"
                    >
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
              <tr v-if="wishlist.length === 0">
                <td colspan="4" class="py-4 px-4 text-center text-gray-400">
                  No wishlist records found.
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
        wishlist: [], // Replace with your fetched wishlist data
      };
    },
    methods: {
      deleteWishlistItem(wishlistId) {
        // Logic to delete a wishlist item
        console.log("Delete wishlist item:", wishlistId);
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add custom styles if needed */
  </style>
  