import { defineStore } from 'pinia';

export const useMainStore = defineStore('main', {
  state: () => ({
    user: null, // User details
    maintoken: localStorage.getItem('maintoken') || null, // JWT token,
    apptoken: localStorage.getItem('apptoken') || 0,
  }),
  actions: {
    setMainToken(token) {
      this.maintoken = token;
      localStorage.setItem('maintoken', token);
    },
    clearToken() {
      this.maintoken = null;
      localStorage.removeItem('maintoken');
    },
    setUser(user) {
      this.user = user;
    },
    clearUser() {
      this.user = null;
    },
    setAppToken(token) {
      this.apptoken = token;
      localStorage.setItem('apptoken', token);
    }
  },
});
