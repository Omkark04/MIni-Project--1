import React, { useState, useEffect, useCallback } from "react";
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
  const [errors, setErrors] = useState({});

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

    try {
      const validSkills = skills.filter((skill) => skill.trim() !== "");
      
      const res = await api.post("api/rform-data/", {
        ...formData,
        skills: validSkills,
      });

      if (res.data.status) {
        alert("✅ Success: " + res.data.message);
        
        // Reset form
        setFormData({
          name: "",
          location: "",
          education: "",
          exp: "",
        });
        setSkills([""]);
      } else {
        setErrors({ submit: res.data.errors || "Registration failed" });
      }
    } catch (error) {
      const errorMessage =
        error.response?.data?.message || "❌ An error occurred. Please try again.";
      setErrors({ submit: errorMessage });
    } finally {
      setLoading(false);
    }
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
            aria-invalid={errors.name ? "true" : "false"}
            aria-describedby={errors.name ? "name-error" : undefined}
          />
          {errors.name && (
            <span id="name-error" className="error-text" role="alert">
              {errors.name}
            </span>
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
            aria-invalid={errors.exp ? "true" : "false"}
            aria-describedby={errors.exp ? "exp-error" : undefined}
          />
          {errors.exp && (
            <span id="exp-error" className="error-text" role="alert">
              {errors.exp}
            </span>
          )}
        </div>

        {/* Dynamic Skills */}
        <div className="skills-section">
          <h3>Skills *</h3>
          {errors.skills && (
            <span className="error-text" role="alert">
              {errors.skills}
            </span>
          )}
          <div className="skills-list">
            {skills.map((skill, index) => (
              <div className="skill-field" key={index}>
                <input
                  type="text"
                  value={skill}
                  onChange={(e) => handleSkillChange(index, e.target.value)}
                  placeholder={`Skill ${index + 1} (e.g., Python, React)`}
                  aria-label={`Skill ${index + 1}`}
                />
                {skills.length > 1 && (
                  <button
                    type="button"
                    className="delete-skill"
                    onClick={() => delSkill(index)}
                    aria-label={`Delete skill ${index + 1}`}
                    title="Remove this skill"
                  >Delete
                  </button>
                )}
              </div>
            ))}
          </div>
          <button
            type="button"
            className="add-btn"
            onClick={addSkill}
            aria-label="Add another skill"
          >
            Add Skill
          </button>
        </div>

        {/* Submit Button */}
        <button
          type="submit"
          className="predict-btn"
          disabled={loading}
          aria-busy={loading}
        >
          {loading ? (
            <>
              <span className="spinner"></span>
              Processing...
            </>
          ) : (
            <>
              Predict Job Role
            </>
          )}
        </button>

        {/* Required Fields Notice */}
        <p className="required-notice">
          <span className="asterisk">*</span> Required fields
        </p>
      </form>
    </div>
  );
}

export default Rform;