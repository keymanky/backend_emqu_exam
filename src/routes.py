from flask import Blueprint
from src.controllers.user_controller import users
from src.controllers.computer_controller import computers
from src.controllers.ping_controller import pings

# main blueprint to be registered with application
api = Blueprint('api', __name__)

# register user with api blueprint
api.register_blueprint(users, url_prefix="/users")

# register user with api blueprint
api.register_blueprint(computers, url_prefix="/computers")

# register user with api blueprint
api.register_blueprint(pings, url_prefix="/pings")