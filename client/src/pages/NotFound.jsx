import React from "react";
import ErrorDisplay from "../components/ErrorDisplay";

const NotFound = () => {
  return (
    <div className="h-screen w-full bg-bright-lavender flex flex-col">
      {/* Background Triangles */}
      {/* Triangle 1 */}
      <div className="absolute top-16 left-16 w-48 h-48 bg-toolbox clip-triangle opacity-30 animate-pulse rotate-45"></div>
      
      {/* Triangle 2 */}
      <div className="absolute top-40 left-36 w-40 h-40 bg-tango-pink clip-triangle opacity-40 animate-pulse rotate-90"></div>
      
      {/* Triangle 3 */}
      <div className="absolute top-80 right-16 w-32 h-32 bg-platinum clip-triangle opacity-25 animate-pulse rotate-120"></div>

      {/* Triangle 4 */}
      <div className="absolute bottom-20 left-48 w-56 h-56 bg-toolbox clip-triangle opacity-20 animate-pulse rotate-45"></div>

      {/* Triangle 5 */}
      <div className="absolute bottom-10 right-20 w-40 h-40 bg-tango-pink clip-triangle opacity-35 animate-pulse rotate-135"></div>

      {/* Triangle 6 */}
      <div className="absolute bottom-40 left-8 w-48 h-48 bg-platinum clip-triangle opacity-25 animate-pulse rotate-180"></div>

      {/* Main Content */}
      <div className="relative z-10 flex flex-col items-center justify-center p-8 text-center min-h-screen">
        <ErrorDisplay
            errorCode="404"
            title="Page Not Found"
            description="Sorry, the page you're looking for isn't there."
            buttonText="BACK HOME"
            buttonLink="/"
            helpText="If you believe this is a mistake, please contact support or try again later."
        />
        </div>
    </div>
  );
};

export default NotFound;
