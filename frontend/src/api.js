import axios from "axios";
import { ACCESS_TOKEN } from "./constants";

const api = axios.create({
  baseURL: "http://localhost:8000/",
  headers: {
    "Content-Type": "application/json",
  },
});

api.interceptors.request.use(
  (config) => {
    if (config.url.includes('/register') || config.url.includes('/login')) {
      return config;
    }
    
    const token = localStorage.getItem(ACCESS_TOKEN);
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

export const jobAPI = {
  // Get all jobs with pagination
  getJobs: (page = 1, pageSize = 100, filters = {}) => 
    api.get('/jobs/', { 
      params: { 
        page, 
        page_size: pageSize,
        ...filters
      } 
    }),
  
  // Get specific job
  getJob: (id) => api.get(`/jobs/${id}/`),
  
  // Scrape new jobs with advanced options
  scrapeJobs: (scrapingConfig) => 
    api.post('/jobs/scrape_jobs/', scrapingConfig),
  
  // Get job image
  getJobImage: (id) => api.get(`/jobs/${id}/get_image/`),
  
  // Session management
  getSessions: () => api.get('/jobs/sessions/'),
  deleteSession: (sessionId) => api.delete(`/jobs/sessions/${sessionId}/`),
  
  // Filter options
  getFilterOptions: () => api.get('/jobs/filter_options/'),
};

export default api;