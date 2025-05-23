<template>
    <div class="bg-stone-900 min-h-screen text-gray-200 font-sans">
      <div class="max-w-7xl mx-auto px-6 py-12">
        <h1 class="text-3xl font-bold mb-8 text-amber-700 text-center">Admin - Product Management</h1>
        <div class="overflow-x-auto bg-stone-800 rounded-lg shadow-lg p-4">
          <table class="w-full border-collapse bg-stone-800">
            <thead>
              <tr class="text-left text-gray-300 bg-stone-900">
                <th class="py-3 px-4 border-b border-gray-600">ID</th>
                <th class="py-3 px-4 border-b border-gray-600">Name</th>
                <th class="py-3 px-4 border-b border-gray-600">Description</th>
                <th class="py-3 px-4 border-b border-gray-600">Category</th>
                <th class="py-3 px-4 border-b border-gray-600">Price</th>
                <th class="py-3 px-4 border-b border-gray-600">Discount</th>
                <th class="py-3 px-4 border-b border-gray-600">SKU</th>
                <th class="py-3 px-4 border-b border-gray-600">Image</th>
                <th class="py-3 px-4 border-b border-gray-600">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr 
                v-for="product in products" 
                :key="product.id" 
                class="hover:bg-stone-700 transition duration-200">
                <td class="py-3 px-4 border-b border-gray-600">{{ product.id }}</td>
                <td class="py-3 px-4 border-b border-gray-600">{{ product.name }}</td>
                <td class="py-3 px-4 border-b border-gray-600 truncate" :title="product.description">
                  {{ product.description }}
                </td>
                <td class="py-3 px-4 border-b border-gray-600">{{ product.category }}</td>
                <td class="py-3 px-4 border-b border-gray-600">${{ product.price.toFixed(2) }}</td>
                <td class="py-3 px-4 border-b border-gray-600">{{ product.discount }}%</td>
                <td class="py-3 px-4 border-b border-gray-600">{{ product.sku }}</td>
                <td class="py-3 px-4 border-b border-gray-600">
                  <img :src="product.image" alt="Product Image" class="h-12 w-12 object-cover rounded-md" />
                </td>
                <td class="py-3 px-4 border-b border-gray-600">
                  <div class="flex space-x-2">
                    <button
                      class="bg-amber-600 hover:bg-amber-500 text-gray-900 px-4 py-2 rounded-md shadow-md transition"
                      @click="editProduct(product)"
                    >
                      Edit
                    </button>
                    <button
                      class="bg-red-600 hover:bg-red-500 text-gray-100 px-4 py-2 rounded-md shadow-md transition"
                      @click="deleteProduct(product.id)"
                    >
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
              <tr v-if="products.length === 0">
                <td colspan="9" class="py-4 px-4 text-center text-gray-400">No products found.</td>
              </tr>
            </tbody>
          </table>
        </div>
        <button
          class="mt-6 bg-amber-700 hover:bg-amber-600 text-gray-900 font-semibold py-3 px-6 rounded-md shadow-md transition"
          @click="addProduct"
        >
          Add New Product
        </button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        products: [], // Replace with your fetched product data
      };
    },
    methods: {
      addProduct() {
        // Logic for adding a product
        console.log("Add Product");
      },
      editProduct(product) {
        // Logic for editing a product
        console.log("Edit Product:", product);
      },
      deleteProduct(productId) {
        // Logic for deleting a product
        console.log("Delete Product:", productId);
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add custom styles if needed */
  </style>
  