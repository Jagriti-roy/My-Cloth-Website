<template>
    <div>
        <!-- Wishlist Section -->
      <section id="wishlist" class="py-16 px-6 bg-stone-900">
          <div class="max-w-7xl mx-auto">
              <h2 class="text-3xl font-bold mb-8 text-center text-gray-200">Your Wishlist</h2>

              <!-- Wishlist Items -->
              <div v-if="wishlist.length > 0" class="grid gap-6 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
                  <div v-for="item in wishlist" :key="item.id" class="bg-gray-700 rounded-lg shadow-md overflow-hidden">
                      <img :src="item.image" alt="Product" class="w-full h-56 object-cover" />
                      <div class="p-4">
                          <h3 class="font-semibold text-lg text-gray-200">{{ item.name }}</h3>
                          <p class="text-amber-600 font-bold mt-2">${{ item.price }}</p>
                          <div class="mt-4 flex space-x-2">
                              <button 
                                  class="w-full py-2 bg-amber-100 text-gray-900 rounded hover:bg-amber-300 transition"
                                  @click="addToCart(item)"
                              >
                                  Add to Cart
                              </button>
                              <button 
                                  class="w-full py-2 bg-white text-red-600 hover:text-white rounded hover:bg-red-300 transition"
                                  @click="removeFromWishlist(item)"
                              >
                                  Remove
                              </button>
                          </div>
                      </div>
                  </div>
              </div>

              <!-- No Wishlist Items Message -->
              <div v-else class="text-center text-gray-400">
                  <p>Your wishlist is currently empty.</p>
              </div>
          </div>
      </section>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                msg: "ShopEase",
                wishlist: [
                    { id: 1, name: "Product 1", price: 100, image: "product1.jpg" },
                    { id: 2, name: "Product 2", price: 120, image: "product2.jpg" },
                    // Add more wishlist items as needed
                ],
            };
        },
        methods: {
            toggleMenu() {
                this.isMenuOpen = !this.isMenuOpen;
            },
            addToCart(item) {
                alert(`Added ${item.name} to cart!`);
            },
            removeFromWishlist(item) {
                this.wishlist = this.wishlist.filter(w => w.id !== item.id);
                alert(`${item.name} has been removed from your wishlist.`);
            }
        }
    };
</script>