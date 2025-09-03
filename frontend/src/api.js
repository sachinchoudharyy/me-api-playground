import axios from "axios";

// Change this URL when deployed
const API_URL = "http://127.0.0.1:5000";

export const getProfile = () => axios.get(`${API_URL}/profile`);
export const getProjects = (skill) =>
  axios.get(`${API_URL}/projects`, { params: { skill } });
export const search = (query) =>
  axios.get(`${API_URL}/search`, { params: { q: query } });
