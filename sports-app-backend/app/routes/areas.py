from flask_restx import Namespace, Resource, fields
from app import db
from app.models import Area

api = Namespace('Areas', description='Areas Operations - Create or View Areas (Location)')

# Model for GET (with id field)
area_model_get = api.model('AreaGet', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of an area'),
    'name': fields.String(required=True, description='Area name'),
})

# Model for POST (without id field)
area_model_post = api.model('AreaPost', {
    'name': fields.String(required=True, description='Area name'),
})

@api.route('/')
class AreaList(Resource):
    @api.doc('list_areas')
    @api.marshal_list_with(area_model_get)
    def get(self):
        """List all areas"""
        areas = Area.query.all()
        return areas

    @api.doc('create_area')
    @api.expect(area_model_post, validate=True)  # Use area_model_post for POST requests
    @api.marshal_with(area_model_get, code=201)   # Use area_model_get for the response
    def post(self):
        """Create a new area"""
        data = api.payload
        new_area = Area(name=data['name'])
        db.session.add(new_area)
        db.session.commit()
        return new_area, 201

@api.route('/<int:id>')
@api.response(404, 'Area not found')
@api.param('id', 'The area identifier')
class AreaResource(Resource):
    @api.doc('get_area')
    @api.marshal_with(area_model_get)
    def get(self, id):
        """Fetch an area given its identifier"""
        area = Area.query.get_or_404(id)
        return area
