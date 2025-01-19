module.exports = {
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
    },
  },
  plugins: [],
};