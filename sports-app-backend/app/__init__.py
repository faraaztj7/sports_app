from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api
from .config import Config
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
api = Api(
    title='Sports API',
    version='1.0',
    description='API for listing football teams, competitions, matches, players, and areas',
)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    CORS(app, resources={r"/*": {"origins": "*"}}) # Allow all origins

    from .routes import matches, teams, players, areas, competitions
    api.add_namespace(teams.api, path='/teams')
    api.add_namespace(players.api, path='/players')
    api.add_namespace(areas.api, path='/areas')
    api.add_namespace(competitions.api, path='/competitions')
    api.add_namespace(matches.api, path='/matches')


    return app
