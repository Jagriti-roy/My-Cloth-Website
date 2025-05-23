<template>
    <div class="bg-stone-900 min-h-screen text-gray-200 font-sans">
      <div class="max-w-7xl mx-auto px-6 py-12">
        <h1 class="text-3xl font-bold mb-8 text-amber-700 text-center">Admin - Shipping Management</h1>
        <div class="overflow-x-auto bg-stone-800 rounded-lg shadow-lg p-4">
          <table class="w-full border-collapse bg-stone-800">
            <thead>
              <tr class="text-left text-gray-300 bg-stone-900">
                <th class="py-3 px-4 border-b border-gray-600">ID</th>
                <th class="py-3 px-4 border-b border-gray-600">Order ID</th>
                <th class="py-3 px-4 border-b border-gray-600">Provider</th>
                <th class="py-3 px-4 border-b border-gray-600">Tracking Number</th>
                <th class="py-3 px-4 border-b border-gray-600">Status</th>
                <th class="py-3 px-4 border-b border-gray-600">Estimated Delivery</th>
                <th class="py-3 px-4 border-b border-gray-600">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="shipping in shippings"
                :key="shipping.id"
                class="hover:bg-stone-700 transition duration-200"
              >
                <td class="py-3 px-4 border-b border-gray-600">{{ shipping.id }}</td>
                <td class="py-3 px-4 border-b border-gray-600">{{ shipping.order_id }}</td>
                <td class="py-3 px-4 border-b border-gray-600">{{ shipping.provider }}</td>
                <td class="py-3 px-4 border-b border-gray-600">
                  {{ shipping.tracking_number || "N/A" }}
                </td>
                <td class="py-3 px-4 border-b border-gray-600">
                  <span
                    :class="[
                      'px-3 py-1 rounded-full text-sm font-semibold',
                      shipping.status === 'Pending'
                        ? 'bg-yellow-600 text-yellow-100'
                        : shipping.status === 'Shipped'
                        ? 'bg-blue-600 text-blue-100'
                        : shipping.status === 'Delivered'
                        ? 'bg-green-600 text-green-100'
                        : 'bg-red-600 text-red-100',
                    ]"
                  >
                    {{ shipping.status }}
                  </span>
                </td>
                <td class="py-3 px-4 border-b border-gray-600">
                  {{ shipping.estimated_delivery
                    ? new Date(shipping.estimated_delivery).toLocaleDateString()
                    : "N/A" }}
                </td>
                <td class="py-3 px-4 border-b border-gray-600">
                  <div class="flex space-x-2">
                    <button
                      class="bg-blue-600 hover:bg-blue-500 text-gray-100 px-4 py-2 rounded-md shadow-md transition"
                      @click="updateShippingStatus(shipping.id)"
                    >
                      Update Status
                    </button>
                    <button
                      class="bg-red-600 hover:bg-red-500 text-gray-100 px-4 py-2 rounded-md shadow-md transition"
                      @click="deleteShipping(shipping.id)"
                    >
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
              <tr v-if="shippings.length === 0">
                <td colspan="7" class="py-4 px-4 text-center text-gray-400">
                  No shipping records found.
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
        shippings: [], // Replace with your fetched shipping data
      };
    },
    methods: {
      updateShippingStatus(shippingId) {
        // Logic to update the shipping status
        console.log("Update shipping status:", shippingId);
      },
      deleteShipping(shippingId) {
        // Logic to delete a shipping record
        console.log("Delete shipping record:", shippingId);
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add custom styles if needed */
  </style>
  