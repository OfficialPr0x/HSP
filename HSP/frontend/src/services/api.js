import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:5000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export async function generateGuide(scopeUrl) {
  try {
    const response = await api.post('/guide/generate', { scope_url: scopeUrl });
    return response.data;
  } catch (error) {
    console.error('Error generating guide:', error);
    throw new Error('Failed to generate guide');
  }
}

export async function getAIInsights(scopeUrl) {
  try {
    const response = await api.post('/guide/insights', { scope_url: scopeUrl });
    return response.data;
  } catch (error) {
    console.error('Error getting AI insights:', error);
    throw new Error('Failed to get AI insights');
  }
}