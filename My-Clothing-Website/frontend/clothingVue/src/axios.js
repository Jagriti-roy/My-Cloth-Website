import axios from 'axios';
import { useMainStore } from './store';

const axiosInstance = axios.create({
  baseURL: 'http://127.0.0.1:5000/api', // Update with your backend URL
});

// Add request interceptor
axiosInstance.interceptors.request.use((config) => {
  const store = useMainStore();
  if (store.maintoken) {
    config.headers.Authorization = `Bearer ${store.maintoken}`;
  }
  return config;
}, (error) => {
  return Promise.reject(error);
});

export default axiosInstance;
