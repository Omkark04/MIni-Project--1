import React, { useState, useCallback } from "react";
import "../styles/Rform.css"
import api from "../api";
import Navbar from "./Navabar";
import JobCard from "./JobCard"; // Import JobCard component

function Rform() {
  const [formData, setFormData] = useState({
    name: "",
    location: "",
    education: "",
    exp: "",
  });
  const [skills, setSkills] = useState([""]);
  const [loading, setLoading] = useState(false);
  const [jobsLoading, setJobsLoading] = useState(false);
  const [errors, setErrors] = useState({});
  const [predictedCategory, setPredictedCategory] = useState("");
  const [categoryJobs, setCategoryJobs] = useState([]);
  const [showJobs, setShowJobs] = useState(false);
  const [allCategoryJobs, setAllCategoryJobs] = useState([]); // All jobs for the predicted category
  const [filteredJobs, setFilteredJobs] = useState([]); // Filtered jobs
  const [filters, setFilters] = useState({
    location: 'all',
    company: 'all',
    search: ''
  });

  // Validate form fields
  const validateForm = () => {
    const newErrors = {};

    if (!formData.name.trim()) {
      newErrors.name = "Full name is required";
    } else if (formData.name.trim().length < 2) {
      newErrors.name = "Name must be at least 2 characters";
    }

    if (formData.exp && formData.exp < 0) {
      newErrors.exp = "Experience cannot be negative";
    }

    const validSkills = skills.filter((skill) => skill.trim() !== "");
    if (validSkills.length === 0) {
      newErrors.skills = "At least one skill is required";
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!validateForm()) {
      return;
    }

    setLoading(true);
    setErrors({});
    setPredictedCategory("");
    setCategoryJobs([]);
    setAllCategoryJobs([]);
    setFilteredJobs([]);
    setShowJobs(false);

    try {
      const validSkills = skills.filter((skill) => skill.trim() !== "");
      
      // Send data to your prediction endpoint
      const res = await api.post("api/rform-data/", {
        ...formData,
        skills: validSkills,
      });

      if (res.data.status) {
        const category = res.data.predicted_category || res.data.message;
        setPredictedCategory(category);
        
        alert("Success: " + res.data.message);
        
      } else {
        setErrors({ submit: res.data.errors || "Prediction failed" });
      }
    } catch (error) {
      const errorMessage =
        error.response?.data?.message || "An error occurred. Please try again.";
      setErrors({ submit: errorMessage });
    } finally {
      setLoading(false);
    }
  };

  // Get jobs for predicted category
  const handleGetJobs = async () => {
    if (!predictedCategory) {
      alert("Please predict a job category first");
      return;
    }

    setJobsLoading(true);
    setShowJobs(true);

    try {
      const res = await api.get(`jobs/?category=${encodeURIComponent(predictedCategory)}`);
      
      // Handle the response based on your API structure
      const jobs = res.data.results || res.data.jobs || res.data;
      const jobsArray = Array.isArray(jobs) ? jobs : [];
      
      setAllCategoryJobs(jobsArray);
      setFilteredJobs(jobsArray);
      setCategoryJobs(jobsArray);
      
    } catch (error) {
      const errorMessage =
        error.response?.data?.message || "Error fetching jobs";
      setErrors({ jobs: errorMessage });
    } finally {
      setJobsLoading(false);
    }
  };

  // Apply filters to jobs
  const applyFilters = useCallback(() => {
    let filtered = [...allCategoryJobs];

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
  }, [filters, allCategoryJobs]);

  // Apply filters when they change
  React.useEffect(() => {
    if (allCategoryJobs.length > 0) {
      applyFilters();
    }
  }, [applyFilters, allCategoryJobs]);

  const handleFilterChange = (newFilters) => {
    setFilters(newFilters);
  };

  // Extract unique filter options
  const getFilterOptions = () => {
    const locations = [...new Set(allCategoryJobs.map(job => job.location).filter(Boolean))];
    const companies = [...new Set(allCategoryJobs.map(job => job.company).filter(Boolean))];
    
    return {
      locations: ['all', ...locations],
      companies: ['all', ...companies]
    };
  };

  // Reset form after user is done
  const resetForm = () => {
    setFormData({
      name: "",
      location: "",
      education: "",
      exp: "",
    });
    setSkills([""]);
    setPredictedCategory("");
    setCategoryJobs([]);
    setAllCategoryJobs([]);
    setFilteredJobs([]);
    setShowJobs(false);
    setFilters({
      location: 'all',
      company: 'all',
      search: ''
    });
  };

  // Handle input changes
  const handleInputChange = useCallback((field, value) => {
    setFormData((prev) => ({
      ...prev,
      [field]: value,
    }));
    
    // Clear error for this field
    if (errors[field]) {
      setErrors((prev) => {
        const newErrors = { ...prev };
        delete newErrors[field];
        return newErrors;
      });
    }
  }, [errors]);

  // Add Skill Field
  const addSkill = useCallback(() => {
    setSkills((prev) => [...prev, ""]);
    
    // Clear skills error
    if (errors.skills) {
      setErrors((prev) => {
        const newErrors = { ...prev };
        delete newErrors.skills;
        return newErrors;
      });
    }
  }, [errors.skills]);

  // Delete Skill
  const delSkill = useCallback((index) => {
    if (skills.length > 1) {
      setSkills((prev) => prev.filter((_, i) => i !== index));
    }
  }, [skills.length]);

  // Update Skill
  const handleSkillChange = useCallback((index, value) => {
    setSkills((prev) => {
      const updated = [...prev];
      updated[index] = value;
      return updated;
    });

    // Clear skills error
    if (errors.skills) {
      setErrors((prev) => {
        const newErrors = { ...prev };
        delete newErrors.skills;
        return newErrors;
      });
    }
  }, [errors.skills]);

  const filterOptions = getFilterOptions();

  return (
    <div className="container">
      <Navbar/>
      <form className="job-form" onSubmit={handleSubmit}>
        <h2 className="form-title">
          Job Role Predictor
        </h2>

        {/* Error Message */}
        {errors.submit && (
          <div className="error-banner" role="alert">
            {errors.submit}
          </div>
        )}

        {/* Full Name */}
        <div className="field">
          <label htmlFor="fullname">
            <h3>Full Name *</h3>
          </label>
          <input
            id="fullname"
            type="text"
            value={formData.name}
            onChange={(e) => handleInputChange("name", e.target.value)}
            placeholder="Enter your full name"
            required
          />
          {errors.name && (
            <span className="error-text">{errors.name}</span>
          )}
        </div>

        {/* Location */}
        <div className="field">
          <label htmlFor="location">
            <h3>Location</h3>
          </label>
          <input
            id="location"
            type="text"
            value={formData.location}
            onChange={(e) => handleInputChange("location", e.target.value)}
            placeholder="Enter your city or region"
          />
        </div>

        {/* Education */}
        <div className="field">
          <label htmlFor="education">
            <h3>Education</h3>
          </label>
          <input
            id="education"
            type="text"
            value={formData.education}
            onChange={(e) => handleInputChange("education", e.target.value)}
            placeholder="e.g., B.Tech in AI & DS"
          />
        </div>

        {/* Experience */}
        <div className="field">
          <label htmlFor="experience">
            <h3>Experience (Years)</h3>
          </label>
          <input
            id="experience"
            type="number"
            value={formData.exp}
            onChange={(e) => handleInputChange("exp", e.target.value)}
            placeholder="e.g., 1"
            min="0"
            step="0.5"
          />
          {errors.exp && (
            <span className="error-text">{errors.exp}</span>
          )}
        </div>

        {/* Dynamic Skills */}
        <div className="skills-section">
          <h3>Skills *</h3>
          {errors.skills && (
            <span className="error-text">{errors.skills}</span>
          )}
          <div className="skills-list">
            {skills.map((skill, index) => (
              <div className="skill-field" key={index}>
                <input
                  type="text"
                  className="skill-in"
                  value={skill}
                  onChange={(e) => handleSkillChange(index, e.target.value)}
                  placeholder={`Skill ${index + 1} (e.g., Python, React)`}
                />
                {skills.length > 1 && (
                  <button
                    type="button"
                    className="delete-skill"
                    onClick={() => delSkill(index)}
                  >
                    Delete
                  </button>
                )}
              </div>
            ))}
          </div>
          <button
            type="button"
            className="add-btn"
            onClick={addSkill}
          >
            Add Skill
          </button>
        </div>

        {/* Submit Button */}
        <button
          type="submit"
          className="predict-btn"
          disabled={loading}
        >
          {loading ? (
            <>
              <span className="spinner"></span>
              Predicting...
            </>
          ) : (
            "Predict Job Role"
          )}
        </button>

        {/* Required Fields Notice */}
        <p className="required-notice">
          <span className="asterisk">*</span> Required fields
        </p>
      </form>

      {/* PREDICTION RESULT */}
      {predictedCategory && (
        <div className="prediction-result">
          <div className="prediction-card">
            <h3>Predicted Job Category</h3>
            <div className="predicted-category">{predictedCategory}</div>
            <p>Based on your skills and experience, we recommend exploring {predictedCategory} roles.</p>
            
            {/* GET JOB ROLES BUTTON */}
            <button
              type="button"
              className="get-jobs-btn"
              onClick={handleGetJobs}
              disabled={jobsLoading}
            >
              {jobsLoading ? (
                <>
                  <span className="spinner"></span>
                  Loading Jobs...
                </>
              ) : (
                "Get Job Roles"
              )}
            </button>

            {/* RESET BUTTON */}
            <button
              type="button"
              className="reset-btn"
              onClick={resetForm}
            >
              Make Another Prediction
            </button>
          </div>
        </div>
      )}

      {/* JOBS DISPLAY WITH FILTERS */}
      {showJobs && (
        <div className="jobs-section">
          <div className="jobs-header">
            <h2>
              Available {predictedCategory} Jobs
              <span className="jobs-count">
                ({filteredJobs.length} of {allCategoryJobs.length})
              </span>
            </h2>
          </div>
          
          {errors.jobs && (
            <div className="error-banner">{errors.jobs}</div>
          )}

          {/* FILTERS SECTION */}
          {allCategoryJobs.length > 0 && (
            <div className="jobs-filters">
              <div className="filter-group">
                <label>Search:</label>
                <input
                  type="text"
                  placeholder="Search jobs..."
                  value={filters.search}
                  onChange={(e) => handleFilterChange({ ...filters, search: e.target.value })}
                  className="filter-input"
                />
              </div>
              
              <div className="filter-group">
                <label>Location:</label>
                <select
                  value={filters.location}
                  onChange={(e) => handleFilterChange({ ...filters, location: e.target.value })}
                  className="filter-select"
                >
                  {filterOptions.locations.map(location => (
                    <option key={location} value={location}>
                      {location === 'all' ? 'All Locations' : location}
                    </option>
                  ))}
                </select>
              </div>
              
              <div className="filter-group">
                <label>Company:</label>
                <select
                  value={filters.company}
                  onChange={(e) => handleFilterChange({ ...filters, company: e.target.value })}
                  className="filter-select"
                >
                  {filterOptions.companies.map(company => (
                    <option key={company} value={company}>
                      {company === 'all' ? 'All Companies' : company}
                    </option>
                  ))}
                </select>
              </div>

              <button
                onClick={() => handleFilterChange({
                  location: 'all',
                  company: 'all',
                  search: ''
                })}
                className="clear-filters-btn"
              >
                Clear Filters
              </button>
            </div>
          )}

          {jobsLoading ? (
            <div className="loading-jobs">
              <div className="spinner"></div>
              Loading job listings...
            </div>
          ) : filteredJobs.length > 0 ? (
            <div className="jobs-grid">
              {filteredJobs.map(job => (
                <JobCard key={job.id} job={job} />
              ))}
            </div>
          ) : allCategoryJobs.length === 0 ? (
            <div className="no-jobs">
              <div className="empty-icon">📭</div>
              <h3>No jobs found</h3>
              <p>Try scraping some jobs first or check back later for new listings.</p>
            </div>
          ) : (
            <div className="no-jobs">
              <h3>No matching jobs found</h3>
              <p>Try adjusting your filters to see more results.</p>
              <button 
                onClick={() => handleFilterChange({
                  location: 'all',
                  company: 'all',
                  search: ''
                })} 
                className="clear-filters-prompt"
              >
                Clear all filters
              </button>
            </div>
          )}
        </div>

        
      )}
      <button onClick={LoadMore()} className="load-more">Load More Jobs</button>
    </div>
  );
}

export default Rform;