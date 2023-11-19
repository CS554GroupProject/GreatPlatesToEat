import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../context(s)/AuthContext';

const Header = () => {
  const { currentUser, login, logout } = useAuth();
  return (
    // <header>
    //     <nav>
    //         <Link to="/">Page 1</Link>
    //         <Link to="/page2">Page 2</Link>
    //         <Link to="/page3">Page 3</Link>
    //         <Link to="/about">About</Link>
    //     </nav>
    // </header>
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <Link className="navbar-brand" to="/">
        Home
      </Link>
      <button
        className="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span className="navbar-toggler-icon"></span>
      </button>
      <div className="collapse navbar-collapse" id="navbarNav">
        <ul className="navbar-nav">
          <li className="nav-item active">
            <Link className="nav-link" to="/request">
              Send request
            </Link>
          </li>
          <li className="nav-item">
            <Link className="nav-link" to="/saved">
              Saved Items
            </Link>
          </li>
          <li className="nav-item">
            <Link className="nav-link" to="/about">
              About
            </Link>
          </li>
        </ul>
        <div className="ml-auto">
          {currentUser ? (
            <>
              <div className="d-flex ml-auto">
                <p className="mr-3 tex-center my-auto">
                  {currentUser.username}
                </p>
                <button className="btn btn-primary" onClick={logout}>
                  Logout
                </button>
              </div>
            </>
          ) : (
            <Link to="/login" className="btn btn-primary">
              Login
            </Link>
          )}
        </div>
      </div>
    </nav>
  );
};

export default Header;
