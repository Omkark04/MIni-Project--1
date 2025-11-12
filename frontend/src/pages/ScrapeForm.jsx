import React, { useState, useEffect } from 'react';
import '../styles/ScrapeForm.css';
import api, { jobAPI } from '../api';

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
  "Network", "Operations", "PMO", "Python Developer", "SAP", "Sales", "Testing", "Web Design"
];

const ScrapeForm = ({ onScrape, loading }) => {
  const [isVerified, setIsVerified] = useState(false);
  const [scrapingConfig, setScrapingConfig] = useState({
    categories: [],
    locations: [],
    scrape_all_categories: false,
    scrape_all_locations: false,
    session_name: ''
  });
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [authLoading, setAuthLoading] = useState(false);
  const [sessions, setSessions] = useState([]);

  useEffect(() => {
    if (isVerified) {
      fetchSessions();
    }
  }, [isVerified]);

  const fetchSessions = async () => {
    try {
      const response = await jobAPI.getSessions();
      setSessions(response.data);
    } catch (error) {
      console.error('Error fetching sessions:', error);
    }
  };

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

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!scrapingConfig.scrape_all_categories && scrapingConfig.categories.length === 0) {
      alert('Please select at least one category or choose "All Categories"');
      return;
    }
    
    if (!scrapingConfig.scrape_all_locations && scrapingConfig.locations.length === 0) {
      alert('Please select at least one location or choose "All Locations"');
      return;
    }

    try {
      await onScrape(scrapingConfig);
      setTimeout(fetchSessions, 2000);
    } catch (error) {
      alert('Scraping failed: ' + error.message);
    }
  };

  const handleDeleteSession = async (sessionId) => {
    if (!window.confirm('Are you sure you want to delete this session and all associated jobs?')) {
      return;
    }

    try {
      await jobAPI.deleteSession(sessionId);
      alert('Session deleted successfully!');
      fetchSessions();
    } catch (error) {
      alert('Error deleting session: ' + error.response?.data?.error || error.message);
    }
  };

  const handleConfigChange = (key, value) => {
    setScrapingConfig(prev => ({
      ...prev,
      [key]: value
    }));
  };

  const handleCategoryToggle = (category) => {
    setScrapingConfig(prev => ({
      ...prev,
      categories: prev.categories.includes(category)
        ? prev.categories.filter(c => c !== category)
        : [...prev.categories, category]
    }));
  };

  const handleLocationToggle = (location) => {
    setScrapingConfig(prev => ({
      ...prev,
      locations: prev.locations.includes(location)
        ? prev.locations.filter(l => l !== location)
        : [...prev.locations, location]
    }));
  };

  const selectAllCategories = () => {
    setScrapingConfig(prev => ({
      ...prev,
      categories: [...CATEGORIES],
      scrape_all_categories: false
    }));
  };

  const clearAllCategories = () => {
    setScrapingConfig(prev => ({
      ...prev,
      categories: [],
      scrape_all_categories: false
    }));
  };

  const selectAllLocations = () => {
    setScrapingConfig(prev => ({
      ...prev,
      locations: [...LOCATIONS],
      scrape_all_locations: false
    }));
  };

  const clearAllLocations = () => {
    setScrapingConfig(prev => ({
      ...prev,
      locations: [],
      scrape_all_locations: false
    }));
  };

  if (!isVerified) {
    return (
      <div className="scrape-dashboard">
        <div className="auth-container">
          <div className="auth-card">
            <div className="auth-header">
              <div className="auth-icon">
                <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                  <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                </svg>
              </div>
              <h2>Admin Verification</h2>
              <p className="auth-subtitle">Please verify your credentials to access the scraping dashboard</p>
            </div>
            
            <form onSubmit={AdminVerify} className="auth-form">
              <div className="form-group">
                <label htmlFor="username">Username</label>
                <div className="input-wrapper">
                  <span className="input-icon">👤</span>
                  <input
                    type="text"
                    id="username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    disabled={authLoading}
                    required
                    className="form-input"
                    placeholder="Enter your username"
                  />
                </div>
              </div>
              
              <div className="form-group">
                <label htmlFor="password">Password</label>
                <div className="input-wrapper">
                  <span className="input-icon">🔒</span>
                  <input
                    type="password"
                    id="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    disabled={authLoading}
                    required
                    className="form-input"
                    placeholder="Enter your password"
                  />
                </div>
              </div>

              <button 
                type="submit" 
                className="gradient-btn primary-btn"
                disabled={authLoading || !username || !password}
              >
                {authLoading ? (
                  <>
                    <span className="spinner"></span>
                    Verifying...
                  </>
                ) : (
                  <>
                    <span>Verify & Continue</span>
                    <span className="btn-arrow">→</span>
                  </>
                )}
              </button>
            </form>
          </div>
        </div>
      </div>
    );
  }

  const totalCombinations = 
    (scrapingConfig.scrape_all_categories ? CATEGORIES.length : scrapingConfig.categories.length) * 
    (scrapingConfig.scrape_all_locations ? LOCATIONS.length : scrapingConfig.locations.length);

  return (
    <div className="scrape-dashboard">
      {/* Dashboard Header */}
      <div className="dashboard-header">
        <div className="header-content">
          <div className="header-left">
            <h1 className="dashboard-title">
              <span className="title-icon">🚀</span>
              Job Scraping Dashboard
            </h1>
            <p className="dashboard-subtitle">Configure and manage your scraping sessions</p>
          </div>
          <div className="header-right">
            <button className="icon-btn notification-btn">
              <span className="icon">🔔</span>
              <span className="notification-badge">{sessions.length}</span>
            </button>
            <button 
              className="logout-btn"
              onClick={() => setIsVerified(false)}
            >
              <span className="icon">🚪</span>
              Logout
            </button>
          </div>
        </div>
      </div>

      {/* Stats Overview */}
      <div className="stats-section">
        <div className="stat-card">
          <div className="stat-icon blue">📊</div>
          <div className="stat-content">
            <h3 className="stat-value">{sessions.length}</h3>
            <p className="stat-label">Total Sessions</p>
          </div>
        </div>
        
        <div className="stat-card">
          <div className="stat-icon green">✅</div>
          <div className="stat-content">
            <h3 className="stat-value">
              {sessions.filter(s => s.status === 'completed').length}
            </h3>
            <p className="stat-label">Completed</p>
          </div>
        </div>
        
        <div className="stat-card">
          <div className="stat-icon purple">💼</div>
          <div className="stat-content">
            <h3 className="stat-value">
              {sessions.reduce((acc, s) => acc + (s.jobs_count || 0), 0)}
            </h3>
            <p className="stat-label">Total Jobs</p>
          </div>
        </div>
        
        <div className="stat-card">
          <div className="stat-icon orange">⚡</div>
          <div className="stat-content">
            <h3 className="stat-value">{totalCombinations}</h3>
            <p className="stat-label">Combinations</p>
          </div>
        </div>
      </div>

      {/* Main Content Grid */}
      <div className="dashboard-grid">
        {/* Scraping Configuration */}
        <div className="config-section">
          <div className="section-card">
            <div className="section-header">
              <h2 className="section-title">
                <span className="title-icon">⚙️</span>
                Scraping Configuration
              </h2>
            </div>
            
            <form onSubmit={handleSubmit} className="config-form">
              <div className="form-group">
                <label htmlFor="session_name">Session Name</label>
                <input
                  type="text"
                  id="session_name"
                  value={scrapingConfig.session_name}
                  onChange={(e) => handleConfigChange('session_name', e.target.value)}
                  className="form-input"
                  placeholder="e.g., Tech Jobs Q4 2024"
                />
                <span className="input-hint">Optional: Give your session a memorable name</span>
              </div>

              {/* Categories Selection */}
              <div className="form-group">
                <div className="selection-header">
                  <label className="main-label">
                    <span className="label-icon">🏷️</span>
                    Job Categories
                    <span className="required">*</span>
                  </label>
                  <div className="selection-actions">
                    <button type="button" onClick={selectAllCategories} className="action-btn">
                      Select All
                    </button>
                    <button type="button" onClick={clearAllCategories} className="action-btn">
                      Clear
                    </button>
                  </div>
                </div>
                
                <div className="checkbox-group">
                  <label className="checkbox-card highlight">
                    <input
                      type="checkbox"
                      checked={scrapingConfig.scrape_all_categories}
                      onChange={(e) => handleConfigChange('scrape_all_categories', e.target.checked)}
                    />
                    <span className="checkbox-label">
                      <span className="checkbox-icon">🌐</span>
                      Scrape All Categories
                    </span>
                  </label>
                </div>

                {!scrapingConfig.scrape_all_categories && (
                  <>
                    <div className="multi-select-grid">
                      {CATEGORIES.map(category => (
                        <label key={category} className="checkbox-card">
                          <input
                            type="checkbox"
                            checked={scrapingConfig.categories.includes(category)}
                            onChange={() => handleCategoryToggle(category)}
                          />
                          <span className="checkbox-label">{category}</span>
                        </label>
                      ))}
                    </div>
                    
                    <div className="selection-counter">
                      <span className="counter-badge">
                        {scrapingConfig.categories.length} selected
                      </span>
                    </div>
                  </>
                )}
              </div>

              {/* Locations Selection */}
              <div className="form-group">
                <div className="selection-header">
                  <label className="main-label">
                    <span className="label-icon">📍</span>
                    Locations
                    <span className="required">*</span>
                  </label>
                  <div className="selection-actions">
                    <button type="button" onClick={selectAllLocations} className="action-btn">
                      Select All
                    </button>
                    <button type="button" onClick={clearAllLocations} className="action-btn">
                      Clear
                    </button>
                  </div>
                </div>
                
                <div className="checkbox-group">
                  <label className="checkbox-card highlight">
                    <input
                      type="checkbox"
                      checked={scrapingConfig.scrape_all_locations}
                      onChange={(e) => handleConfigChange('scrape_all_locations', e.target.checked)}
                    />
                    <span className="checkbox-label">
                      <span className="checkbox-icon">🌍</span>
                      Scrape All Locations
                    </span>
                  </label>
                </div>

                {!scrapingConfig.scrape_all_locations && (
                  <>
                    <div className="multi-select-grid">
                      {LOCATIONS.map(location => (
                        <label key={location} className="checkbox-card">
                          <input
                            type="checkbox"
                            checked={scrapingConfig.locations.includes(location)}
                            onChange={() => handleLocationToggle(location)}
                          />
                          <span className="checkbox-label">{location}</span>
                        </label>
                      ))}
                    </div>
                    
                    <div className="selection-counter">
                      <span className="counter-badge">
                        {scrapingConfig.locations.length} selected
                      </span>
                    </div>
                  </>
                )}
              </div>

              {/* Info Box */}
              <div className="info-box">
                <div className="info-icon">ℹ️</div>
                <div className="info-content">
                  <h4>Scraping Summary</h4>
                  <ul>
                    <li>
                      <strong>{totalCombinations}</strong> total combinations will be processed
                    </li>
                    <li>Each category-location pair is scraped separately</li>
                    <li>Large selections may take significant time</li>
                  </ul>
                </div>
              </div>

              <button 
                type="submit" 
                className="gradient-btn primary-btn submit-btn"
                disabled={loading || 
                  (!scrapingConfig.scrape_all_categories && scrapingConfig.categories.length === 0) ||
                  (!scrapingConfig.scrape_all_locations && scrapingConfig.locations.length === 0)
                }
              >
                {loading ? (
                  <>
                    <span className="spinner"></span>
                    Scraping in Progress...
                  </>
                ) : (
                  <>
                    <span className="btn-icon">🚀</span>
                    Start Advanced Scraping
                  </>
                )}
              </button>
            </form>
          </div>
        </div>

        {/* Sessions Section */}
        <div className="sessions-section">
          <div className="section-card">
            <div className="section-header">
              <h2 className="section-title">
                <span className="title-icon">📋</span>
                Scraping Sessions
              </h2>
            </div>
            
            <div className="sessions-list">
              {sessions.length === 0 ? (
                <div className="empty-state">
                  <div className="empty-icon">📭</div>
                  <h3>No Sessions Yet</h3>
                  <p>Start your first scraping session to see results here</p>
                </div>
              ) : (
                sessions.map(session => (
                  <div key={session.id} className="session-card">
                    <div className="session-header">
                      <h4 className="session-name">
                        <span className="session-icon">📄</span>
                        {session.name || `Session #${session.id}`}
                      </h4>
                      <button 
                        className="delete-btn"
                        onClick={() => handleDeleteSession(session.id)}
                        title="Delete session"
                      >
                        <span>🗑️</span>
                      </button>
                    </div>
                    
                    <div className="session-body">
                      <div className="session-stats">
                        <div className="session-stat">
                          <span className="stat-label">Jobs</span>
                          <span className="stat-value">{session.jobs_count || 0}</span>
                        </div>
                        <div className="session-stat">
                          <span className="stat-label">Categories</span>
                          <span className="stat-value">{session.categories?.length || 0}</span>
                        </div>
                        <div className="session-stat">
                          <span className="stat-label">Locations</span>
                          <span className="stat-value">{session.locations?.length || 0}</span>
                        </div>
                      </div>
                      
                      <div className="session-status">
                        <span className={`status-badge status-${session.status}`}>
                          {session.status === 'completed' && '✅'}
                          {session.status === 'pending' && '⏳'}
                          {session.status === 'failed' && '❌'}
                          {session.status}
                        </span>
                      </div>
                      
                      <div className="session-meta">
                        <div className="meta-item">
                          <span className="meta-icon">📅</span>
                          <span className="meta-text">
                            {new Date(session.created_at).toLocaleDateString('en-US', {
                              month: 'short',
                              day: 'numeric',
                              year: 'numeric',
                              hour: '2-digit',
                              minute: '2-digit'
                            })}
                          </span>
                        </div>
                        {session.completed_at && (
                          <div className="meta-item">
                            <span className="meta-icon">✓</span>
                            <span className="meta-text">
                              {new Date(session.completed_at).toLocaleDateString('en-US', {
                                month: 'short',
                                day: 'numeric',
                                hour: '2-digit',
                                minute: '2-digit'
                              })}
                            </span>
                          </div>
                        )}
                      </div>
                    </div>
                  </div>
                ))
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ScrapeForm;