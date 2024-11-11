from flask import request
from flask_restx import Namespace, Resource, fields
from app import db
from app.models import Match, Team, Competition, Area, Player
from datetime import datetime

api = Namespace('Matches', description='Matches Operations - Create or View Matches')

# Model for displaying match data
match_model = api.model('Match', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a match'),
    'date': fields.DateTime(required=True, description='Date and time of the match'),
    'home_team': fields.String(attribute=lambda x: x.home_team.name),
    'away_team': fields.String(attribute=lambda x: x.away_team.name),
    'competition': fields.String(attribute=lambda x: x.competition.name),
    'area': fields.String(attribute=lambda x: x.area.name),
})

# Model for creating new match data
match_creation_model = api.model('MatchCreation', {
    'date': fields.String(required=True, description='Date and time of the match in ISO 8601 format'),
    'home_team_id': fields.Integer(required=True, description='ID of the home team'),
    'away_team_id': fields.Integer(required=True, description='ID of the away team'),
    'competition_id': fields.Integer(required=True, description='ID of the competition'),
    'area_id': fields.Integer(required=True, description='ID of the area'),
})

@api.route('/')
class MatchList(Resource):
    @api.doc('list_matches', 
             params={
                 'date': 'Date and time of the match in ISO 8601 format (YYYY-MM-DDTHH:MM:SS or YYYY-MM-DD)',
                 'location': 'Location (area) where the match takes place',
                 'team': 'Team name to filter by (home or away)',
                 'player': 'Player name to filter by (player is part of the team)'
             })
    @api.marshal_list_with(match_model)
    def get(self):
        """List all matches with optional filtering by date, location, team, or player"""
        date = request.args.get('date')
        location = request.args.get('location')
        team = request.args.get('team')
        player_name = request.args.get('player')

        query = Match.query

        # Filter by date
        if date:
            try:
                try:
                    date_obj = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
                except ValueError:
                    date_obj = datetime.strptime(date, '%Y-%m-%d')
                query = query.filter(Match.date == date_obj)
            except ValueError:
                api.abort(400, "Invalid date format. Use YYYY-MM-DDTHH:MM:SS or YYYY-MM-DD.")

        # Filter by location (area)
        if location:
            query = query.join(Area).filter(Area.name.ilike(f'%{location}%'))

        # Filter by team (home or away)
        if team:
            query = query.filter(
                (Match.home_team.has(Team.name.ilike(f'%{team}%'))) | 
                (Match.away_team.has(Team.name.ilike(f'%{team}%')))
            )

        # Filter by player
        if player_name:
            player = Player.query.filter_by(name=player_name).first()
            if player:
                query = query.filter(
                    (Match.home_team_id == player.team_id) | (Match.away_team_id == player.team_id)
                )
            else:
                api.abort(404, f"Player with name {player_name} not found.")

        matches = query.all()
        return matches

    @api.expect(match_creation_model, validate=True)
    @api.marshal_with(match_model, code=201)
    def post(self):
        """Create a new match"""
        data = request.json
        
        # Parse the date and validate format (ISO 8601)
        try:
            try:
                date = datetime.strptime(data['date'], '%Y-%m-%dT%H:%M:%S')
            except ValueError:
                date = datetime.strptime(data['date'], '%Y-%m-%d')
        except ValueError:
            api.abort(400, "Invalid date format. Use YYYY-MM-DDTHH:MM:SS or YYYY-MM-DD.")

        # Validate existence of foreign key references by ID
        home_team = db.session.get(Team, data['home_team_id'])
        away_team = db.session.get(Team, data['away_team_id'])
        competition = db.session.get(Competition, data['competition_id'])
        area = db.session.get(Area, data['area_id'])
        # area = Area.query.get(data['area_id'])

        if not home_team:
            api.abort(400, "Home team with the given ID does not exist.")
        if not away_team:
            api.abort(400, "Away team with the given ID does not exist.")
        if not competition:
            api.abort(400, "Competition with the given ID does not exist.")
        if not area:
            api.abort(400, "Area with the given ID does not exist.")

        # Create new Match object with IDs
        new_match = Match(
            date=date,
            home_team_id=data['home_team_id'],
            away_team_id=data['away_team_id'],
            competition_id=data['competition_id'],
            area_id=data['area_id']
        )

        db.session.add(new_match)
        db.session.commit()
        return new_match, 201
