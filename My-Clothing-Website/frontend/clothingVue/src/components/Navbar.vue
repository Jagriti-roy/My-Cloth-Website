<script setup>

    import { useMainStore } from '../store';
    import router from '../router';
    const store = useMainStore();
    import { ref, computed } from 'vue';

    import product1 from '../assets/product1.jpeg';
    import product2 from '../assets/product2.jpeg';
    import product3 from '../assets/product3.jpeg';
    import product4 from '../assets/product4.jpeg';
    import product5 from '../assets/product5.jpeg';
    import product6 from '../assets/product6.jpeg';

    defineProps({
        msg: String
    });

    const selectedCategory = ref('');
    const searchQuery = ref('');
    const islogged = ref(false);
    const isMenuOpen = ref(false);
    const toggleMenu = () => {
        isMenuOpen.value = !isMenuOpen.value;
    };

    const isDropdownOpen = ref(false);

    const toggleDropdown = () => {
        isDropdownOpen.value = !isDropdownOpen.value;
    };

    const openDropdown = () => {
        isDropdownOpen.value = true;
    };

    const closeDropdown = () => {
        isDropdownOpen.value = false;
    };

    const keepDropdownOpen = () => {
        isDropdownOpen.value = true;
    };

    const currentSlide = ref(0);
    const slides = ref([
        { image: product1 },
        { image: product2 },
        { image: product3 },
        { image: product4 },
        { image: product5 },
        { image: product6 },
    ]);

    const nextSlide = () => {
        currentSlide.value = (currentSlide.value + 1) % slides.value.length;
    };

    const prevSlide = () => {
        currentSlide.value = (currentSlide.value - 1 + slides.value.length) % slides.value.length;
    };

    function logout() {
        store.clearToken();
        store.clearUser();
        window.location.href = '/';
    }

    const redirectToAuthPage = () => {
        router.push('/signup');
    }


</script>

<template>
    <div class="font-sans text-gray-800 sticky top-0 z-50">
        <header class="bg-stone-950 shadow-md">
            <nav class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
                <router-link to="/" class="text-3xl font-bold text-white hover:text-amber-100">{{ msg }}</router-link>
                
                <ul class="hidden md:flex space-x-6">
                    <li>
                        <router-link to="/" class="text-gray-300 hover:text-amber-100 hover:underline underline-offset-4  transition-colors duration-200 flex items-center">
                            <i class="fas fa-home mr-2"></i>
                            Home
                        </router-link>
                    </li>
                    <li>
                        <router-link to="/shop" class="text-gray-300 hover:text-amber-100 hover:underline underline-offset-4 transition-colors duration-200 flex items-center">
                            <i class="fas fa-shopping-bag mr-2"></i>
                            Shop
                        </router-link>
                    </li>
                    <li>
                        <router-link to="/cart" class="text-gray-300 hover:text-amber-100 hover:underline underline-offset-4 transition-colors duration-200 flex items-center">
                            <i class="fas fa-shopping-cart mr-2"></i>
                            Cart
                        </router-link>
                    </li>
                    <li>
                        <router-link to="/wishlist" class="text-gray-300 hover:text-amber-100 hover:underline underline-offset-4 transition-colors duration-200 flex items-center">
                            <i class="fas fa-heart mr-2"></i>
                            Wishlist
                        </router-link>
                    </li>
                    <li>
                        <router-link to="/customercare" class="text-gray-300 hover:text-amber-100 hover:underline underline-offset-4 transition-colors duration-200 flex items-center">
                            <i class="fas fa-phone-alt mr-2"></i>
                            Customer Care
                        </router-link>
                    </li>
                </ul>

                <div class=" hidden md:flex items-center relative bg-gray-200 rounded-lg h-10 focus:outline-none focus:ring-2 focus:ring-amber-700">
                    <select 
                        class="py-2 px-4 rounded-l-lg bg-gray-200 text-gray-900 w-12 "
                        v-model="selectedCategory">
                        
                        <option value="All" disabled selected>All Categories</option>
                        <option value="men">Men</option>
                        <option value="women">Women</option>
                        <option value="accessories">Accessories</option>
                        <option value="shoes">Shoes</option>
                        <option value="kids">Kids</option>
                    </select>
                    <input 
                        type="text" 
                        v-model="searchQuery"
                        class="w-full px-1 py-2 pl-1 text-gray-900 rounded-r-lg bg-gray-200 "
                        placeholder="Search for products..."
                    />
                    <svg class="cursor-pointer ml-1 px-2 bg-white rounded-r-lg h-10" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="50" height="50" viewBox="0 0 50 50">
                        <path d="M 21 3 C 11.601563 3 4 10.601563 4 20 C 4 29.398438 11.601563 37 21 37 C 24.355469 37 27.460938 36.015625 30.09375 34.34375 L 42.375 46.625 L 46.625 42.375 L 34.5 30.28125 C 36.679688 27.421875 38 23.878906 38 20 C 38 10.601563 30.398438 3 21 3 Z M 21 7 C 28.199219 7 34 12.800781 34 20 C 34 27.199219 28.199219 33 21 33 C 13.800781 33 8 27.199219 8 20 C 8 12.800781 13.800781 7 21 7 Z"></path>
                    </svg>
                </div>

                <div class="cursor-pointer hidden md:flex items-center">
                    <select class="px-4 w-10 py-2 rounded-lg cursor-pointer bg-gray-200 text-gray-800 focus:outline-none focus:ring-2 focus:ring-amber-100">
                        <option value="en">EN</option>
                        <option value="es">ES</option>
                        <option value="fr">FR</option>
                    </select>
                </div>
                <router-link to="/orders" class="rounded-lg px-2 py-2 bg-stone-900 hover:bg-stone-800 text-white hover:text-amber-100 focus:outline-none focus:ring-2 focus:ring-amber-100 flex items-center">
                    <i class="fas fa-box mr-2"></i>
                    Orders
                </router-link>

                <button class="md:hidden text-amber-700" @click="toggleMenu">☰</button>
                
                <div v-if="isMenuOpen" class="absolute top-16 right-0 bg-stone-800 shadow-md rounded-lg p-4 md:hidden">
                    <ul class="flex flex-col space-y-2">
                        <li><router-link to="/home" class="hover:text-amber-100 text-gray-300">Home</router-link></li>
                        <li><router-link to="/shop" class="hover:text-amber-100 text-gray-300">Shop</router-link></li>
                        <li><router-link to="/cart" class="hover:text-amber-100 text-gray-300">Cart</router-link></li>
                        <li><router-link to="/wishlist" class="hover:text-amber-100 text-gray-300">Wishlist</router-link></li>
                        <li><router-link to="#" class="hover:text-amber-100 text-gray-300">Customer Care</router-link></li>
                    </ul>
                </div>

                <div v-if="!store.maintoken" class="relative ml-4">
                    <button
                        @click="redirectToAuthPage"
                        class="bg-gradient-to-r from-amber-600 to-amber-500 text-gray-900 font-semibold py-2 px-6 rounded-full shadow-lg transform transition-transform duration-200 hover:scale-105 hover:from-amber-500 hover:to-amber-400 focus:outline-none focus:ring-4 focus:ring-amber-700">
                        Login / Signup
                    </button>
                </div>

                <div v-else class="relative ml-4">
                    <button 
                        class="p-2 rounded-full bg-white  hover:bg-stone-800 focus:outline-none"
                        @click="toggleDropdown"
                    >
                        <img src="../assets/black.png" alt="Profile" class="w-8 h-8 rounded-full" />
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
</template>