<template>
    <div class="font-sans text-gray-200">
        <!-- Cart Section -->
      <section id="cart" class="py-16 px-6 bg-stone-900">
          <div class="max-w-7xl mx-auto">
              <h2 class="text-3xl font-bold mb-8 text-center text-gray-200">Your Shopping Cart</h2>

              <!-- Cart Items -->
              <div v-if="cartItems.length" class="grid gap-6 md:grid-cols-3">
                  <!-- Cart Item List -->
                  <div class="md:col-span-2">
                      <div v-for="item in cartItems" :key="item.id" class="bg-amber-100 p-4 rounded-lg flex items-center space-x-4 mt-2">
                          <img :src="item.image" alt="Product" class="w-20 h-20 rounded-md object-cover" />
                          <div class="flex-1">
                              <h3 class="text-lg font-semibold text-stone-700">{{ item.name }}</h3>
                              <p class="text-stone-800 mt-1">Price: ${{ item.price }}</p>
                              <p class="text-stone-800">Subtotal: ${{ (item.price * item.quantity).toFixed(2) }}</p>
                          </div>
                          <div class="flex items-center space-x-2">
                              <button @click="decreaseQuantity(item)" class="px-2 py-1 bg-stone-500 rounded text-gray-200 hover:bg-stone-700">-</button>
                              <span class="text-stone-900">{{ item.quantity }}</span>
                              <button @click="increaseQuantity(item)" class="px-2 py-1 bg-stone-500 rounded text-gray-200 hover:bg-stone-700">+</button>
                          </div>
                          <button @click="removeFromCart(item.id)" class="ml-4 text-red-500 hover:text-red-700">Remove</button>
                      </div>
                  </div>

                  <!-- Order Summary -->
                  <div class="bg-stone-500 p-6 rounded-lg">
                      <h3 class="text-xl font-semibold text-stone-800 mb-4">Order Summary</h3>
                      <div class="flex justify-between text-stone-200 mb-2">
                          <span>Subtotal</span>
                          <span>${{ cartSubtotal.toFixed(2) }}</span>
                      </div>
                      <div class="flex justify-between text-stone-200 mb-2">
                          <span>Tax</span>
                          <span>${{ cartTax.toFixed(2) }}</span>
                      </div>
                      <div class="flex justify-between text-stone-200 mb-2">
                          <span>Shipping</span>
                          <span>${{ shippingCost }}</span>
                      </div>
                      <div class="border-t border-gray-600 mt-4"></div>
                      <div class="flex justify-between text-xl font-semibold text-gray-200 mt-4">
                          <span>Total</span>
                          <span>${{ cartTotal.toFixed(2) }}</span>
                      </div>
                      <button class="w-full mt-6 py-2 bg-amber-100 text-gray-900 rounded-lg hover:bg-amber-200 transition" @click="checkout">Proceed to Checkout</button>
                  </div>
              </div>

              <!-- Empty Cart Message -->
              <div v-else class="text-center text-gray-400">
                  <p>Your cart is currently empty.</p>
                  <a href="#products" class="mt-4 inline-block px-6 py-3 bg-amber-700 text-gray-900 font-semibold rounded-lg shadow-lg hover:bg-amber-800 transition">Browse Products</a>
              </div>
          </div>
      </section>

      
    </div>
</template>


<script>
    export default {
        data() {
            return {
                cartItems: [
                    // Sample data structure for cart items; replace with API call results
                    { id: 1, name: "Product 1", price: 29.99, quantity: 2, image: "product1.jpg" },
                    { id: 2, name: "Product 2", price: 49.99, quantity: 1, image: "product2.jpg" },
                ],
                isMenuOpen: false,
                isDropdownOpen: false,
                shippingCost: 5.99
            };
        },
        computed: {
            cartSubtotal() {
                return this.cartItems.reduce((sum, item) => sum + item.price * item.quantity, 0);
            },
            cartTax() {
                return this.cartSubtotal * 0.1;  // Assuming 10% tax rate
            },
            cartTotal() {
                return this.cartSubtotal + this.cartTax + this.shippingCost;
            }
        },
        methods: {
            toggleMenu() {
                this.isMenuOpen = !this.isMenuOpen;
            },
            toggleDropdown() {
                this.isDropdownOpen = !this.isDropdownOpen;
            },
            increaseQuantity(item) {
                item.quantity++;
            },
            decreaseQuantity(item) {
                if (item.quantity > 1) item.quantity--;
            },
            removeFromCart(id) {
                this.cartItems = this.cartItems.filter(item => item.id !== id);
            },
            checkout() {
                // Trigger checkout process
                alert("Proceeding to checkout...");
            }
        }
    };
</script>
  
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
  