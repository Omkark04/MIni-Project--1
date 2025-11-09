import React, { useState, useEffect } from 'react';
import { jobAPI } from '../api';
import JobFilters from './JobFilters';
import JobCard from './JobCard';
import LoadingSpinner from './LoadingSpinnner';
import '../styles/JobList.css';
import Navbar from './Navabar';

const JobListPage = () => {
  const [allJobs, setAllJobs] = useState([]); // All jobs from API
  const [filteredJobs, setFilteredJobs] = useState([]); // Jobs after filtering
  const [loading, setLoading] = useState(false);
  const [filters, setFilters] = useState({
    category: 'all',
    location: 'all',
    company: 'all',
    search: ''
  });

  // Load all jobs on component mount
  useEffect(() => {
    loadJobs();
  }, []);

  // Apply filters whenever filters or allJobs change
  useEffect(() => {
    applyFilters();
  }, [filters, allJobs]);

  const loadJobs = async () => {
    setLoading(true);
    try {
      const response = await jobAPI.getJobs();
      setAllJobs(response.data.results || response.data);
    } catch (error) {
      console.error('Error loading jobs:', error);
    } finally {
      setLoading(false);
    }
  };

  const applyFilters = () => {
    let filtered = [...allJobs];

    // Apply category filter
    if (filters.category && filters.category !== 'all') {
      filtered = filtered.filter(job => 
        job.category && job.category.toLowerCase().includes(filters.category.toLowerCase())
      );
    }

    // Apply location filter
    if (filters.location && filters.location !== 'all') {
      filtered = filtered.filter(job => 
        job.location && job.location.toLowerCase().includes(filters.location.toLowerCase())
      );
    }

    // Apply company filter
    if (filters.company && filters.company !== 'all') {
      filtered = filtered.filter(job => 
        job.company && job.company.toLowerCase().includes(filters.company.toLowerCase())
      );
    }

    // Apply search filter
    if (filters.search) {
      const searchLower = filters.search.toLowerCase();
      filtered = filtered.filter(job =>
        (job.title && job.title.toLowerCase().includes(searchLower)) ||
        (job.company && job.company.toLowerCase().includes(searchLower)) ||
        (job.location && job.location.toLowerCase().includes(searchLower)) ||
        (job.category && job.category.toLowerCase().includes(searchLower))
      );
    }

    setFilteredJobs(filtered);
  };

  const handleFilterChange = (newFilters) => {
    setFilters(newFilters);
  };

  return (
    <div className="job-list-page">
      <Navbar/>
      <div className="page-header">
        <h1>💼 Job Listings</h1>
        <p>Browse and filter through available job opportunities</p>
      </div>

      <JobFilters 
        onFilterChange={handleFilterChange}
        currentFilters={filters}
        jobs={allJobs} // Pass all jobs to extract filter options
      />

      <div className="jobs-section">
        <div className="jobs-header">
          <h2>
            Available Jobs 
            <span className="jobs-count">
              ({filteredJobs.length} of {allJobs.length})
            </span>
          </h2>
          <button 
            onClick={loadJobs} 
            disabled={loading}
            className="refresh-btn"
          >
            {loading ? '🔄 Refreshing...' : '🔄 Refresh'}
          </button>
        </div>

        {loading && <LoadingSpinner message="Loading jobs..." />}

        {!loading && filteredJobs.length > 0 && (
          <>
            <div className="jobs-grid">
              {filteredJobs.map(job => (
                <JobCard key={job.id} job={job} />
              ))}
            </div>
          </>
        )}

        {!loading && allJobs.length === 0 && (
          <div className="empty-state">
            <div className="empty-icon">📭</div>
            <h3>No jobs found</h3>
            <p>Try scraping some jobs first or check back later for new listings.</p>
          </div>
        )}

        {!loading && allJobs.length > 0 && filteredJobs.length === 0 && (
          <div className="empty-state">
            <div className="empty-icon">🔍</div>
            <h3>No matching jobs found</h3>
            <p>Try adjusting your filters to see more results.</p>
            <button onClick={() => setFilters({
              category: 'all',
              location: 'all',
              company: 'all',
              search: ''
            })} className="clear-filters-prompt">
              Clear all filters
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

export default JobListPage;