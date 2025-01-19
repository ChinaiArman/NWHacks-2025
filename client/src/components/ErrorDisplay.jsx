import React from 'react';

const ErrorDisplay = ({ 
    errorCode,
    title,
    description,
    buttonText,
    buttonLink,
    helpText 
}) => {
    return (
        <section className="flex flex-col items-center space-y-8">
            {/* Large Error Number */}
            <div className="text-9xl font-bold text-toolbox">{errorCode}</div>
           
            {/* SVG Icon */}
            <svg
                className="w-32 h-32 text-platinum"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
            >
                <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                />
            </svg>

            {/* Error Messages */}
            <div className="text-center space-y-4">
                <h1 className="text-4xl font-bold text-white">{title}</h1>
                <p className="text-xl text-white">{description}</p>
            </div>

            {/* Back Button */}
            <a
                href={buttonLink}
                className="transform rounded-lg bg-tango-pink px-8 py-3 font-bold text-white duration-300 hover:bg-tango-pink/80 text-center"
            >
                {buttonText}
            </a>

            {/* Additional Help Text */}
            <p className="text-white text-sm text-center max-w-md">
                {helpText}
            </p>
        </section>
    );
};

export default ErrorDisplay;
