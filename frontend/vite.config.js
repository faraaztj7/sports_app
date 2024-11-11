import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0', // Allow external access to the frontend
    port: 5173,      // Ensure the port matches the one in docker-compose.yml
  },
})
