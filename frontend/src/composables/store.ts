import { acceptHMRUpdate, defineStore } from 'pinia'

export const useStore = defineStore('store', () => {
  const login = ref('');
  const password = ref('')

  return {
    login,
    password
  }
})

if (import.meta.hot)
  import.meta.hot.accept(acceptHMRUpdate(useStore, import.meta.hot))