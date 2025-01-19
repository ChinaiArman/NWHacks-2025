/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}", // Covers React components
    "./public/index.html",        // Covers HTML files
  ],
  theme: {
    extend: {
      colors: {
        platinum: "#E5E4E2",
        "tango-pink": "#E4717A",
        "orange-yellow": "#F5C71A",
        toolbox: "#746CC0",
        "bright-lavender": "#BF94E4",
      },
      animation: {
        "pulse-slow": "pulse 2s ease-in-out infinite",
      },
      clipPath: {
        triangle: "polygon(50% 0%, 0% 100%, 100% 100%)", // Triangle clip path
      },
    },
  },
  plugins: [],
};