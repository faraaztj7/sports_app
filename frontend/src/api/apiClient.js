// src/api/apiClient.js
const BASE_URL = import.meta.env.VITE_BACKEND_URL || 'http://localhost:5000';

// Fetch matches with optional filters (team, location, etc.)
export async function fetchMatches(filters = {}) {
  const queryParams = new URLSearchParams(filters).toString();
  const response = await fetch(`${BASE_URL}/matches?${queryParams}`);
  return response.json();
}

// Fetch a list of teams
export async function fetchTeams() {
  const response = await fetch(`${BASE_URL}/teams`);
  return response.json();
}

// Fetch players with optional team filter
export async function fetchPlayers(teamId) {
  const response = await fetch(`${BASE_URL}/players?team_id=${teamId}`);
  return response.json();
}
