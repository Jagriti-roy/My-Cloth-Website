<template>
    <div class="bg-stone-900 min-h-screen text-gray-200 font-sans">
      <div class="max-w-7xl mx-auto px-6 py-12">
        <h1 class="text-3xl font-bold text-amber-700 mb-8 text-center">My Orders</h1>
  
        <div v-if="orders.length === 0" class="text-center text-gray-400">
          <p>You have not placed any orders yet.</p>
        </div>
  
        <div v-else class="space-y-6">
          <div
            v-for="order in orders"
            :key="order.id"
            class="bg-stone-800 rounded-lg shadow-md p-6 hover:shadow-lg transition duration-300"
          >
            <div class="flex items-center justify-between">
              <div>
                <p class="text-gray-300 text-sm">Order ID:</p>
                <p class="text-lg font-semibold text-gray-100">{{ order.id }}</p>
              </div>
              <div>
                <p class="text-gray-300 text-sm">Status:</p>
                <p
                  :class="{
                    'text-green-400': order.status === 'Delivered',
                    'text-yellow-400': order.status === 'Pending',
                    'text-red-400': order.status === 'Cancelled',
                  }"
                  class="text-lg font-semibold"
                >
                  {{ order.status }}
                </p>
              </div>
              <div>
                <p class="text-gray-300 text-sm">Total Amount:</p>
                <p class="text-lg font-semibold text-gray-100">${{ order.total.toFixed(2) }}</p>
              </div>
              <button
                class="bg-amber-600 text-gray-900 hover:bg-amber-700 font-semibold rounded-lg px-4 py-2"
                @click="viewOrderDetails(order.id)"
              >
                View Details
              </button>
            </div>
            <p class="text-gray-400 text-sm mt-2">
              Placed on {{ formatDate(order.created_at) }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        orders: [], // List of orders for the user
      };
    },
    methods: {
      // Fetch orders for the logged-in user
      fetchOrders() {
        // Mock data (replace with API call)
        this.orders = [
          {
            id: 12345,
            status: 'Delivered',
            total: 150.5,
            created_at: '2025-01-15T10:00:00Z',
          },
          {
            id: 12346,
            status: 'Pending',
            total: 75.0,
            created_at: '2025-01-16T14:30:00Z',
          },
          {
            id: 12347,
            status: 'Cancelled',
            total: 200.75,
            created_at: '2025-01-14T16:45:00Z',
          },
        ];
      },
      // Navigate to order details page
      viewOrderDetails(orderId) {
        this.$router.push(`/orders/${orderId}`);
      },
      // Format date to a readable format
      formatDate(date) {
        const d = new Date(date);
        return d.toLocaleDateString('en-US', {
          year: 'numeric',
          month: 'long',
          day: 'numeric',
        });
      },
    },
    mounted() {
      this.fetchOrders();
    },
  };
  </script>
  
  <style scoped>
  /* Custom styles for orders page */
  </style>
  