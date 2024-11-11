import React, { useEffect, useState } from 'react';
import apiClient from '../api';

function PlayerList({ onSelectPlayer }) {
  const [players, setPlayers] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchPlayers = async () => {
      try {
        const response = await apiClient.get('/players');
        setPlayers(response.data); // Ensure players are set correctly
      } catch (error) {
        console.error('Error fetching players:', error);
        setError('Could not load players.');
      }
    };

    fetchPlayers();
  }, []);

  if (error) {
    return <div className="alert alert-danger">{error}</div>;
  }

  return (
    <div className="mb-3">
      {/* <label>Players:</label> */}
      <select onChange={(e) => onSelectPlayer(e.target.value)} className="form-select">
        <option value="">Select a player</option>
        {players.map(player => (
          <option key={player.id} value={player.name}>
            {player.name}
          </option>
        ))}
      </select>
    </div>
  );
}

export default PlayerList;
