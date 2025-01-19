import { Navigate } from 'react-router-dom';
import { useMultiLevelAuth } from '../contexts/AuthProvider';

const PrivateRoute = ({ children, role }) => {
    const { isVerified, isUnverified, loading } = useMultiLevelAuth();

    if (loading) {
        return <div>Loading...</div>;
    }

    if (role === 'verified' && isVerified ) return children;
    if (role === 'unverified' && isUnverified) return children;
    if (role === 'any') return children;

    // Redirect based on role type
    return <Navigate to="/login" />;
};

export default PrivateRoute;
