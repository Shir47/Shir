import type { Config } from 'tailwindcss';
import tailwindcssAnimate from 'tailwindcss-animate'; // Required for the plugin

const config: Config = {
  darkMode: ['class'],
  content: [
    './pages/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
    './app/**/*.{ts,tsx}',
    './src/**/*.{ts,tsx}',
  ],
  prefix: '',
  theme: {
    container: {
      center: true,
      padding: '1rem',
    },
    screens: {
      sm: '660px',
      md: '760px',
      lg: '960px',
      xl: '1200px',
    },
    extend: {
      colors: {
        primary: '#16213F',
        secondary: '#050D28',
        lighted: '#EFEFEF',
        blue: {
          DEFAULT: '#336DFF',
          hover: '#336DFF',
        },
      },
      keyframes: {
        'accordion-down': {
          from: { height: '0' },
          to: { height: 'var(--radix-accordion-content-height)' },
        },
        'accordion-up': {
          from: { height: 'var(--radix-accordion-content-height)' },
          to: { height: '0' },
        },
      },
      animation: {
        'accordion-down': 'accordion-down 0.2s ease-out',
        'accordion-up': 'accordion-up 0.2s ease-out',
      },
    },
  },
  plugins: [tailwindcssAnimate],
};

export default config;
