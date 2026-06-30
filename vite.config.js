import { dirname, resolve } from 'node:path';
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [vue()],
  base:'./',
  build: {
    rollupOptions: {
      output: {
        // Enlève le dossier "assets/" du nom des fichiers générés
        entryFileNames: '[name]-[hash].js',
        chunkFileNames: '[name]-[hash].js',
        assetFileNames: '[name]-[hash].[ext]'
      }
    }
  },
  resolve: {
    dedupe: ['vue', /primevue\/.+/],
  },
})