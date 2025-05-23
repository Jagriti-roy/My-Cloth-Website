<script>
    export default {
        data() {
            return {
                msg: "ShopEase",
                categories: [
                    { id: 1, name: "Men" },
                    { id: 2, name: "Women" },
                    { id: 3, name: "Shoes" },
                    { id: 4, name: "Accessories" },
                ],
                sizes: ["S", "M", "L", "XL"],
                colors: ["Red", "Blue", "Green", "Black"],
                selectedCategories: [],
                priceRange: 1000,
                selectedSizes: [],
                selectedColors: [],
                sortBy: "price",
                products: [
                    { id: 1, name: "Product 1", originalPrice: 100, discountedPrice: 80, image: "product1.jpg" },
                    { id: 2, name: "Product 2", originalPrice: 120, image: "product2.jpg" },
                    // Add more product data as needed
                ],
                currentPage: 1,
                productsPerPage: 8,
            };
        },
        computed: {
            filteredProducts() {
                return this.products
                    .filter(p => 
                        (this.selectedCategories.length === 0 || this.selectedCategories.includes(p.category)) &&
                        (this.selectedSizes.length === 0 || this.selectedSizes.includes(p.size)) &&
                        (this.selectedColors.length === 0 || this.selectedColors.includes(p.color)) &&
                        p.price <= this.priceRange
                    )
                    .sort((a, b) => {
                        if (this.sortBy === "price") return a.price - b.price;
                        if (this.sortBy === "newest") return new Date(b.dateAdded) - new Date(a.dateAdded);
                        if (this.sortBy === "popularity") return b.popularity - a.popularity;
                    });
            },
            paginatedProducts() {
                const start = (this.currentPage - 1) * this.productsPerPage;
                return this.filteredProducts.slice(start, start + this.productsPerPage);
            },
            totalPages() {
                return Math.ceil(this.filteredProducts.length / this.productsPerPage);
            }
        },
        methods: {
            toggleMenu() {
                this.isMenuOpen = !this.isMenuOpen;
            },
            prevPage() {
                if (this.currentPage > 1) this.currentPage--;
            },
            nextPage() {
                if (this.currentPage < this.totalPages) this.currentPage++;
            },
            addToCart(product) {
                alert(`Added ${product.name} to cart!`);
            }
        }
    };
</script>


<template>
    <div>
        <!-- Product Listing Section -->
      <section id="products" class="py-16 px-6 bg-stone-900">
          <div class="max-w-7xl mx-auto">
              <h2 class="text-3xl font-bold mb-8 text-center text-amber-100">Our Products</h2>

              <!-- Filters -->
              <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-10">
                  <!-- Category Filter -->
                  <div>
                      <h3 class="text-lg font-semibold text-gray-100 mb-4">Categories</h3>
                      <div v-for="category in categories" :key="category.id" class="flex items-center mb-2">
                          <input type="checkbox" :value="category.name" v-model="selectedCategories" class="mr-2">
                          <label class="text-gray-400">{{ category.name }}</label>
                      </div>
                  </div>

                  <!-- Price Range Filter -->
                  <div>
                      <h3 class="text-lg font-semibold text-amber-100 mb-4">Price Range</h3>
                      <input type="range" v-model="priceRange" min="0" max="1000" class="w-full" />
                      <p class="text-stone-200 mt-2">Up to ${{ priceRange }}</p>
                  </div>

                  <!-- Size Filter -->
                  <div>
                      <h3 class="text-lg font-semibold text-gray-200 mb-4">Size</h3>
                      <div v-for="size in sizes" :key="size" class="flex items-center mb-2">
                          <input type="checkbox" :value="size" v-model="selectedSizes" class="mr-2">
                          <label class="text-gray-400">{{ size }}</label>
                      </div>
                  </div>

                  <!-- Color Filter -->
                  <div>
                      <h3 class="text-lg font-semibold text-gray-200 mb-4">Color</h3>
                      <div v-for="color in colors" :key="color" class="flex items-center mb-2">
                          <input type="checkbox" :value="color" v-model="selectedColors" class="mr-2">
                          <label class="text-gray-400">{{ color }}</label>
                      </div>
                  </div>
              </div>

              <!-- Sort By Filter -->
              <div class="flex justify-between items-center mb-10">
                  <div>
                      <label class="text-gray-400 mr-2">Sort By:</label>
                      <select v-model="sortBy" class="bg-gray-700 text-gray-300 p-2 rounded-md">
                          <option value="price">Price</option>
                          <option value="newest">Newest</option>
                          <option value="popularity">Popularity</option>
                      </select>
                  </div>
                  <p class="text-gray-400">Showing {{ filteredProducts.length }} results</p>
              </div>

              <!-- Product Grid -->
              <div class="grid gap-6 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
                  <div v-for="product in paginatedProducts" :key="product.id" class="bg-gray-700 rounded-lg shadow-md overflow-hidden">
                      <a :href="'/product/' + product.id">
                          <img :src="product.image" alt="Product" class="w-full h-56 object-cover" />
                      </a>
                      <div class="p-4">
                          <h3 class="font-semibold text-lg text-gray-200">{{ product.name }}</h3>
                          <p class="text-gray-400 mt-2">
                              <span v-if="product.discountedPrice" class="line-through text-red-400">${{ product.originalPrice }}</span>
                              ${{ product.discountedPrice || product.originalPrice }}
                          </p>
                          <button class="w-full mt-4 py-2 bg-amber-700 text-gray-900 rounded hover:bg-amber-800 transition" @click="addToCart(product)">Add to Cart</button>
                      </div>
                  </div>
              </div>

              <!-- Pagination -->
              <div class="flex justify-center mt-10">
                  <button @click="prevPage" :disabled="currentPage === 1" class="px-4 py-2 bg-amber-200 text-stone-800 rounded-l hover:bg-amber-100">Previous</button>
                  <button @click="nextPage" :disabled="currentPage === totalPages" class="px-4 py-2 bg-amber-200 text-stone-800 rounded-r hover:bg-amber-100">Next</button>
              </div>
          </div>
      </section>
    </div>
</template>


<style scoped>

</style>