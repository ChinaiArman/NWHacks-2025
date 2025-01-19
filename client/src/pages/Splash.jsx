import React from "react";
import Header from "../components/Header";
import Button from "../components/Button";

export default function Splash() {
  return (
    <div className="h-screen w-full bg-bright-lavender flex flex-col">
      <Header />
      <div className="flex-grow flex flex-col items-center justify-center p-8 relative">
        {/* Background Triangles */}
        <div className="absolute top-16 left-16 w-32 h-32 bg-toolbox clip-triangle opacity-20 animate-pulse rotate-45"></div>
        <div className="absolute top-48 left-36 w-40 h-40 bg-tango-pink clip-triangle opacity-30 animate-pulse rotate-90"></div>
        <div className="absolute top-80 right-20 w-28 h-28 bg-platinum clip-triangle opacity-25 animate-pulse rotate-45"></div>
        <div className="absolute bottom-20 left-16 w-48 h-48 bg-toolbox clip-triangle opacity-20 animate-pulse rotate-45"></div>
        <div className="absolute bottom-10 right-40 w-40 h-40 bg-tango-pink clip-triangle opacity-30 animate-pulse rotate-45"></div>
        <div className="absolute bottom-10 left-10 w-32 h-32 bg-platinum clip-triangle opacity-25 animate-pulse rotate-180"></div>
        <div className="absolute top-40 right-10 w-36 h-36 bg-toolbox clip-triangle opacity-20 animate-pulse rotate-60"></div>
        <div className="absolute top-20 right-80 w-28 h-28 bg-tango-pink clip-triangle opacity-25 animate-pulse rotate-150"></div>
        <div className="absolute bottom-40 left-80 w-24 h-24 bg-platinum clip-triangle opacity-30 animate-pulse rotate-120"></div>
        <div className="absolute bottom-60 left-20 w-48 h-48 bg-toolbox clip-triangle opacity-20 animate-pulse rotate-45"></div>

        {/* Content */}
        <h1 className="text-5xl text-white font-extrabold mb-6">
          Welcome to <span className="text-toolbox">INSERT EPIC APP NAME HERE</span>
        </h1>
        <p className="text-lg text-white opacity-90 mb-8 text-center max-w-lg">
          INSERT EPIC TAGLINE HERE
        </p>
        <div className="flex space-x-4">
          <Button text="DASHBOARD" color="toolbox" redirectTo="/dashboard" />
          <Button text="SIGN UP" color="tango-pink" redirectTo="/register" />
        </div>
      </div>
    </div>
  );
}