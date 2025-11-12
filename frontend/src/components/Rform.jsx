import React, { useState, useCallback } from "react";
import "../styles/Rform.css";
import api from "../api";

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
      setCategoryJobs(Array.isArray(jobs) ? jobs : []);
      
    } catch (error) {
      const errorMessage =
        error.response?.data?.message || "Error fetching jobs";
      setErrors({ jobs: errorMessage });
    } finally {
      setJobsLoading(false);
    }
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
    setShowJobs(false);
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

  return (
    <div className="form-container">
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

      {/* JOBS DISPLAY */}
      {showJobs && (
        <div className="jobs-section">
          <h3>Available {predictedCategory} Jobs</h3>
          
          {errors.jobs && (
            <div className="error-banner">{errors.jobs}</div>
          )}

          {jobsLoading ? (
            <div className="loading-jobs">Loading job listings...</div>
          ) : categoryJobs.length > 0 ? (
            <div className="jobs-list">
              <p className="jobs-count">Found {categoryJobs.length} jobs in {predictedCategory}</p>
              
              {categoryJobs.map((job, index) => (
                <div key={job.id || index} className="job-card">
                  <div className="job-header">
                    <h4 className="job-title">{job.title}</h4>
                    <span className="job-company">{job.company}</span>
                  </div>
                  <div className="job-details">
                    <span className="job-location">📍 {job.location}</span>
                  </div>
                  {job.job_link && (
                    <a 
                      href={job.job_link} 
                      target="_blank" 
                      rel="noopener noreferrer"
                      className="job-link"
                    >
                      View Job Details →
                    </a>
                  )}
                </div>
              ))}
            </div>
          ) : (
            <div className="no-jobs">
              <p>No jobs found for {predictedCategory} category.</p>
              <p>Try scraping some jobs first or check back later.</p>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default Rform;