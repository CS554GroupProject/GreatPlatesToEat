// Main app file, holds the router and use context providers usually
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import './App.css';
import Header from './components/Header';
import Footer from './components/Footer';
import About from './pages/About';
import LoginPage from './pages/LoginPage';
import RequestRecipesPage from './pages/RequestRecipesPage';
import { AuthProvider } from './context(s)/AuthContext';
import { UserItemsProvider } from './context(s)/RecipeStorageContext';
import SavedRecipesPage from './pages/SavedRecipesPage';
import Home from './pages/Home';

const App = () => {
  return (
    <>
      <UserItemsProvider>
        <AuthProvider>
          <Router>
            <div>
              <Header />
              <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/about" element={<About />} />
                <Route path="/request" element={<RequestRecipesPage />} />
                <Route path="/login" element={<LoginPage />} />
                <Route path="/saved" element={<SavedRecipesPage />} />
              </Routes>
              <Footer />
            </div>
          </Router>
        </AuthProvider>
      </UserItemsProvider>
    </>
  );
};

export default App;
