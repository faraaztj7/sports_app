import React, { useEffect, useState } from 'react';
import apiClient from '../api';

function MatchList({ location, teams, player }) {
  const [matches, setMatches] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchMatches = async () => {
      setLoading(true);
      try {
        let url = '/matches';
        const params = [];
        if (location) params.push(`location=${location}`);
        if (teams) params.push(`team=${teams}`);  // Update this `team` for single team filtering
        if (player) params.push(`player=${player}`);

        if (params.length > 0) {
          url += `?${params.join('&')}`;
        }

        const response = await apiClient.get(url);
        setMatches(response.data);
      } catch (err) {
        console.error('Error fetching matches:', err);
        setError('Failed to fetch matches. Please try again later.');
      } finally {
        setLoading(false);
      }
    };

    fetchMatches();
  }, [location, teams, player]);  // Re-fetch when these values change

  return (
    <div>
      <h2>Matches</h2>
      {loading ? (
        <p>Loading...</p>
      ) : error ? (
        <p>{error}</p>
      ) : matches.length === 0 ? (
        <p>No matches available for the selected filters.</p>
      ) : (
        <table className="table table-bordered">
          <thead>
            <tr>
              <th>Date</th>
              <th>Home Team</th>
              <th>Away Team</th>
              <th>Competition</th>
              <th>Area (Location)</th>
            </tr>
          </thead>
          <tbody>
            {matches.map((match) => (
              <tr key={match.id}>
                <td>{new Date(match.date).toLocaleString()}</td>
                <td>{match.home_team}</td>
                <td>{match.away_team}</td>
                <td>{match.competition}</td>
                <td>{match.area}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default MatchList;
