from flask_restx import Namespace, Resource, fields
from flask import request
from app import db
from app.models import Team

api = Namespace('Teams', description='Teams Operations - Create or View Teams')

# Model for GET (with id field)
team_model_get = api.model('TeamGet', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a team'),
    'name': fields.String(required=True, description='Team name'),
    'city': fields.String(required=True, description='City of the team'),
})

# Model for POST (without id field)
team_model_post = api.model('TeamPost', {
    'name': fields.String(required=True, description='Team name'),
    'city': fields.String(required=True, description='City of the team'),
})

@api.route('/')
class TeamList(Resource):
    @api.doc('list_teams')
    @api.marshal_list_with(team_model_get)
    def get(self):
        """List all teams, with optional filtering by name or city"""
        name = request.args.get('name')  # Filter by team name
        city = request.args.get('city')  # Filter by city

        query = Team.query

        # Filter by team name if provided
        if name:
            query = query.filter(Team.name.ilike(f'%{name}%'))

        # Filter by city if provided
        if city:
            query = query.filter(Team.city.ilike(f'%{city}%'))

        teams = query.all()
        return teams

    @api.doc('create_team')
    @api.expect(team_model_post, validate=True)  # Use team_model_post for POST requests
    @api.marshal_with(team_model_get, code=201)   # Use team_model_get for the response
    def post(self):
        """Create a new team"""
        data = api.payload
        new_team = Team(name=data['name'], city=data['city'])
        db.session.add(new_team)
        db.session.commit()
        return new_team, 201

@api.route('/<int:id>')
@api.response(404, 'Team not found')
@api.param('id', 'The team identifier')
class TeamResource(Resource):
    @api.doc('get_team')
    @api.marshal_with(team_model_get)
    def get(self, id):
        """Fetch a team given its identifier"""
        team = Team.query.get_or_404(id)
        return team
