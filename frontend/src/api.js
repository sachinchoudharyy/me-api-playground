import axios from "axios";

const API_URL = "http://127.0.0.1:5000"; // local dev

export const getProfile = () => axios.get(`${API_URL}/profile`);
export const getProjects = (skill) =>
  axios.get(`${API_URL}/projects`, { params: { skill } });
export const getSkills = () => axios.get(`${API_URL}/skills`);      // <- works even if UI used /skills/top
export const search = (q) => axios.get(`${API_URL}/search`, { params: { q } });
