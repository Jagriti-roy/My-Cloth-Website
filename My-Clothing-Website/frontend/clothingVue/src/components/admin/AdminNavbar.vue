<script setup>

    import { ref, computed, onMounted } from 'vue';
    import { useMainStore } from '../../store';
    const store = useMainStore();

    defineProps({
        msg: String
    });
    const isMenuOpen = ref(false);

    // Dropdown state for profile button
    const isDropdownOpen = ref(false);

    const toggleDropdown = () => {
        isDropdownOpen.value = !isDropdownOpen.value;
    };
    const toggleMenu = () => {
            isMenuOpen.value = !isMenuOpen.value;
        };

    onMounted(() => {
        store.setAppToken(1);
    });
</script>

<template>
    <div class="font-sans text-gray-800 sticky top-0 z-50">
        <!-- Navbar -->
        <header class="bg-stone-950 shadow-md">
            <nav class="max-w-10xl mx-auto px-2 py-4 flex justify-between items-center">
                <router-link to="/admin/addashboard" class="text-3xl font-bold text-white hover:text-amber-100">{{ msg }}</router-link>
                
                <ul class="hidden md:flex space-x-6">
                    <li>
                        <router-link to="/admin/addashboard" class="text-gray-300 hover:text-amber-100 hover:underline underline-offset-4  transition-colors duration-200 flex items-center">
                            <i class="fas fa-home mr-2"></i>
                            Dashboard
                        </router-link>
                    </li>
                    <li>
                        <router-link to="/admin/aduser" class="text-gray-300 hover:text-amber-100 hover:underline underline-offset-4 transition-colors duration-200 flex items-center">
                            <i class="fa-regular fa-user mr-2"></i>
                            User
                        </router-link>
                    </li>
                    <li>
                        <router-link to="/admin/adproduct" class="text-gray-300 hover:text-amber-100 hover:underline underline-offset-4 transition-colors duration-200 flex items-center">
                            <i class="fas fa-box mr-2"></i>
                            Product
                        </router-link>
                    </li>
                    <li>
                        <router-link to="/admin/adorder" class="text-gray-300 hover:text-amber-100 hover:underline underline-offset-4 transition-colors duration-200 flex items-center">
                            <i class="fas fa-shopping-cart mr-2"></i>
                            Order
                        </router-link>
                    </li>
                    <li>
                        <router-link to="/admin/adpayment" class="text-gray-300 hover:text-amber-100 hover:underline underline-offset-4 transition-colors duration-200 flex items-center">
                            <i class="fas fa-credit-card mr-2"></i>
                            Payment
                        </router-link>
                    </li>
                    <li>
                        <router-link to="/admin/adshipping" class="text-gray-300 hover:text-amber-100 hover:underline underline-offset-4 transition-colors duration-200 flex items-center">
                            <i class="fas fa-truck mr-2"></i>
                            Shipping
                        </router-link>
                    </li>
                    <li>
                        <router-link to="/admin/addiscount" class="text-gray-300 hover:text-amber-100 hover:underline underline-offset-4 transition-colors duration-200 flex items-center">
                            <i class="fas fa-tags mr-2"></i>
                            Discount&Promotion
                        </router-link>
                    </li>
                    <li>
                        <router-link to="/admin/adreview" class="text-gray-300 hover:text-amber-100 hover:underline underline-offset-4 transition-colors duration-200 flex items-center">
                            <i class="fas fa-star mr-2"></i>
                            Review
                        </router-link>
                    </li>
                    <li>
                        <router-link to="/admin/adwishlist" class="text-gray-300 hover:text-amber-100 hover:underline underline-offset-4 transition-colors duration-200 flex items-center">
                            <i class="fas fa-heart mr-2"></i>
                            Wishlist
                        </router-link>
                    </li>
                    <li>
                        <router-link to="/admin/adanalytics" class="text-gray-300 hover:text-amber-100 hover:underline underline-offset-4 transition-colors duration-200 flex items-center">
                            <i class="fas fa-chart-line mr-2"></i>
                            Analytics
                        </router-link>
                    </li>
                    <li>
                        <router-link to="/admin/adnotifications" class="text-gray-300 hover:text-amber-100 hover:underline underline-offset-4 transition-colors duration-200 flex items-center">
                            <i class="fas fa-bell mr-2"></i>
                            Notifications
                        </router-link>
                    </li>
                </ul>



                
                <router-link to="/admin/adcartmanagement" class="rounded-lg px-2 py-2 bg-stone-900 hover:bg-stone-800 text-white hover:text-amber-100 focus:outline-none focus:ring-2 focus:ring-amber-100 flex items-center">
                    <i class="fas fa-box mr-2"></i>
                    Cart Management
                </router-link>

                <button class="md:hidden text-amber-700" @click="toggleMenu">☰</button>
                
                <div v-if="isMenuOpen" class="absolute top-16 right-0 bg-stone-800 shadow-md rounded-lg p-4 md:hidden">
                    <ul class="flex flex-col space-y-2">
                        <li><router-link to="/admin/addashboard" class="hover:text-amber-100 text-gray-300">Dashboard</router-link></li>
                        <li><router-link to="/admin/adminuser" class="hover:text-amber-100 text-gray-300">User</router-link></li>
                        <li><router-link to="/admin/adproduct" class="hover:text-amber-100 text-gray-300">Product</router-link></li>
                        <li><router-link to="/admin/adorder" class="hover:text-amber-100 text-gray-300">Order</router-link></li>
                        <li><router-link to="/admin/adpayment" class="hover:text-amber-100 text-gray-300">Payment</router-link></li>
                        <li><router-link to="/admin/adshipping" class="hover:text-amber-100 text-gray-300">Shipping</router-link></li>
                        <li><router-link to="/admin/addiscount" class="hover:text-amber-100 text-gray-300">Discount and Promotion</router-link></li>
                        <li><router-link to="/admin/adreview" class="hover:text-amber-100 text-gray-300">Review</router-link></li>
                        <li><router-link to="/admin/adwishlist" class="hover:text-amber-100 text-gray-300">Wishlist</router-link></li>
                        <li><router-link to="/admin/adanalytics" class="hover:text-amber-100 text-gray-300">Analytics</router-link></li>
                        <li><router-link to="/admin/adnotifications" class="hover:text-amber-100 text-gray-300">Notifications</router-link></li>
                        <li><router-link to="/admin/adcartmanagement" class="hover:text-amber-100 text-gray-300">Cart Management</router-link></li>
                    </ul>
                </div>

                

                <div class="relative ml-4">
                    <button 
                        class="p-2 rounded-full bg-white  hover:bg-stone-800 focus:outline-none"
                        @click="toggleDropdown"
                    >
                        <img src="../../assets/black.png" alt="Profile" class="w-8 h-8 rounded-full" />
                    </button>
                    
                    <div 
                        v-if="isDropdownOpen" 
                        class="absolute right-0 mt-2 w-48 bg-gray-800 rounded-md shadow-lg py-2 z-20"
                    >
                        <router-link to="/profile" class="block px-4 py-2 text-gray-300 hover:bg-gray-700">Profile</router-link>
                        <router-link to="/settings" class="block px-4 py-2 text-gray-300 hover:bg-gray-700">Settings</router-link>
                        <router-link to="/logout" class="block px-4 py-2 text-gray-300 hover:bg-gray-700">Logout</router-link>
                    </div>
                </div>
            </nav>
        </header>
    </div>
    <router-view></router-view>
</template>