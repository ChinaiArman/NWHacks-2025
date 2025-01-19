import React from 'react';
import RegisterForm from '../components/RegisterForm';

const Register = () => {
  return (
    <div className="h-screen w-full bg-bright-lavender flex flex-col">
      {/* Background Triangles */}
      {/* Triangle 1 */}
      <div className="absolute top-16 left-16 w-48 h-48 bg-toolbox clip-triangle opacity-25 animate-pulse rotate-45"></div>

      {/* Triangle 2 */}
      <div className="absolute top-40 left-36 w-40 h-40 bg-tango-pink clip-triangle opacity-30 animate-pulse rotate-90"></div>

      {/* Triangle 3 */}
      <div className="absolute top-80 right-16 w-32 h-32 bg-platinum clip-triangle opacity-20 animate-pulse rotate-120"></div>

      {/* Main Content */}
      <div className="relative z-10 flex flex-col items-center justify-center p-8 text-center min-h-screen">
            <RegisterForm />
        </div>
    </div>
  );
};

export default Register;
