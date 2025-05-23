<template>
    <div class="bg-stone-900 min-h-screen text-gray-200 font-sans">
      <div class="max-w-7xl mx-auto px-6 py-12">
        <h1 class="text-3xl font-bold mb-8 text-amber-700 text-center">Admin - Notification Management</h1>
  
        <div class="overflow-x-auto bg-stone-800 rounded-lg shadow-lg p-4">
          <table class="w-full border-collapse bg-stone-800">
            <thead>
              <tr class="text-left text-gray-300 bg-stone-900">
                <th class="py-3 px-4 border-b border-gray-600">Notification ID</th>
                <th class="py-3 px-4 border-b border-gray-600">Title</th>
                <th class="py-3 px-4 border-b border-gray-600">Message</th>
                <th class="py-3 px-4 border-b border-gray-600">Status</th>
                <th class="py-3 px-4 border-b border-gray-600">Created At</th>
                <th class="py-3 px-4 border-b border-gray-600">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="notification in notifications"
                :key="notification.id"
                class="hover:bg-stone-700 transition duration-200"
              >
                <td class="py-3 px-4 border-b border-gray-600">{{ notification.id }}</td>
                <td class="py-3 px-4 border-b border-gray-600">{{ notification.title }}</td>
                <td class="py-3 px-4 border-b border-gray-600">{{ notification.message }}</td>
                <td class="py-3 px-4 border-b border-gray-600">
                  <span class="px-2 py-1 rounded-full text-xs font-semibold"
                    :class="{
                      'bg-amber-100 text-stone-800': notification.status === 'Active',
                      'bg-gray-500 text-white': notification.status === 'Inactive',
                    }"
                    >{{ notification.status }}</span
                  >
                </td>
                <td class="py-3 px-4 border-b border-gray-600">{{ formatDate(notification.created_at) }}</td>
                <td class="py-3 px-4 border-b border-gray-600">
                  <div class="flex space-x-2">
                    <button
                      class="bg-amber-700 hover:bg-amber-600 text-white px-4 py-2 rounded-md shadow-md transition"
                      @click="editNotification(notification.id)"
                    >
                      Edit
                    </button>
                    <button
                      class="ml-2 bg-red-600 hover:bg-red-500 text-white px-4 py-2 rounded-md shadow-md transition"
                      @click="deleteNotification(notification.id)"
                    >
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
              <tr v-if="notifications.length === 0">
                <td colspan="6" class="py-4 px-4 text-center text-gray-400">
                  No notifications found.
                </td>
              </tr>
            </tbody>
          </table>
        </div>
  
        <div
          v-if="isEditModalOpen"
          class="fixed inset-0 flex items-center justify-center z-50 bg-black bg-opacity-50"
        >
          <div class="bg-stone-800 p-6 rounded-lg shadow-lg w-1/3">
            <h2 class="text-2xl font-semibold text-amber-700 mb-4">Edit Notification</h2>
            <form @submit.prevent="saveNotification">
              <div class="mb-4">
                <label class="block text-gray-300" for="title">Title</label>
                <input
                  v-model="editedNotification.title"
                  type="text"
                  id="title"
                  class="w-full px-4 py-2 mt-1 bg-stone-700 text-gray-200 rounded-md"
                  required
                />
              </div>
              <div class="mb-4">
                <label class="block text-gray-300" for="message">Message</label>
                <textarea
                  v-model="editedNotification.message"
                  id="message"
                  class="w-full px-4 py-2 mt-1 bg-stone-700 text-gray-200 rounded-md"
                  required
                ></textarea>
              </div>
              <div class="mb-4">
                <label class="block text-gray-300" for="status">Status</label>
                <select
                  v-model="editedNotification.status"
                  id="status"
                  class="w-full px-4 py-2 mt-1 bg-stone-700 text-gray-200 rounded-md"
                >
                  <option value="Active">Active</option>
                  <option value="Inactive">Inactive</option>
                </select>
              </div>
              <div class="flex justify-end">
                <button
                  type="submit"
                  class="bg-green-600 hover:bg-green-500 text-gray-100 px-4 py-2 rounded-md shadow-md transition"
                >
                  Save
                </button>
                <button
                  type="button"
                  class="bg-gray-600 hover:bg-gray-500 text-gray-100 px-4 py-2 rounded-md shadow-md ml-2"
                  @click="closeEditModal"
                >
                  Cancel
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        notifications: [],
        isEditModalOpen: false,
        editedNotification: {
          id: null,
          title: '',
          message: '',
          status: 'Active',
          created_at: '',
        },
      };
    },
    methods: {
      formatDate(date) {
        const d = new Date(date);
        return d.toLocaleString();
      },
  
      editNotification(id) {
        const notification = this.notifications.find((n) => n.id === id);
        this.editedNotification = { ...notification };
        this.isEditModalOpen = true;
      },
  
      closeEditModal() {
        this.isEditModalOpen = false;
      },
  
      saveNotification() {
        console.log('Saving notification with ID:', this.editedNotification.id);
        this.isEditModalOpen = false;
      },
  
      deleteNotification(id) {
        console.log('Deleting notification with ID:', id);
      },
    },
    mounted() {
      this.notifications = [
        {
          id: 1,
          title: 'New Product Launch',
          message: 'We have launched a new product. Check it out!',
          status: 'Active',
          created_at: '2025-01-16T12:00:00Z',
        },
        {
          id: 2,
          title: 'System Maintenance',
          message: 'The system will be down for maintenance on 18th January.',
          status: 'Inactive',
          created_at: '2025-01-14T10:00:00Z',
        },
      ];
    },
  };
  </script>
