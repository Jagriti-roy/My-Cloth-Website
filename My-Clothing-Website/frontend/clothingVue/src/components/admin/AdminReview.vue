<template>
    <div class="bg-stone-900 min-h-screen text-gray-200 font-sans">
      <div class="max-w-7xl mx-auto px-6 py-12">
        <h1 class="text-3xl font-bold mb-8 text-amber-700 text-center">Admin - Review Management</h1>
        <div class="overflow-x-auto bg-stone-800 rounded-lg shadow-lg p-4">
          <table class="w-full border-collapse bg-stone-800">
            <thead>
              <tr class="text-left text-gray-300 bg-stone-900">
                <th class="py-3 px-4 border-b border-gray-600">ID</th>
                <th class="py-3 px-4 border-b border-gray-600">User ID</th>
                <th class="py-3 px-4 border-b border-gray-600">Product ID</th>
                <th class="py-3 px-4 border-b border-gray-600">Rating</th>
                <th class="py-3 px-4 border-b border-gray-600">Comment</th>
                <th class="py-3 px-4 border-b border-gray-600">Created At</th>
                <th class="py-3 px-4 border-b border-gray-600">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="review in reviews"
                :key="review.id"
                class="hover:bg-stone-700 transition duration-200"
              >
                <td class="py-3 px-4 border-b border-gray-600">{{ review.id }}</td>
                <td class="py-3 px-4 border-b border-gray-600">{{ review.user_id }}</td>
                <td class="py-3 px-4 border-b border-gray-600">{{ review.product_id }}</td>
                <td class="py-3 px-4 border-b border-gray-600">{{ review.rating }}</td>
                <td class="py-3 px-4 border-b border-gray-600">
                  {{ review.comment ? review.comment : "No comment" }}
                </td>
                <td class="py-3 px-4 border-b border-gray-600">
                  {{ new Date(review.created_at).toLocaleString() }}
                </td>
                <td class="py-3 px-4 border-b border-gray-600">
                  <div class="flex space-x-2">
                    <button
                      class="bg-blue-600 hover:bg-blue-500 text-gray-100 px-4 py-2 rounded-md shadow-md transition"
                      @click="editReview(review.id)"
                    >
                      Edit
                    </button>
                    <button
                      class="bg-red-600 hover:bg-red-500 text-gray-100 px-4 py-2 rounded-md shadow-md transition"
                      @click="deleteReview(review.id)"
                    >
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
              <tr v-if="reviews.length === 0">
                <td colspan="7" class="py-4 px-4 text-center text-gray-400">
                  No review records found.
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
        reviews: [], // Replace with your fetched review data
      };
    },
    methods: {
      editReview(reviewId) {
        // Logic to edit a review
        console.log("Edit review:", reviewId);
      },
      deleteReview(reviewId) {
        // Logic to delete a review
        console.log("Delete review:", reviewId);
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add custom styles if needed */
  </style>
  