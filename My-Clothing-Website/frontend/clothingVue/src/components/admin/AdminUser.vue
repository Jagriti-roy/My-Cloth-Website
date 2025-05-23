<template>
    <div class="bg-stone-900 min-h-screen p-8">
      <h1 class="text-3xl font-bold text-gray-100 mb-6">Admin User Management</h1>
  
      <div class="overflow-x-auto">
        <table class="min-w-full bg-stone-800 rounded-lg shadow-md overflow-hidden">
          <thead class="bg-stone-950 text-amber-100">
            <tr>
              <th class="text-left px-6 py-3 text-sm font-semibold uppercase">ID</th>
              <th class="text-left px-6 py-3 text-sm font-semibold uppercase">Name</th>
              <th class="text-left px-6 py-3 text-sm font-semibold uppercase">Email</th>
              <th class="text-left px-6 py-3 text-sm font-semibold uppercase">Phone</th>
              <th class="text-left px-6 py-3 text-sm font-semibold uppercase">Address</th>
              <th class="text-left px-6 py-3 text-sm font-semibold uppercase">Active</th>
              <th class="text-left px-6 py-3 text-sm font-semibold uppercase">Actions</th>
            </tr>
          </thead>
  
          <tbody>
            <tr
              v-for="user in users"
              :key="user.user_id"
              class="hover:bg-stone-700 text-gray-300 border-b border-stone-700"
            >
              <td class="px-6 py-4 text-sm">{{ user.user_id }}</td>
              <td class="px-6 py-4 text-sm">{{ user.name }}</td>
              <td class="px-6 py-4 text-sm">{{ user.email }}</td>
              <td class="px-6 py-4 text-sm">{{ user.phone_number }}</td>
              <td class="px-6 py-4 text-sm">{{ user.address }}</td>
              <td class="px-6 py-4 text-sm">
                <span
                  class="px-2 py-1 rounded-full text-xs font-semibold"
                  :class="user.active ? 'bg-amber-100 text-stone-800' : 'bg-gray-500 text-white'"
                >
                  {{ user.active ? 'Active' : 'Inactive' }}
                </span>
              </td>
              <td class="px-6 py-4 text-sm">
                <button
                  class="bg-amber-700 hover:bg-amber-600 text-white px-3 py-1 rounded shadow-md"
                  @click="editUser(user)"
                >
                  Edit
                </button>
                <button
                  class="ml-2 bg-red-600 hover:bg-red-500 text-white px-3 py-1 rounded shadow-md"
                  @click="deleteUser(user.user_id)"
                >
                  Delete
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
</template>
  
  <script setup>
    import { ref } from 'vue';
    import { onMounted } from 'vue';
    import axiosInstance from "../../axios";

    const users = ref([]);

    const fetchUsers = async () => {
      try {
        const response = await axiosInstance.get('/getUsers'); // Update endpoint based on your backend route
        users.value = response.data; // Populate the users array with data from the backend
        console.log("Fetched users:", users.value);
      } catch (error) {
        console.error("Error fetching users:", error);
        alert("Failed to fetch users. Please try again later.");
      }
    };

    onMounted(() => {
      fetchUsers(); // Fetch users on component mount
    });

    const editUser = (user) => {
      alert(`Editing user: ${user.name}`);
    };

    const deleteUser = (userId) => {
      if (confirm("Are you sure you want to delete this user?")) {
        users.value = users.value.filter((user) => user.id !== userId);
      }
    };
  </script>

  
  <style scoped>
  /* Add custom styles here if needed */
  </style>
  