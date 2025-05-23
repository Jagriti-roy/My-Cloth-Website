<script setup>
    import router from '../router';

</script>
<template>
    <div class="mt-0 ">
        <!-- First Footer -->
        
        <footer class="bg-stone-800 text-gray-400 py-8 px-6">
            <div class="max-w-7xl mx-auto grid gap-6 sm:grid-cols-2 md:grid-cols-4 text-center md:text-left">
                <div>
                    <h3 class="text-lg font-semibold mb-4 text-amber-700">ShopEase</h3>
                    <p>Making shopping easy and enjoyable.</p>
                </div>
                <div>
                    <h3 class="text-lg font-semibold mb-4 text-amber-700">Quick Links</h3>
                    <ul>
                        <li><a href="#home" class="hover:underline">Home</a></li>
                        <li><a href="#products" class="hover:underline">Products</a></li>
                        <li><a href="#categories" class="hover:underline">Categories</a></li>
                        <li><a href="#contact" class="hover:underline">Contact</a></li>
                    </ul>
                </div>
                <div>
                    <h3 class="text-lg font-semibold mb-4 text-amber-700">Contact</h3>
                    <p>Email: support@shopease.com</p>
                    <p>Phone: (123) 456-7890</p>
                </div>
                <div>
                    <h3 class="text-lg font-semibold mb-4 text-amber-700">Follow Us</h3>
                    <div class="flex justify-center md:justify-start space-x-4">
                        <a href="#" class="hover:underline">Facebook</a>
                        <a href="#" class="hover:underline">Twitter</a>
                        <a href="#" class="hover:underline">Instagram</a>
                    </div>
                </div>
            </div>
            <div class="text-center text-sm text-gray-500 mt-8">
                &copy; 2023 ShopEase. All rights reserved.
            </div>
        </footer>

        <!-- Second Footer -->
        
        <footer id="contact" class="bg-stone-950 text-gray-200 px-6 fixed inset-x-0 bottom-0">
            <div class="flex justify-center space-x-4 mt-4 mb-3">
                <router-link to="/cart" class="bg-amber-200 text-gray-800 py-2 px-4 rounded-full shadow-md hover:bg-amber-100 transition flex items-center">
                    <i class="fas fa-shopping-cart mr-2"></i>
                    Cart
                </router-link>

                <router-link to="/wishlist" class="bg-amber-200 text-gray-800 py-2 px-4 rounded-full shadow-md hover:bg-amber-100 transition flex items-center">
                    <i class="fas fa-heart mr-2"></i>
                    Wishlist
                </router-link>

                <router-link to="/orders" class="bg-amber-200 text-gray-800 py-2 px-4 rounded-full shadow-md hover:bg-amber-100 transition flex items-center">
                    <i class="fas fa-box mr-2"></i>
                    Orders
                </router-link>
            </div>

        </footer>
    </div>
</template>
