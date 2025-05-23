<script setup>
    import { ref, computed } from 'vue';


    import product1 from '../assets/product1.jpeg';
    import product2 from '../assets/product2.jpeg';
    import product3 from '../assets/product3.jpeg';
    import product4 from '../assets/product4.jpeg';
    import product5 from '../assets/product5.jpeg';
    import product6 from '../assets/product6.jpeg';

    // Define props
    defineProps({
        msg: String
    });

    // State for mobile menu
    const isMenuOpen = ref(false);
    const toggleMenu = () => {
        isMenuOpen.value = !isMenuOpen.value;
    };

    // Dropdown state for profile button
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

    // Carousel functionality
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

    // Computed property for hero section background
    const heroStyle = computed(() => {
        const slide = slides.value[currentSlide.value];
        return {
            backgroundImage: slide ? `url(${slide.image})` : 'none',
            backgroundSize: 'cover',
            backgroundPosition: 'center',
            height: '400px', // Adjust the height as needed
        };
    });

    // Example data for demonstration
    const products = ref([
        { id: 1, name: 'Product 1', description: 'Description of Product 1', price: 19.99, image: 'https://via.placeholder.com/200' },
        { id: 2, name: 'Product 2', description: 'Description of Product 2', price: 29.99, image: 'https://via.placeholder.com/200' },
        { id: 3, name: 'Product 3', description: 'Description of Product 3', price: 39.99, image: 'https://via.placeholder.com/200' },
        { id: 4, name: 'Product 4', description: 'Description of Product 4', price: 49.99, image: 'https://via.placeholder.com/200' },
    ]);

    const categories = ref([
        { id: 1, name: 'Electronics', image: 'https://via.placeholder.com/200' },
        { id: 2, name: 'Clothing', image: 'https://via.placeholder.com/200' },
        { id: 3, name: 'Books', image: 'https://via.placeholder.com/200' },
        { id: 4, name: 'Home & Kitchen', image: 'https://via.placeholder.com/200' }
    ]);


</script>

<template>

    <div class="font-sans text-gray-800">
        
        <section id="home" class="relative text-white text-center py-20 px-6 transition duration-500" :style="heroStyle">
            <h1 class="text-4xl md:text-5xl font-bold mb-4">Discover Amazing Products</h1>
            <p class="text-lg md:text-xl mb-6">Find everything you need, delivered to your door.</p>
            <!-- Carousel Controls -->
            <div class="absolute inset-0 flex justify-between items-center">
                <button class="bg-stone-500 text-gray-800 rounded-full p-2 hover:bg-amber-100 transition" @click="prevSlide">
                    &#10094; <!-- Left Arrow -->
                </button>
                <button class="bg-stone-500 text-gray-800 rounded-full p-2 hover:bg-amber-100 transition" @click="nextSlide">
                    &#10095; <!-- Right Arrow -->
                </button>
            </div>
        </section>

        <section id="products" class="py-16 px-6 bg-stone-900">
            <div class="max-w-7xl mx-auto text-center mb-10">
                <h2 class="text-3xl font-bold mb-4 text-gray-200">Featured Products</h2>
                <p class="text-gray-400">Explore our bestsellers and latest arrivals</p>
            </div>
            <div class="grid gap-6 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 max-w-7xl mx-auto">
                <div v-for="product in products" :key="product.id" class="bg-stone-800 rounded-lg shadow-md overflow-hidden">
                    <img :src="product.image" alt="Product" class="w-full h-56 object-cover" />
                    <div class="p-4">
                        <h3 class="font-semibold text-lg text-gray-200">{{ product.name }}</h3>
                        <p class="text-gray-400 mt-2">{{ product.description }}</p>
                        <p class="font-bold text-amber-700 mt-4">${{ product.price }}</p>
                        <button class="w-full mt-4 py-2 bg-white text-gray-800 rounded hover:bg-amber-100 transition">Add to Cart</button>
                    </div>
                </div>
            </div>
        </section>

        <section id="categories" class="py-16 bg-stone-900 px-6">
            <div class="max-w-7xl mx-auto text-center mb-10">
                <h2 class="text-3xl font-bold mb-4 text-gray-100">Shop by Category</h2>
                <p class="text-gray-400">Browse products by popular categories</p>
            </div>
            <div class="grid gap-6 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 max-w-7xl mx-auto">
                <div v-for="category in categories" :key="category.id" class="bg-stone-800   rounded-lg shadow-md p-6 text-center">
                    <img :src="category.image" alt="Category" class="w-full h-32 object-cover mb-4 rounded-md" />
                    <h3 class="text-lg font-semibold text-gray-200">{{ category.name }}</h3>
                </div>
            </div>
        </section>

    </div>
</template>

<style scoped>
/* Custom styling for buttons, hover states, and transitions */
.carousel-inner {
    display: flex;
    transition: transform 0.5s ease;
}

.hero-text {
    position: relative;
    z-index: 10;
}
</style>
