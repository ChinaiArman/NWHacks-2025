import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { MultiLevelAuthProvider } from './contexts/AuthProvider';
import PrivateRoute from './components/PrivateRoute';
import Splash from './pages/Splash';
import NotFound from './pages/NotFound';
import Dashboard from './pages/Dashboard';
import Login from './pages/Login';
import Register from './pages/Register';
import UnderConstruction from './pages/UnderConstruction';

const App = () => {
  return (
    <div className='flex h-screen bg-bright-lavender text-gray-100 overflow-hidden'>
      <MultiLevelAuthProvider>
        <Router>
          <Routes>
            {/* Public Routes */}
            <Route path='/' element={<Splash />} />
            <Route path='/login' element={<Login />} />
            <Route path='/register' element={<Register />} />
            <Route path='/construction' element={<UnderConstruction />} />
            
            {/* Protected Routes */}
            <Route path='/dashboard' element={<PrivateRoute role='verified'><Dashboard /></PrivateRoute>} />

            {/* 404 Route */}
            <Route path='*' element={<NotFound />} />
          </Routes>
        </Router>
      </MultiLevelAuthProvider>
    </div>
  );
}

export default App;