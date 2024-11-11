import React, { useState } from 'react';
import MatchList from './components/MatchList';
import TeamList from './components/TeamList';
import PlayerList from './components/PlayerList';
import './App.css';


function App() {
  const [location, setLocation] = useState('');
  const [team, setTeam] = useState(''); // Holds team name as a string
  const [player, setPlayer] = useState('');

  return (
    <div className="app-container">
      <h1>Sports App</h1>

      {/* Filters Container */}
      <div className="filters">
        {/* Location Filter */}
        <div className="filter-item">
          <label>Area (Location):</label>
          <input
            type="text"
            value={location}
            onChange={(e) => setLocation(e.target.value)}
            placeholder="Enter location"
          />
        </div>

        {/* Team Filter */}
        <div className="filter-item">
          <label>Teams:</label>
          <TeamList onSelectTeam={setTeam} />
        </div>

        {/* Player Filter */}
        <div className="filter-item">
          <label>Players:</label>
          <PlayerList onSelectPlayer={setPlayer} />
        </div>
      </div>

      {/* Match List */}
      <MatchList location={location} teams={team} player={player} />
    </div>
  );
}

export default App;
