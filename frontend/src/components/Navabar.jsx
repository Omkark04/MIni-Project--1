import React, { useState, useEffect } from "react";
import "../styles/Navbar.css";
import { useNavigate } from "react-router-dom";

function Navbar() {
  const navigate = useNavigate();
  const [isDarkTheme, setIsDarkTheme] = useState(false);
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  // Load saved theme or match system preference
  useEffect(() => {
    const savedTheme = localStorage.getItem("theme");
    const systemPrefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
    const finalTheme = savedTheme || (systemPrefersDark ? "dark" : "light");
    setIsDarkTheme(finalTheme === "dark");
    document.documentElement.setAttribute("data-theme", finalTheme);
  }, []);

  // 🌗 Toggle Theme
  const toggleTheme = () => {
    const newTheme = isDarkTheme ? "light" : "dark";
    setIsDarkTheme(!isDarkTheme);
    document.documentElement.setAttribute("data-theme", newTheme);
    localStorage.setItem("theme", newTheme);
  };

  // 📱 Toggle Mobile Menu
  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  // Navigation handler
  const handleNavClick = (path) => {
    navigate(path);
    setIsMenuOpen(false);
  };

  // 🔍 Search handler
  const handleSearch = (e) => {
    e.preventDefault();
    const query = document.getElementById("searchbar").value.trim();
    if (query) {
      console.log("Searching for:", query);
      // navigate(`/search?q=${encodeURIComponent(query)}`);
    }
  };

  return (
    <nav className="Navbar">
      {/* 🌈 Logo */}
      <div className="logo" onClick={() => handleNavClick("/")}>
        CareerConnect
      </div>

      {/* 🔍 Search Bar (hidden on mobile) */}
      <form className="search" onSubmit={handleSearch}>
        <input
          type="text"
          id="searchbar"
          placeholder="Search jobs, companies..."
        />
        <button id="Search" type="submit">
          <span className="search-text">Search</span>
        </button>
      </form>

      {/* 🌐 Navigation Links */}
      <div className={`Navlinks ${isMenuOpen ? "open" : ""}`}>
        <ul>
          <li>
            <a
              href="#predictor"
              onClick={(e) => {
                e.preventDefault();
                handleNavClick("/predictor");
              }}
            >
              Job Predictor
            </a>
          </li>
          <li>
            <a
              href="#roles"
              onClick={(e) => {
                e.preventDefault();
                handleNavClick("/roles");
              }}
            >
              Job Roles
            </a>
          </li>
          <li>
            <a
              href="#about"
              onClick={(e) => {
                e.preventDefault();
                handleNavClick("/about");
              }}
            >
              About Us
            </a>
          </li>
          <li>
            <a
              href="#faqs"
              onClick={(e) => {
                e.preventDefault();
                handleNavClick("/faqs");
              }}
            >
              FAQs
            </a>
          </li>
        </ul>
      </div>

      {/* ⚙️ Controls (Theme + Auth + Menu Toggle) */}
      <div className="auth-buttons">
        {/* Theme Toggle */}
        <button
          className="theme-toggle"
          onClick={toggleTheme}
          aria-label={isDarkTheme ? "Switch to light theme" : "Switch to dark theme"}
        >
          {isDarkTheme ? "☀️" : "🌙"}
        </button>

        {/* Auth Buttons (Hidden on mobile) */}
        <button
          className="login-btn"
          onClick={() => handleNavClick("/login")}
        >
          Login
        </button>
        <button
          className="register-btn"
          onClick={() => handleNavClick("/register")}
        >
          Register
        </button>

        {/* 🍔 Mobile Menu Toggle */}
        <div
          className={`menu-toggle ${isMenuOpen ? "active" : ""}`}
          onClick={toggleMenu}
          aria-label="Toggle navigation menu"
        >
          <div></div>
          <div></div>
          <div></div>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
