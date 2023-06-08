import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  build: {
    target: 'esnext'
  },
  server: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:4800', // 接口的域名
        changeOrigin: true,
      }
    }
  }
})