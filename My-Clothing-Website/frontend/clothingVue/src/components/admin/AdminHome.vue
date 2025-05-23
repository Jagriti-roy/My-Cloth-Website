<template>
    <div class="bg-stone-900 min-h-screen text-gray-200 font-sans">
      <div class="max-w-7xl mx-auto px-6 py-12">
        <h1 class="text-3xl font-bold text-amber-700 mb-8 text-center">Admin Dashboard</h1>
        
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          <!-- Total Users -->
          <div class="bg-stone-800 p-6 rounded-lg shadow-md hover:shadow-lg transition duration-300">
            <div class="flex items-center justify-between">
              <div class="text-amber-500 text-xl font-semibold">Total Users</div>
              <div class="text-6xl font-bold text-gray-100">{{ totalUsers }}</div>
            </div>
            <p class="text-gray-400 mt-2">Total number of registered users in the system.</p>
          </div>
  
          <!-- Total Orders -->
          <div class="bg-stone-800 p-6 rounded-lg shadow-md hover:shadow-lg transition duration-300">
            <div class="flex items-center justify-between">
              <div class="text-amber-500 text-xl font-semibold">Total Orders</div>
              <div class="text-6xl font-bold text-gray-100">{{ totalOrders }}</div>
            </div>
            <p class="text-gray-400 mt-2">Total number of orders placed.</p>
          </div>
  
          <!-- Total Revenue -->
          <div class="bg-stone-800 p-6 rounded-lg shadow-md hover:shadow-lg transition duration-300">
            <div class="flex items-center justify-between">
              <div class="text-amber-500 text-xl font-semibold">Total Revenue</div>
              <div class="text-6xl font-bold text-gray-100">${{ totalRevenue }}</div>
            </div>
            <p class="text-gray-400 mt-2">Total revenue from all orders.</p>
          </div>
          
          <!-- Pending Orders -->
          <div class="bg-stone-800 p-6 rounded-lg shadow-md hover:shadow-lg transition duration-300">
            <div class="flex items-center justify-between">
              <div class="text-amber-500 text-xl font-semibold">Pending Orders</div>
              <div class="text-6xl font-bold text-gray-100">{{ pendingOrders }}</div>
            </div>
            <p class="text-gray-400 mt-2">Orders that are pending and need to be processed.</p>
          </div>
  
          <!-- Total Products -->
          <div class="bg-stone-800 p-6 rounded-lg shadow-md hover:shadow-lg transition duration-300">
            <div class="flex items-center justify-between">
              <div class="text-amber-500 text-xl font-semibold">Total Products</div>
              <div class="text-6xl font-bold text-gray-100">{{ totalProducts }}</div>
            </div>
            <p class="text-gray-400 mt-2">Total number of products in your store.</p>
          </div>
  
          <!-- Total Reviews -->
          <div class="bg-stone-800 p-6 rounded-lg shadow-md hover:shadow-lg transition duration-300">
            <div class="flex items-center justify-between">
              <div class="text-amber-500 text-xl font-semibold">Total Reviews</div>
              <div class="text-6xl font-bold text-gray-100">{{ totalReviews }}</div>
            </div>
            <p class="text-gray-400 mt-2">Total number of reviews submitted by users.</p>
          </div>
        </div>
  
        <div class="mt-12">
          <h2 class="text-2xl font-bold text-amber-700 mb-6">Recent Activities</h2>
          <div class="bg-stone-800 rounded-lg shadow-md p-6">
            <div class="overflow-x-auto">
              <table class="w-full border-collapse">
                <thead>
                  <tr class="text-left text-gray-300 bg-stone-900">
                    <th class="py-3 px-4 border-b border-gray-600">Activity</th>
                    <th class="py-3 px-4 border-b border-gray-600">User</th>
                    <th class="py-3 px-4 border-b border-gray-600">Date</th>
                    <th class="py-3 px-4 border-b border-gray-600">Details</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="activity in recentActivities" :key="activity.id" class="hover:bg-stone-700 transition duration-200">
                    <td class="py-3 px-4 border-b border-gray-600">{{ activity.action }}</td>
                    <td class="py-3 px-4 border-b border-gray-600">{{ activity.user.name }}</td>
                    <td class="py-3 px-4 border-b border-gray-600">{{ formatDate(activity.created_at) }}</td>
                    <td class="py-3 px-4 border-b border-gray-600">{{ activity.details }}</td>
                  </tr>
                  <tr v-if="recentActivities.length === 0">
                    <td colspan="4" class="py-4 px-4 text-center text-gray-400">No recent activities.</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        totalUsers: 1200, // Example number
        totalOrders: 350, // Example number
        totalRevenue: 10500, // Example number
        pendingOrders: 10, // Example number
        totalProducts: 200, // Example number
        totalReviews: 500, // Example number
        recentActivities: [], // Example data for recent activities
      };
    },
    methods: {
      // Method to format date (example)
      formatDate(date) {
        const d = new Date(date);
        return d.toLocaleString();
      },
    },
    mounted() {
      // Example of fetching recent activities
      this.recentActivities = [
        {
          id: 1,
          action: 'New order placed',
          user: { name: 'John Doe' },
          created_at: '2025-01-17T10:30:00Z',
          details: 'Order #12345 placed by John Doe',
        },
        {
          id: 2,
          action: 'Product added',
          user: { name: 'Admin' },
          created_at: '2025-01-16T14:00:00Z',
          details: 'New product added to the store',
        },
        {
          id: 3,
          action: 'Product review posted',
          user: { name: 'Jane Smith' },
          created_at: '2025-01-15T16:45:00Z',
          details: 'User Jane Smith posted a review on Product #987',
        },
      ];
    },
  };
  </script>
  
  <style scoped>
  /* Custom styles for the dashboard */
  </style>
  