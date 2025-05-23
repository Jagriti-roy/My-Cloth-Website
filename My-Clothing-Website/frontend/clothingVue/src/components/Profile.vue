<template>
    <div>
        <!-- Profile Section -->
        <section class="py-16 px-6 bg-stone-900">
            <div class="max-w-5xl mx-auto">
                <h2 class="text-3xl font-bold mb-8 text-center text-stone-200">Your Profile</h2>

                <!-- Personal Information -->
                <div class="mb-10 bg-stone-200 rounded-lg p-6 shadow-lg">
                    <h3 class="text-xl font-semibold mb-4 text-stone-700">Personal Information</h3>
                    <form @submit.prevent="savePersonalInfo">
                        <div class="grid gap-4 md:grid-cols-2">
                            <div>
                                <label class="block text-sm text-stone-800 mb-1">Name</label>
                                <input v-model="user.name" type="text" class="w-full p-2 rounded bg-stone-800 text-gray-200 border border-gray-600" />
                            </div>
                            <div>
                                <label class="block text-sm text-stone-800 mb-1">Email</label>
                                <input v-model="user.email" type="email" class="w-full p-2 rounded bg-stone-800 text-gray-200 border border-gray-600" disabled />
                            </div>
                            <div>
                                <label class="block text-sm text-stone-800 mb-1">Phone Number</label>
                                <input v-model="user.phone_number" type="text" class="w-full p-2 rounded bg-stone-800 text-gray-200 border border-gray-600" />
                            </div>
                            <div>
                                <label class="block text-sm text-stone-800 mb-1">Address</label>
                                <input v-model="user.address" type="text" class="w-full p-2 rounded bg-stone-800 text-gray-200 border border-gray-600" />
                            </div>
                        </div>
                        <button type="submit" class="mt-6 bg-amber-200 py-2 px-4 rounded text-stone-900 hover:bg-amber-100">Save Changes</button>
                    </form>
                </div>

                <!-- Order History -->
                <div class="mb-10 bg-stone-200 rounded-lg p-6 shadow-lg">
                    <h3 class="text-xl font-semibold mb-4 text-stone-700">Order History</h3>
                    <div v-if="orders.length > 0" class="space-y-4">
                        <div v-for="order in orders" :key="order.id" @click="viewOrderDetails(order.id)" class="bg-stone-500 p-4 rounded-lg cursor-pointer hover:bg-stone-700 transition">
                            <h4 class="font-semibold text-gray-200">Order #{{ order.id }}</h4>
                            <p class="text-gray-400">Status: {{ order.status }}</p>
                            <p class="text-gray-500">Date: {{ new Date(order.created_at).toLocaleDateString() }}</p>
                        </div>
                    </div>
                    <p v-else class="text-center text-gray-400">You have no past orders.</p>
                </div>

                <!-- Wishlist -->
                <div class="bg-stone-200 rounded-lg p-6 shadow-lg">
                    <h3 class="text-xl font-semibold mb-4 text-stone-700">Your Wishlist</h3>
                    <div v-if="wishlist.length > 0" class="grid gap-6 sm:grid-cols-2 md:grid-cols-3">
                        <div v-for="item in wishlist" :key="item.id" class="bg-stone-500 rounded-lg p-4">
                            <img :src="item.image" alt="Product" class="w-full h-40 object-cover rounded-md mb-4" />
                            <h4 class="font-semibold text-lg text-gray-200">{{ item.name }}</h4>
                            <p class="text-amber-600 font-bold mt-2">${{ item.price }}</p>
                            <button @click="addToCart(item)" class="w-full mt-2 py-2 bg-amber-100 text-gray-900 rounded hover:bg-amber-300 transition">Add to Cart</button>
                            <button @click="removeFromWishlist(item)" class="w-full mt-2 py-2 bg-white text-red-600 hover:text-white rounded hover:bg-red-300 transition">Remove</button>
                        </div>
                    </div>
                    <p v-else class="text-center text-gray-400">Your wishlist is empty.</p>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
export default {
    data() {
        return {
            user: {
                name: "Rhythm",
                email: "Rhythm@gmail.com",
                phone_number: "9999999999",
                address: "West Bengal",
            },
            orders: [
                { id: 1, status: "Delivered", created_at: "2023-09-14T15:30:00Z" },
                { id: 2, status: "Pending", created_at: "2023-09-20T12:15:00Z" },
                // Additional orders can be added here
            ],
            wishlist: [
                { id: 1, name: "Product 1", price: 99.99, image: "product1.jpg" },
                { id: 2, name: "Product 2", price: 79.99, image: "product2.jpg" },
                // More wishlist items can be added here
            ]
        };
    },
    methods: {
        savePersonalInfo() {
            alert("Your information has been saved.");
        },
        viewOrderDetails(orderId) {
            alert(`Viewing details for order #${orderId}`);
        },
        addToCart(item) {
            alert(`${item.name} added to cart.`);
        },
        removeFromWishlist(item) {
            this.wishlist = this.wishlist.filter(w => w.id !== item.id);
            alert(`${item.name} removed from wishlist.`);
        },
        logout() {
            alert("You have been logged out.");
        }
    }
};
</script>