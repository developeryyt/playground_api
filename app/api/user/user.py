from flask import Blueprint, request, jsonify

check_auth = Blueprint('user', __name__)

@check_auth.route('/check', methods=['GET'])
def check_def():
    return 'JUST CHECKING'


@check_auth.route('/auth', methods=['POST'])
def get_auth():
    req_data = request.get_json()
    return jsonify({
        "name" : req_data['username']
    })

