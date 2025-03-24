from flask import Blueprint
from .user import user

api_init = Blueprint('api', __name__, url_prefix='/api')
api_init.register_blueprint(user.check_auth, url_prefix='/user')