import React from 'react';
import '../styles/JobCard.css';

const JobCard = ({ job }) => {
  const formatDate = (dateString) => {
    if (!dateString || dateString === 'N/A') return 'Recently';
    return dateString;
  };

  const getImageUrl = () => {
    if (job.image_filename) {
      return `http://localhost:8000/media/job_images/${job.image_filename}`;
    }
    return '/placeholder-company.png';
  };

  return (
    <div className="job-card">
      <div className="job-card-header">
        <div className="company-logo-container">
          <img 
            src={getImageUrl()}
            alt={`${job.company} logo`}
            className="company-logo"
            onError={(e) => {
              e.target.style.display = 'none';
              e.target.nextSibling.style.display = 'flex';
            }}
          />
          <div className="company-logo-placeholder">
            {job.company ? job.company.charAt(0).toUpperCase() : '?'}
          </div>
        </div>
        
        <div className="job-basic-info">
          <h3 className="job-title">{job.title}</h3>
          <p className="company-name">{job.company}</p>
          <div className="job-meta">
            <span className="location">📍 {job.location}</span>
            {job.category && (
              <span className="category">🏷️ {job.category}</span>
            )}
            <span className="date">📅 {formatDate(job.date_posted)}</span>
          </div>
        </div>
      </div>
      
      <div className="job-card-actions">
        <a 
          href={job.job_link} 
          target="_blank" 
          rel="noopener noreferrer"
          className="apply-btn"
        >
          View on LinkedIn
        </a>
      </div>
    </div>
  );
};

export default JobCard;