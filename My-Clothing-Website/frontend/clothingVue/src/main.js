import { createApp } from 'vue';
import App from './App.vue';
import './assets/tailwind.css';
import router from './router';
import { createPinia } from 'pinia';

const app = createApp(App);

// Add Pinia store
const pinia = createPinia();
app.use(pinia);

// Add router
app.use(router);

app.mount('#app');
