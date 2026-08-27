/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './*.html',
    './layout/**/*.liquid',
    './sections/**/*.liquid',
    './snippets/**/*.liquid',
    './templates/**/*.json',
    './assets/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        brandDark: '#0a0b0e',
        brandCard: '#12151c',
        brandEmerald: '#123824',
        brandGold: '#d4af37',
        brandGoldLight: '#e6c265',
      },
      fontFamily: {
        serif: ['Cormorant Garamond', 'Georgia', 'serif'],
        sans: ['Plus Jakarta Sans', 'system-ui', '-apple-system', 'sans-serif'],
      }
    }
  },
  plugins: [],
}

