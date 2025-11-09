import React, { useState } from 'react';
import '../styles/SearchForm.css';

const SearchForm = ({ onSearch, loading }) => {
  const [searchParams, setSearchParams] = useState({
    keywords: 'Data Scientist',
    location: 'Germany'
  });

  const handleInputChange = (e) => {
    setSearchParams({
      ...searchParams,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (searchParams.keywords.trim() && searchParams.location.trim()) {
      onSearch(searchParams.keywords, searchParams.location);
    }
  };

  return (
    <div className="search-form-container">
      <h2>🔍 LinkedIn Job Scraper</h2>
      <p className="subtitle">Find and scrape job listings from LinkedIn</p>
      
      <form onSubmit={handleSubmit} className="search-form">
        <div className="form-group">
          <label htmlFor="keywords">Job Title/Keywords</label>
          <input
            type="text"
            id="keywords"
            name="keywords"
            placeholder="e.g., Data Scientist, Python Developer..."
            value={searchParams.keywords}
            onChange={handleInputChange}
            disabled={loading}
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="location">Location</label>
          <input
            type="text"
            id="location"
            name="location"
            placeholder="e.g., Germany, Berlin, Remote..."
            value={searchParams.location}
            onChange={handleInputChange}
            disabled={loading}
          />
        </div>
        
        <button 
          type="submit" 
          className="search-btn"
          disabled={loading || !searchParams.keywords.trim() || !searchParams.location.trim()}
        >
          {loading ? (
            <>
              <span className="spinner-small"></span>
              Scraping Jobs...
            </>
          ) : (
            '🚀 Scrape Jobs'
          )}
        </button>
      </form>
    </div>
  );
};

export default SearchForm;