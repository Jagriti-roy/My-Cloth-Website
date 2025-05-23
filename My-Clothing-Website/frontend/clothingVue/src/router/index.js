import { createRouter, createWebHistory } from 'vue-router';

import { useMainStore } from '../store'; // Import Pinia store

////////////////////////////////////////////////////////////USER IMPORTING PART/////////////////////////////////////////////////

import LandingPage from '../components/LandingPage.vue';
import Cart from '../components/Cart.vue';
import PageListingPage from '../components/PageListingPage.vue';
import Wishlist from '../components/Wishlist.vue';
import Profile from '../components/Profile.vue';
import Orders from '../components/Orders.vue';
import CustomerCare from '../components/CustomerCare.vue';
import Login from '../components/authenticate/Login.vue';
import Signup from '../components/authenticate/Signup.vue';


////////////////////////////////////////////////////////////ADMIN IMPORTING PART/////////////////////////////////////////////////

import AdminHome from '../components/admin/AdminHome.vue';
import AdminNavbar from '../components/admin/AdminNavbar.vue';
import AdminUser from '../components/admin/AdminUser.vue';
import AdminProduct from '../components/admin/AdminProduct.vue';
import AdminOrder from '../components/admin/AdminOrder.vue';
import AdminPayment from '../components/admin/AdminPayment.vue';
import AdminShipping from '../components/admin/AdminShipping.vue';
import AdminDiscount from '../components/admin/AdminDiscount.vue';
import AdminReview from '../components/admin/AdminReview.vue';
import AdminWishlist from '../components/admin/AdminWishlist.vue';
import AdminAnalytics from '../components/admin/AdminAnalytics.vue';
import AdminNotifications from '../components/admin/AdminNotifications.vue';
import AdminCartManagement from '../components/admin/AdminCartManagement.vue';



////////////////////////////////////////////////////////////ROUTES DEFINING PART/////////////////////////////////////////////////


const routes = [
  { path: '/', component: LandingPage, name: 'LandingPage' },
  { path: '/cart', component: Cart, name: 'Cart' },
  { path: '/shop', component: PageListingPage, name: 'PageListingPage' },
  { path: '/orders', component: Orders, name: 'Orders' },
  { path: '/customercare', component: CustomerCare, name: 'CustomerCare' },
  { path: '/profile', component: Profile, name: 'Profile', meta: { requiresAuth: true } }, // Protected route
  { path: '/wishlist', component: Wishlist, name: 'Wishlist', meta: { requiresAuth: true } }, // Protected route
  { path: '/login', component: Login, name: 'Login' },
  { path: '/signup', component: Signup, name: 'Signup' },

  {
    path: '/admin',
    component: AdminNavbar,
    children: [
        { path: 'addashboard', component: AdminHome },
        { path: 'aduser', component: AdminUser },
        { path: 'adproduct', component: AdminProduct },
        { path: 'adorder', component: AdminOrder },
        { path: 'adpayment', component: AdminPayment },
        { path: 'adshipping', component: AdminShipping },
        { path: 'addiscount', component: AdminDiscount },
        { path: 'adreview', component: AdminReview },
        { path: 'adwishlist', component: AdminWishlist },
        { path: 'adanalytics', component: AdminAnalytics },
        { path: 'adnotifications', component: AdminNotifications },
        { path: 'adcartmanagement', component: AdminCartManagement },
    ]
  },

  // { 
  //   path: '/:pathMatch(.*)*',
  //   name: 'NotFound', 
  //   component: HelloWorld
  // }

];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Add route guards
router.beforeEach((to, from, next) => {
  const store = useMainStore();
  if (to.meta.requiresAuth && !store.maintoken) {
    // Redirect to login if user is not authenticated
    next({ name: 'LandingPage' });
  } else {
    next();
  }
});

export default router;