import React from 'react';
import Button from '../components/Button';

const UnderConstruction = () => {
  return (
    <div className="h-screen w-full bg-bright-lavender flex flex-col items-center justify-center relative">
      <div className="text-5xl font-bold text-white mb-6 animate__animated animate__fadeIn">
        Under Construction
      </div>
      <div className="text-xl text-gray-300 mb-4 animate__animated animate__fadeIn animate__delay-1s">
        We're building something awesome! Stay tuned!
      </div>
      {/* Geometric shapes */}
      <div className="absolute top-16 left-16 w-32 h-32 bg-toolbox clip-triangle opacity-20 animate-pulse rotate-45"></div>
        <div className="absolute top-48 left-36 w-40 h-40 bg-tango-pink clip-triangle opacity-30 animate-pulse rotate-90"></div>
        <div className="absolute top-80 right-20 w-28 h-28 bg-platinum clip-triangle opacity-25 animate-pulse rotate-45"></div>
        <div className="absolute bottom-20 left-16 w-48 h-48 bg-toolbox clip-triangle opacity-20 animate-pulse rotate-45"></div>
        <div className="absolute bottom-10 right-40 w-40 h-40 bg-tango-pink clip-triangle opacity-30 animate-pulse rotate-45"></div>
        <div className="absolute bottom-10 left-10 w-32 h-32 bg-platinum clip-triangle opacity-25 animate-pulse rotate-180"></div>
        {/* button back home */}
        <Button text="BACK HOME" color="toolbox" redirectTo="/dashboard" />
    </div>
  );
};

export default UnderConstruction;
