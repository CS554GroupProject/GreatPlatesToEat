import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context(s)/AuthContext';

const LoginPage = () => {
  const { login } = useAuth();
  const [username, setUsername] = useState('');
  const navigate = useNavigate();

  const handleLogin = () => {
    login(username);
    navigate('/');
  };

  return (
    <div>
      <input
        type="text"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        placeholder="Enter Username"
      />
      <button onClick={handleLogin}>Login</button>
    </div>
  );
};

export default LoginPage;
