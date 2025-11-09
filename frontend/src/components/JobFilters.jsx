import React from 'react';
import '../styles/JobFilters.css';

const JobFilters = ({ onFilterChange, currentFilters, jobs }) => {
  // Extract filter options from current jobs data
  const extractFilterOptions = () => {
    const categories = new Set();
    const locations = new Set();
    const companies = new Set();

    jobs.forEach(job => {
      if (job.category && job.category !== 'N/A') {
        categories.add(job.category);
      }
      if (job.location && job.location !== 'N/A') {
        locations.add(job.location);
      }
      if (job.company && job.company !== 'N/A') {
        companies.add(job.company);
      }
    });

    return {
      categories: Array.from(categories).sort(),
      locations: Array.from(locations).sort(),
      companies: Array.from(companies).sort()
    };
  };

  const filterOptions = extractFilterOptions();

  const handleFilterChange = (filterType, value) => {
    onFilterChange({
      ...currentFilters,
      [filterType]: value
    });
  };

  const clearFilters = () => {
    onFilterChange({
      category: 'all',
      location: 'all',
      company: 'all',
      search: ''
    });
  };

  return (
    <div className="job-filters">
      <div className="filters-header">
        <h3>🔍 Filters</h3>
        <div className="filters-header-right">
          <span className="filter-count">
            Showing {jobs.length} jobs
          </span>
          <button onClick={clearFilters} className="clear-filters-btn">
            Clear All
          </button>
        </div>
      </div>

      <div className="filters-grid">
        {/* Search Input */}
        <div className="filter-group">
          <label>Search Jobs</label>
          <input
            type="text"
            placeholder="Search by title, company, location, category..."
            value={currentFilters.search || ''}
            onChange={(e) => handleFilterChange('search', e.target.value)}
            className="search-input"
          />
        </div>

        {/* Category Filter */}
        <div className="filter-group">
          <label>Category ({filterOptions.categories.length})</label>
          <select
            value={currentFilters.category || 'all'}
            onChange={(e) => handleFilterChange('category', e.target.value)}
            className="filter-select"
          >
            <option value="all">All Categories</option>
            {filterOptions.categories.map(category => (
              <option key={category} value={category}>{category}</option>
            ))}
          </select>
        </div>

        {/* Location Filter */}
        <div className="filter-group">
          <label>Location ({filterOptions.locations.length})</label>
          <select
            value={currentFilters.location || 'all'}
            onChange={(e) => handleFilterChange('location', e.target.value)}
            className="filter-select"
          >
            <option value="all">All Locations</option>
            {filterOptions.locations.map(location => (
              <option key={location} value={location}>{location}</option>
            ))}
          </select>
        </div>

        {/* Company Filter */}
        <div className="filter-group">
          <label>Company ({filterOptions.companies.length})</label>
          <select
            value={currentFilters.company || 'all'}
            onChange={(e) => handleFilterChange('company', e.target.value)}
            className="filter-select"
          >
            <option value="all">All Companies</option>
            {filterOptions.companies.map(company => (
              <option key={company} value={company}>{company}</option>
            ))}
          </select>
        </div>
      </div>

      {/* Active Filters */}
      <div className="active-filters">
        {Object.entries(currentFilters).map(([key, value]) => {
          if (value && value !== 'all' && value !== '') {
            const displayKey = key.charAt(0).toUpperCase() + key.slice(1);
            return (
              <span key={key} className="active-filter">
                {displayKey}: {value}
                <button 
                  onClick={() => handleFilterChange(key, key === 'search' ? '' : 'all')}
                  className="remove-filter-btn"
                >
                  ×
                </button>
              </span>
            );
          }
          return null;
        })}
      </div>
    </div>
  );
};

export default JobFilters;