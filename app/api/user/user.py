from flask import Blueprint, request, jsonify

check_auth = Blueprint('user', __name__)

@check_auth.route('/auth', methods=['GET'])
def get_auth():
    return jsonify({
        "name" : "patrick"
    })