# app/routes/competitions.py
from flask_restx import Namespace, Resource, fields
from app.models import Competition
from app import db

api = Namespace('Competitions', description='Football Competitions Operation - Create or View Compeitions')

# Define the competition model to be used in Swagger
competition_model = api.model('Competition', {
    'id': fields.Integer(description='The competition identifier'),
    'name': fields.String(required=True, description='The name of the competition'),
})

# Define the model for POST request payload
competition_post_model = api.model('CompetitionPost', {
    'name': fields.String(required=True, description='The name of the competition'),
})

@api.route('/')
class CompetitionList(Resource):
    
    @api.doc('Get list of all competitions')
    @api.marshal_with(competition_model, as_list=True)
    def get(self):
        """Get a list of all competitions"""
        competitions = Competition.query.all()
        return competitions

    @api.doc('Create a new competition')
    @api.expect(competition_post_model, validate=True)
    @api.marshal_with(competition_model, code=201)
    @api.response(400, 'Validation Error')
    def post(self):
        """Create a new competition"""
        data = api.payload
        competition = Competition(name=data['name'])
        db.session.add(competition)
        db.session.commit()
        return competition, 201
