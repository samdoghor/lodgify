# imports
from flask import Blueprint, Flask
from flask_migrate import Migrate
from flask_restful import Api

import config
import routes
from models import db

# configurations
# app
server = Flask(__name__)
server.debug = config.DEBUG
server.config['SECRET_KEY'] = config.SECRET_KEY

# database
server.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS  # noqa
db.init_app(server)
db.app = server
migrate = Migrate(server, db)
api = Api(server)

# blueprints
for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        server.register_blueprint(
            blueprint, url_prefix=config.APPLICATION_ROOT)

if __name__ == "__main__":
    server.debug = config.DEBUG
    server.run(host=config.HOST, port=config.PORT)
