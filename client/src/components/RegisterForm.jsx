import { useState } from 'react';
import axios from 'axios';
import { AlertCircle, X } from 'lucide-react';

const RegisterForm = () => {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const handleRegistration = async (e) => {
        e.preventDefault();
        try {
            const serverUrl = import.meta.env.VITE_SERVER_URL;
            const response = await axios.post(
                `${serverUrl}/api/auth/register`,
                { username, email, password },
                { withCredentials: true }
            )
            if (response.status === 200) {
                console.log('Registration successful:', response.data);
                window.location.href = '/dashboard';
            } else {
                setError('Incorrect username or password');
            }
        } catch (error) {
            setError('Incorrect username or password');
            console.error('Registration failed:', error);
        }
    };

    return (
        <section className="relative w-[30rem] flex flex-col space-y-10 p-8 rounded-lg">
            <div className="text-center text-4xl font-bold text-white">Sign Up</div>
            
            {/* Error Message */}
            {error && (
                <div className="flex items-center justify-between w-full p-4 mb-4 text-white bg-tango-pink rounded-lg">
                    <div className="flex items-center">
                        <AlertCircle className="h-5 w-5 mr-2" />
                        <span>{error}</span>
                    </div>
                    <button 
                        onClick={() => setError('')} 
                        className="text-white focus:outline-none"
                    >
                        <X className="h-5 w-5" />
                    </button>
                </div>
            )}

            {/* Form Inputs */}
            <form onSubmit={handleRegistration} className="flex flex-col space-y-8">
                {/* Username Input */}
                <div className="w-full transform border-b-2 bg-transparent text-lg duration-300 focus-within:border-toolbox">
                    <input 
                        type="text" 
                        placeholder="Username" 
                        className="w-full border-none bg-transparent outline-none placeholder:text-gray-500 focus:outline-none text-white"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                    />
                </div>
                {/* Email Input */}
                <div className="w-full transform border-b-2 bg-transparent text-lg duration-300 focus-within:border-toolbox">
                    <input 
                        type="text" 
                        placeholder="Email" 
                        className="w-full border-none bg-transparent outline-none placeholder:text-gray-500 focus:outline-none text-white"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                    />
                </div>
                
                {/* Password Input */}
                <div className="w-full transform border-b-2 bg-transparent text-lg duration-300 focus-within:border-toolbox">
                    <input 
                        type="password" 
                        placeholder="Password" 
                        className="w-full border-none bg-transparent outline-none placeholder:text-gray-500 focus:outline-none text-white"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    />
                </div>
                
                {/* Submit Button */}
                <button 
                    type="submit"
                    className="transform rounded-lg bg-toolbox py-2 font-bold text-white duration-300 hover:bg-toolbox/80"
                >
                    SIGN UP
                </button>
            </form>
            
            {/* Links */}
            <a href="/construction" className="transform text-center font-semibold text-platinum duration-300 hover:text-platinum/80">
                DON'T HAVE AN ACCOUNT?
            </a>
            <a href="/construction" className="transform text-center font-semibold text-platinum duration-300 hover:text-platinum/80">
                FORGOT PASSWORD?
            </a>
        </section>
    );
};

export default RegisterForm;
