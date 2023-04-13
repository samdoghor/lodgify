# imports
from flask import Blueprint, Flask, jsonify
from flask_migrate import Migrate
from flask_restful import Api
from flasgger import Swagger

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
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS
db.init_app(server)
db.app = server
migrate = Migrate(server, db)
api = Api(server)

# blueprints
for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        server.register_blueprint(
            blueprint, url_prefix=config.APPLICATION_ROOT)

# swagger
server.config["SWAGGER"] = {
    "swagger_version": "2.0",
    "title": "Lodgify API",
    'uiversion': 3,
    "static_url_path": "/api-documentation",
    'openapi': '3.0.0'
}
Swagger(server)


# errors handling
# error handler for 400


@server.errorhandler(400)
def bad_request(error):
    print({"error": error})
    return jsonify({
        "success": False,
        "error": 400,
        "message": error.description
    }), 400

# error handler for 401


@server.errorhandler(401)
def unauthorized(error):
    print({"error": error})
    return jsonify({
        "success": False,
        "error": 401,
        "message": error.description
    }), 401

# error handler for 403


@server.errorhandler(403)
def forbidden(error):
    print({"error": error})
    return jsonify({
        "success": False,
        "error": 403,
        "message": error.description
    }), 403

# error handler for 404


@server.errorhandler(404)
def not_found(error):
    print({"error": error})
    return jsonify({
        "success": False,
        "error": 404,
        "message": error.description
    }), 404


@server.errorhandler(405)
def method_not_allowed(error):
    print({"error": error})
    return jsonify({
        "success": False,
        "error": 405,
        "message": error.description
    }), 405

# error handler for 422


@server.errorhandler(422)
def unprocessable(error):
    print({"error": error})
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422

# error handler for 500


@server.errorhandler(500)
def internal_server_error(error):
    print({"error": error})
    return jsonify({
        "success": False,
        "error": 500,
        "message": "Internal server error"
    }), 500


if __name__ == "__main__":
    server.debug = config.DEBUG
    server.run(host=config.HOST, port=config.PORT)
