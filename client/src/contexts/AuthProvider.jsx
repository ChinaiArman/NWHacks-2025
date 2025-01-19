import React, { createContext, useState, useContext, useEffect } from 'react';
import axios from 'axios';

const AuthContext = createContext();

export const useMultiLevelAuth = () => useContext(AuthContext);

export const MultiLevelAuthProvider = ({ children }) => {
    const [isVerified, setIsVerified] = useState(false);
    const [isUnverified, setIsUnverified] = useState(false);
    const [loading, setLoading] = useState(true);

    // Check authentication status
    const checkAuth = async () => {
        try {
            const serverUrl = import.meta.env.VITE_SERVER_URL;  // Use your environment variable here

            // Use Axios to send the request
            const response = await axios.get(`${serverUrl}/api/auth/check-auth-level`, {
                withCredentials: true,  // Ensure credentials are included in the request
            });

            if (response.data.auth_level === 'verified') {
                setIsVerified(true);  // User is verified
                setIsUnverified(false);  // User is not unverified
            } else if (response.data.auth_level === 'unverified') {
                setIsVerified(false);  // User is not verified
                setIsUnverified(true);  // User is unverified
            } else {
                setIsVerified(false);  // User is not verified
                setIsUnverified(false);  // User is not unverified
            }
        } catch (error) {
            setIsVerified(false);  // User is not verified
            setIsUnverified(false);  // User is not unverified
        } finally {
            setLoading(false);  // Authentication check is done
        }
    };

    useEffect(() => {
        checkAuth();  // Check authentication status when app loads
    }, []);

    return (
        <AuthContext.Provider value={{ isVerified, isUnverified, loading }}>
            {children}
        </AuthContext.Provider>
    );
};
