import React, { useState, useEffect, useCallback } from "react";
import { useNavigate } from "react-router-dom";
import "../styles/Navbar.css";

function Navbar() {
  const navigate = useNavigate();
  const [isDarkTheme, setIsDarkTheme] = useState(false);
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);

  // Load saved theme or match system preference
  useEffect(() => {
    const savedTheme = window.localStorage.getItem("theme");
    const systemPrefersDark = window.matchMedia(
      "(prefers-color-scheme: dark)"
    ).matches;
    const finalTheme = savedTheme || (systemPrefersDark ? "dark" : "light");
    
    setIsDarkTheme(finalTheme === "dark");
    document.documentElement.setAttribute("data-theme", finalTheme);
  }, []);

  // Handle scroll effect
  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 20);
    };

    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  // Toggle Theme
  const toggleTheme = useCallback(() => {
    const newTheme = isDarkTheme ? "light" : "dark";
    setIsDarkTheme(!isDarkTheme);
    document.documentElement.setAttribute("data-theme", newTheme);
    window.localStorage.setItem("theme", newTheme);
  }, [isDarkTheme]);

  // Toggle Mobile Menu
  const toggleMenu = useCallback(() => {
    setIsMenuOpen((prev) => !prev);
  }, []);

  // Navigation handler
  const handleNavClick = useCallback((path) => {
    navigate(path);
    setIsMenuOpen(false);
  }, [navigate]);

  // Search handler
  const handleSearch = useCallback((e) => {
    e.preventDefault();
    const searchInput = e.target.elements.searchbar;
    const query = searchInput?.value?.trim();
    
    if (query) {
      console.log("Searching for:", query);
      // navigate(`/search?q=${encodeURIComponent(query)}`);
      searchInput.value = "";
    }
  }, []);

  // Close menu when clicking outside
  useEffect(() => {
    const handleClickOutside = (e) => {
      if (isMenuOpen && !e.target.closest('.Navbar')) {
        setIsMenuOpen(false);
      }
    };

    document.addEventListener('click', handleClickOutside);
    return () => document.removeEventListener('click', handleClickOutside);
  }, [isMenuOpen]);

  return (
    <nav className={`Navbar ${scrolled ? 'scrolled' : ''}`}>
      {/* Logo */}
      <div 
        className="logo" 
        onClick={() => handleNavClick("/")}
        role="button"
        tabIndex={0}
        onKeyDown={(e) => e.key === 'Enter' && handleNavClick("/")}
      >
        <span className="logo-text">CareerConnect</span>
      </div>

      {/* Search Bar (hidden on mobile) */}
      <form className="search" onSubmit={handleSearch}>
        <div className="search-wrapper">
          <input
            type="text"
            id="searchbar"
            name="searchbar"
            placeholder="Search jobs, companies..."
            aria-label="Search jobs and companies"
          />
          <button 
            id="Search" 
            type="submit" 
            aria-label="Submit search"
          >
            <span className="search-text">Search</span>
          </button>
        </div>
      </form>

      {/* Navigation Links */}
      <div className={`Navlinks ${isMenuOpen ? "open" : ""}`}>
        <ul>
          <li>
            <a
              href="/predictor"
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
              href="/roles"
              onClick={(e) => {
                e.preventDefault();
                handleNavClick("/jobs");
              }}
            >
              Job Roles
            </a>
          </li>
          <li>
            <a
              href="/about"
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
              href="/faqs"
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

      {/* Controls (Theme + Auth + Menu Toggle) */}
      <div className="auth-buttons">
        {/* Theme Toggle */}
        <button
          className="theme-toggle"
          onClick={toggleTheme}
          aria-label={
            isDarkTheme ? "Switch to light theme" : "Switch to dark theme"
          }
          title={isDarkTheme ? "Light mode" : "Dark mode"}
        >
          <span className="theme-icon">
            {isDarkTheme ? "☀️" : "🌙"}
          </span>
        </button>

        {/* Auth Buttons (Hidden on mobile) */}
        <button
          className="login-btn auth-btn"
          onClick={() => handleNavClick("/login")}
        >
          Login
        </button>
        <button
          className="register-btn auth-btn"
          onClick={() => handleNavClick("/register")}
        >
          Register
        </button>

        {/* Mobile Menu Toggle */}
        <button
          className={`menu-toggle ${isMenuOpen ? "active" : ""}`}
          onClick={toggleMenu}
          aria-label="Toggle navigation menu"
          aria-expanded={isMenuOpen}
        >
          <span></span>
          <span></span>
          <span></span>
        </button>
      </div>
    </nav>
  );
}

export default Navbar;