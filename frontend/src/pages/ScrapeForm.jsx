import React, { useState } from 'react';
import '../styles/ScrapeForm.css';
import api from '../api';

const LOCATIONS = [
  "United States", "Germany", "United Kingdom", "Canada", "Australia", "France",
  "India", "Japan", "Brazil", "Spain", "Italy", "Netherlands", "Switzerland",
  "Sweden", "Norway", "Denmark", "Finland", "Ireland", "Austria", "Belgium",
  "Portugal", "Poland", "Czech Republic", "Hungary", "Romania", "Greece",
  "Turkey", "Israel", "UAE", "Saudi Arabia", "South Africa", "Singapore",
  "Malaysia", "Thailand", "Vietnam", "Philippines", "South Korea", "Taiwan",
  "Hong Kong", "New Zealand", "Mexico", "Argentina", "Chile", "Colombia",
  "Peru", "Remote", "Hybrid", "On-site"
];

const CATEGORIES = [
  "Advocate", "Arts", "Automation Testing", "BlockChain", "Business Analyst",
  "Civil Engineer", "Data Science", "Database", "DevOps", ".Net", "ETL",
  "Electrical", "HR", "Hadoop", "Health and Fitness", "Java", "Mechanical",
  "Network", "Operations", "PMO", "Python", "SAP", "Sales", "Testing", "Web Design"
];

const ScrapeForm = ({ onScrape, loading }) => {
  const [isVerified, setIsVerified] = useState(false);
  const [formData, setFormData] = useState({
    category: '',
    location: ''
  });
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [authLoading, setAuthLoading] = useState(false);

  const AdminVerify = async (e) => {
    try {
      e.preventDefault();
      setAuthLoading(true);
      const res = await api.post('api/adminverify/', { username, password });
      
      if (res.data.status) {
        setIsVerified(true);
        alert("Admin verified successfully!");
      }
    } catch(error) {
      alert(error.response?.data?.message || "Invalid credentials");
    } finally {
      setAuthLoading(false);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (formData.category && formData.location) {
      onScrape(formData.category, formData.location, formData.category);
    }
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  // Show admin verification form if not verified
  if (!isVerified) {
    return (
      <div className="scrape-form-container">
        <h2>Admin Verification Required</h2>
        <p className="subtitle">Please verify your admin credentials to access the scraping tool</p>
        
        <form onSubmit={AdminVerify} className="scrape-form">
          <div className="form-group">
            <label htmlFor="username">Username *</label>
            <input
              type="text"
              id="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              disabled={authLoading}
              required
              className="form-input"
              placeholder="Enter admin username"
            />
          </div>
          
          <div className="form-group">
            <label htmlFor="password">Password *</label>
            <input
              type="password"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              disabled={authLoading}
              required
              className="form-input"
              placeholder="Enter admin password"
            />
          </div>

          <button 
            type="submit" 
            className="scrape-btn"
            disabled={authLoading || !username || !password}
          >
            {authLoading ? (
              <>
                <span className="spinner-small"></span>
                Verifying...
              </>
            ) : (
              'Verify Admin'
            )}
          </button>
        </form>
      </div>
    );
  }

  // Show scraping form only after verification
  return (
    <div className="scrape-form-container">
      <div className="admin-header">
        <h2>Scrape New Jobs</h2>
        <button 
          className="logout-btn"
          onClick={() => setIsVerified(false)}
        >
          Logout
        </button>
      </div>
      <p className="subtitle">Find new job listings from LinkedIn</p>
      
      <form onSubmit={handleSubmit} className="scrape-form">
        <div className="form-row">
          <div className="form-group">
            <label htmlFor="category">Job Role/Category *</label>
            <select
              id="category"
              name="category"
              value={formData.category}
              onChange={handleChange}
              disabled={loading}
              required
              className="category-select"
            >
              <option value="">Select Job Role</option>
              {CATEGORIES.map(category => (
                <option key={category} value={category}>{category}</option>
              ))}
            </select>
          </div>
          
          <div className="form-group">
            <label htmlFor="location">Location *</label>
            <select
              id="location"
              name="location"
              value={formData.location}
              onChange={handleChange}
              disabled={loading}
              required
              className="location-select"
            >
              <option value="">Select Location</option>
              {LOCATIONS.map(location => (
                <option key={location} value={location}>{location}</option>
              ))}
            </select>
          </div>
        </div>

        <div className="form-info">
          <div className="info-box">
            <strong>How it works:</strong>
            <ul>
              <li>Select a job role/category to search for specific positions</li>
              <li>Choose a location to target your job search</li>
              <li>The system will automatically scrape relevant job listings</li>
              <li>Jobs will be categorized based on the selected role</li>
            </ul>
          </div>
        </div>

        <button 
          type="submit" 
          className="scrape-btn"
          disabled={loading || !formData.category || !formData.location}
        >
          {loading ? (
            <>
              <span className="spinner-small"></span>
              Scraping Jobs...
            </>
          ) : (
            'Start Scraping'
          )}
        </button>
      </form>
    </div>
  );
};

export default ScrapeForm;