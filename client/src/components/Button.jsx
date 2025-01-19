import React from "react";

export default function Button({ text, color, onClick, redirectTo }) {
  const handleClick = () => {
    if (onClick) {
      onClick(); // If onClick function is passed, call it
    }

    if (redirectTo) {
        window.location.href = redirectTo;
    }
  };

  return (
    <button
      onClick={handleClick}
      className={`px-6 py-3 rounded-lg font-bold text-white bg-${color} shadow-lg hover:bg-opacity-90 transition-all transform hover:scale-105`}
    >
      {text}
    </button>
  );
}
