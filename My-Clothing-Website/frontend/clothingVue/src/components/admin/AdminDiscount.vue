<template>
    <div class="bg-stone-900 min-h-screen text-gray-200 font-sans">
      <div class="max-w-7xl mx-auto px-6 py-12">
        <h1 class="text-3xl font-bold mb-8 text-amber-700 text-center">Admin - Discount Management</h1>
        <div class="overflow-x-auto bg-stone-800 rounded-lg shadow-lg p-4">
          <table class="w-full border-collapse bg-stone-800">
            <thead>
              <tr class="text-left text-gray-300 bg-stone-900">
                <th class="py-3 px-4 border-b border-gray-600">ID</th>
                <th class="py-3 px-4 border-b border-gray-600">Product ID</th>
                <th class="py-3 px-4 border-b border-gray-600">Amount</th>
                <th class="py-3 px-4 border-b border-gray-600">Type</th>
                <th class="py-3 px-4 border-b border-gray-600">Valid Until</th>
                <th class="py-3 px-4 border-b border-gray-600">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="discount in discounts"
                :key="discount.id"
                class="hover:bg-stone-700 transition duration-200"
              >
                <td class="py-3 px-4 border-b border-gray-600">{{ discount.id }}</td>
                <td class="py-3 px-4 border-b border-gray-600">{{ discount.product_id }}</td>
                <td class="py-3 px-4 border-b border-gray-600">
                  {{ discount.discount_type === 'Percentage' ? `${discount.amount}%` : `$${discount.amount}` }}
                </td>
                <td class="py-3 px-4 border-b border-gray-600">{{ discount.discount_type }}</td>
                <td class="py-3 px-4 border-b border-gray-600">
                  {{ discount.valid_until
                    ? new Date(discount.valid_until).toLocaleDateString()
                    : "N/A" }}
                </td>
                <td class="py-3 px-4 border-b border-gray-600">
                  <div class="flex space-x-2">
                    <button
                      class="bg-blue-600 hover:bg-blue-500 text-gray-100 px-4 py-2 rounded-md shadow-md transition"
                      @click="editDiscount(discount.id)"
                    >
                      Edit
                    </button>
                    <button
                      class="bg-red-600 hover:bg-red-500 text-gray-100 px-4 py-2 rounded-md shadow-md transition"
                      @click="deleteDiscount(discount.id)"
                    >
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
              <tr v-if="discounts.length === 0">
                <td colspan="6" class="py-4 px-4 text-center text-gray-400">
                  No discount records found.
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
        discounts: [], // Replace with your fetched discount data
      };
    },
    methods: {
      editDiscount(discountId) {
        // Logic to edit a discount record
        console.log("Edit discount:", discountId);
      },
      deleteDiscount(discountId) {
        // Logic to delete a discount record
        console.log("Delete discount:", discountId);
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add custom styles if needed */
  </style>
  