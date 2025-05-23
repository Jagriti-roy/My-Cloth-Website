<template>
    <div class="bg-stone-900 min-h-screen text-gray-200 font-sans">
      <div class="max-w-4xl mx-auto px-6 py-12">
        <h1 class="text-3xl font-bold text-amber-700 mb-8 text-center">Customer Care</h1>
  
        <!-- FAQ Section -->
        <div class="bg-stone-800 rounded-lg shadow-md p-6 mb-12">
          <h2 class="text-2xl font-semibold mb-4 text-gray-100">Frequently Asked Questions</h2>
          <ul class="space-y-4">
            <li v-for="(faq, index) in faqs" :key="index" class="border-b border-gray-700 pb-4">
              <button
                class="text-lg font-medium text-amber-600 hover:underline"
                @click="toggleFaq(index)"
              >
                {{ faq.question }}
              </button>
              <p v-if="faq.open" class="text-gray-400 mt-2">{{ faq.answer }}</p>
            </li>
          </ul>
        </div>
  
        <!-- Contact Form Section -->
        <div class="bg-stone-800 rounded-lg shadow-md p-6">
          <h2 class="text-2xl font-semibold mb-4 text-gray-100">Contact Us</h2>
          <form @submit.prevent="submitQuery" class="space-y-6">
            <div>
              <label for="name" class="block text-gray-300 font-medium">Name</label>
              <input
                v-model="contactForm.name"
                type="text"
                id="name"
                class="w-full px-4 py-2 rounded-md bg-stone-700 text-gray-200 focus:outline-none focus:ring focus:ring-amber-600"
                required
              />
            </div>
            <div>
              <label for="email" class="block text-gray-300 font-medium">Email</label>
              <input
                v-model="contactForm.email"
                type="email"
                id="email"
                class="w-full px-4 py-2 rounded-md bg-stone-700 text-gray-200 focus:outline-none focus:ring focus:ring-amber-600"
                required
              />
            </div>
            <div>
              <label for="message" class="block text-gray-300 font-medium">Message</label>
              <textarea
                v-model="contactForm.message"
                id="message"
                rows="5"
                class="w-full px-4 py-2 rounded-md bg-stone-700 text-gray-200 focus:outline-none focus:ring focus:ring-amber-600"
                required
              ></textarea>
            </div>
            <button
              type="submit"
              class="w-full bg-amber-600 text-gray-900 hover:bg-amber-700 font-semibold rounded-lg px-4 py-2"
            >
              Submit
            </button>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        // List of FAQs
        faqs: [
          {
            question: "How can I track my order?",
            answer: "You can track your order in the 'My Orders' section. Simply click on the order to view tracking details.",
            open: false,
          },
          {
            question: "What is the return policy?",
            answer: "You can return most items within 30 days of receipt. Visit the 'Return Policy' page for more details.",
            open: false,
          },
          {
            question: "How can I contact customer support?",
            answer: "You can contact us through this page by filling out the form below or using the live chat option.",
            open: false,
          },
        ],
        // Contact form data
        contactForm: {
          name: "",
          email: "",
          message: "",
        },
      };
    },
    methods: {
      // Toggle the visibility of an FAQ answer
      toggleFaq(index) {
        this.faqs[index].open = !this.faqs[index].open;
      },
      // Handle form submission
      submitQuery() {
        // Mock submission logic
        console.log("Query submitted:", this.contactForm);
  
        // Clear the form after submission
        this.contactForm.name = "";
        this.contactForm.email = "";
        this.contactForm.message = "";
  
        // Display a confirmation message (could also integrate with backend API)
        alert("Thank you for contacting us! We will get back to you soon.");
      },
    },
  };
  </script>
  
  <style scoped>
  /* Custom styles for the customer care page */
  </style>
  