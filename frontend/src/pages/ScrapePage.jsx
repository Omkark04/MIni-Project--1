import React, { useState } from 'react';
import { jobAPI } from '../api';
import ScrapeForm from './ScrapeForm';
import '../styles/ScrapePage.css';

const ScrapePage = () => {
  const [scraping, setScraping] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleScrape = async (keywords, location, category) => {
    setScraping(true);
    setError(null);
    setResult(null);
    
    try {
      console.log('Scraping with:', { keywords, location, category });
      const response = await jobAPI.scrapeJobs(keywords, location, category);
      setResult(response.data);
    } catch (error) {
      console.error('Scraping error:', error);
      setError(error.response?.data?.error || 'Failed to scrape jobs. Please try again.');
    } finally {
      setScraping(false);
    }
  };

  const clearResult = () => {
    setResult(null);
    setError(null);
  };

  return (
    <div className="scrape-page">
      <div className="page-header">
        <h1>Scrape Jobs</h1>
        <p>Find new job listings from LinkedIn by selecting job roles and locations</p>
      </div>

      <ScrapeForm 
        onScrape={handleScrape}
        loading={scraping}
      />

      {/* Results */}
      {result && (
        <div className="result-message success">
          <div className="result-header">
            <h3>Success!</h3>
            <button onClick={clearResult} className="close-btn">×</button>
          </div>
          <p>{result.message}</p>
          <div className="result-stats">
            <span>Jobs Found: {result.jobs_count}</span>
            <span>Time: {new Date().toLocaleTimeString()}</span>
          </div>
          {result.jobs && result.jobs.length > 0 && (
            <div className="scraped-jobs-preview">
              <h4>Recently Scraped Jobs:</h4>
              <div className="jobs-preview-list">
                {result.jobs.slice(0, 5).map((job, index) => (
                  <div key={index} className="job-preview-item">
                    <strong>{job.title}</strong> at {job.company}
                  </div>
                ))}
                {result.jobs.length > 5 && (
                  <div className="more-jobs">... and {result.jobs.length - 5} more jobs</div>
                )}
              </div>
            </div>
          )}
        </div>
      )}

      {error && (
        <div className="result-message error">
          <div className="result-header">
            <h3>Error</h3>
            <button onClick={clearResult} className="close-btn">×</button>
          </div>
          <p>{error}</p>
        </div>
      )}
    </div>
  );
};

export default ScrapePage;