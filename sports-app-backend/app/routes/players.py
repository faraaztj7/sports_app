from flask_restx import Namespace, Resource, fields
from app import db
from app.models import Player, Team

api = Namespace('Players', description='Players Operations - Create or View Players')

# Model for GET responses
player_model = api.model('Player', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a player'),
    'name': fields.String(required=True, description='Player name'),
    'position': fields.String(required=True, description='Player position'),
    'team': fields.String(attribute=lambda x: x.team.name),  # Using 'team' name for GET responses
})

# Model for POST requests
player_creation_model = api.model('PlayerCreation', {
    'name': fields.String(required=True, description='Player name'),
    'position': fields.String(required=True, description='Player position'),
    'team_id': fields.Integer(required=True, description='ID of the team')  # Using 'team_id' for POST
})

@api.route('/')
class PlayerList(Resource):
    @api.doc('list_players')
    @api.marshal_list_with(player_model)
    def get(self):
        """List all players"""
        players = Player.query.all()
        return players

    @api.doc('create_player')
    @api.expect(player_creation_model, validate=True)
    @api.marshal_with(player_model, code=201)
    def post(self):
        """Create a new player"""
        data = api.payload
        team_id = data.get('team_id')
        if not team_id:
            api.abort(400, "team_id is required.")

        # Retrieve the team by ID
        team = Team.query.get(team_id)
        if not team:
            api.abort(400, "Team does not exist.")

        new_player = Player(name=data['name'], position=data['position'], team=team)
        db.session.add(new_player)
        db.session.commit()
        return new_player, 201

@api.route('/<int:id>')
@api.response(404, 'Player not found')
@api.param('id', 'The player identifier')
class PlayerResource(Resource):
    @api.doc('get_player')
    @api.marshal_with(player_model)
    def get(self, id):
        """Fetch a player given its identifier"""
        player = Player.query.get_or_404(id)
        return player
