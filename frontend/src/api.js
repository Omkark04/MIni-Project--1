import axios from "axios";
import { ACCESS_TOKEN } from "./constants";

const api = axios.create({
  baseURL: "http://localhost:8000/",
  headers: {
    "Content-Type": "application/json",
  },
});

// Modified interceptor to exclude auth header for registration/login
api.interceptors.request.use(
  (config) => {
    // Skip adding token for these endpoints
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
  getJobs: (page = 1, pageSize = 100) => 
    api.get('/jobs/', { params: { page, page_size: pageSize } }),
  
  // Get specific job
  getJob: (id) => api.get(`/jobs/${id}/`),
  
  // Scrape new jobs
  scrapeJobs: (keywords, location) => 
    api.post('/jobs/scrape_jobs/', { keywords, location }),
  
  // Get job image
  getJobImage: (id) => api.get(`/jobs/${id}/get_image/`),
};

export default api;