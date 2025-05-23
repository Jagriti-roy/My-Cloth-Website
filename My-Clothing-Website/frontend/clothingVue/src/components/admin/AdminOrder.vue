<template>
    <div class="bg-stone-900 min-h-screen text-gray-200 font-sans">
      <div class="max-w-7xl mx-auto px-6 py-12">
        <h1 class="text-3xl font-bold mb-8 text-amber-700 text-center">Admin - Order Management</h1>
        <div class="overflow-x-auto bg-stone-800 rounded-lg shadow-lg p-4">
          <table class="w-full border-collapse bg-stone-800">
            <thead>
              <tr class="text-left text-gray-300 bg-stone-900">
                <th class="py-3 px-4 border-b border-gray-600">ID</th>
                <th class="py-3 px-4 border-b border-gray-600">User ID</th>
                <th class="py-3 px-4 border-b border-gray-600">Status</th>
                <th class="py-3 px-4 border-b border-gray-600">Created At</th>
                <th class="py-3 px-4 border-b border-gray-600">Order Items</th>
                <th class="py-3 px-4 border-b border-gray-600">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="order in orders"
                :key="order.id"
                class="hover:bg-stone-700 transition duration-200"
              >
                <td class="py-3 px-4 border-b border-gray-600">{{ order.id }}</td>
                <td class="py-3 px-4 border-b border-gray-600">{{ order.user_id }}</td>
                <td class="py-3 px-4 border-b border-gray-600">
                  <span
                    :class="[
                      'px-3 py-1 rounded-full text-sm font-semibold',
                      order.status === 'Pending'
                        ? 'bg-yellow-600 text-yellow-100'
                        : order.status === 'Completed'
                        ? 'bg-green-600 text-green-100'
                        : 'bg-red-600 text-red-100',
                    ]"
                  >
                    {{ order.status }}
                  </span>
                </td>
                <td class="py-3 px-4 border-b border-gray-600">
                  {{ new Date(order.created_at).toLocaleString() }}
                </td>
                <td class="py-3 px-4 border-b border-gray-600">
                  <button
                    class="bg-amber-600 hover:bg-amber-500 text-gray-900 px-4 py-2 rounded-md shadow-md transition"
                    @click="viewOrderItems(order.id)"
                  >
                    View Items
                  </button>
                </td>
                <td class="py-3 px-4 border-b border-gray-600">
                  <div class="flex space-x-2">
                    <button
                      class="bg-green-600 hover:bg-green-500 text-gray-100 px-4 py-2 rounded-md shadow-md transition"
                      @click="markAsCompleted(order.id)"
                    >
                      Mark Completed
                    </button>
                    <button
                      class="bg-red-600 hover:bg-red-500 text-gray-100 px-4 py-2 rounded-md shadow-md transition"
                      @click="deleteOrder(order.id)"
                    >
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
              <tr v-if="orders.length === 0">
                <td colspan="6" class="py-4 px-4 text-center text-gray-400">
                  No orders found.
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
        orders: [], // Replace with your fetched order data
      };
    },
    methods: {
      viewOrderItems(orderId) {
        // Logic to view items of a specific order
        console.log("View items for order:", orderId);
      },
      markAsCompleted(orderId) {
        // Logic to mark order as completed
        console.log("Mark order as completed:", orderId);
      },
      deleteOrder(orderId) {
        // Logic to delete an order
        console.log("Delete order:", orderId);
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add custom styles if needed */
  </style>
  