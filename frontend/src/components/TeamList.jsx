import React, { useEffect, useState } from 'react';
import apiClient from '../api';

function TeamList({ onSelectTeam }) {
  const [teams, setTeams] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchTeams = async () => {
      try {
        const response = await apiClient.get('/teams');
        setTeams(response.data);
      } catch (error) {
        console.error('Error fetching teams:', error);
        setError('Could not load teams.');
      }
    };

    fetchTeams();
  }, []);

  if (error) {
    return <div className="alert alert-danger">{error}</div>;
  }

  return (
    <div className="mb-3">
      {/* <label>Teams:</label> */}
      <select
        onChange={(e) => {
          const selectedTeamName = e.target.value;
          onSelectTeam(selectedTeamName); // Pass only the team name
        }}
        className="form-select"
      >
        <option value="">Select a team</option>
        {teams.map(team => (
          <option key={team.id} value={team.name}>
            {team.name}
          </option>
        ))}
      </select>
    </div>
  );
}

export default TeamList;
