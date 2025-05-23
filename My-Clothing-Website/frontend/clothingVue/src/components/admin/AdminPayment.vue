<template>
    <div class="bg-stone-900 min-h-screen text-gray-200 font-sans">
      <div class="max-w-7xl mx-auto px-6 py-12">
        <h1 class="text-3xl font-bold mb-8 text-amber-700 text-center">Admin - Payment Management</h1>
        <div class="overflow-x-auto bg-stone-800 rounded-lg shadow-lg p-4">
          <table class="w-full border-collapse bg-stone-800">
            <thead>
              <tr class="text-left text-gray-300 bg-stone-900">
                <th class="py-3 px-4 border-b border-gray-600">ID</th>
                <th class="py-3 px-4 border-b border-gray-600">Order ID</th>
                <th class="py-3 px-4 border-b border-gray-600">Transaction ID</th>
                <th class="py-3 px-4 border-b border-gray-600">Status</th>
                <th class="py-3 px-4 border-b border-gray-600">Payment Method</th>
                <th class="py-3 px-4 border-b border-gray-600">Created At</th>
                <th class="py-3 px-4 border-b border-gray-600">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="payment in payments"
                :key="payment.id"
                class="hover:bg-stone-700 transition duration-200"
              >
                <td class="py-3 px-4 border-b border-gray-600">{{ payment.id }}</td>
                <td class="py-3 px-4 border-b border-gray-600">{{ payment.order_id }}</td>
                <td class="py-3 px-4 border-b border-gray-600">{{ payment.transaction_id }}</td>
                <td class="py-3 px-4 border-b border-gray-600">
                  <span
                    :class="[
                      'px-3 py-1 rounded-full text-sm font-semibold',
                      payment.status === 'Pending'
                        ? 'bg-yellow-600 text-yellow-100'
                        : payment.status === 'Completed'
                        ? 'bg-green-600 text-green-100'
                        : 'bg-red-600 text-red-100',
                    ]"
                  >
                    {{ payment.status }}
                  </span>
                </td>
                <td class="py-3 px-4 border-b border-gray-600">{{ payment.payment_method }}</td>
                <td class="py-3 px-4 border-b border-gray-600">
                  {{ new Date(payment.created_at).toLocaleString() }}
                </td>
                <td class="py-3 px-4 border-b border-gray-600">
                  <div class="flex space-x-2">
                    <button
                      class="bg-green-600 hover:bg-green-500 text-gray-100 px-4 py-2 rounded-md shadow-md transition"
                      @click="markAsCompleted(payment.id)"
                    >
                      Mark Completed
                    </button>
                    <button
                      class="bg-red-600 hover:bg-red-500 text-gray-100 px-4 py-2 rounded-md shadow-md transition"
                      @click="deletePayment(payment.id)"
                    >
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
              <tr v-if="payments.length === 0">
                <td colspan="7" class="py-4 px-4 text-center text-gray-400">
                  No payments found.
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
        payments: [], // Replace with your fetched payment data
      };
    },
    methods: {
      markAsCompleted(paymentId) {
        // Logic to mark payment as completed
        console.log("Mark payment as completed:", paymentId);
      },
      deletePayment(paymentId) {
        // Logic to delete a payment
        console.log("Delete payment:", paymentId);
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add custom styles if needed */
  </style>
  