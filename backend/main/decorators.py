from flask import jsonify, request, g
from functools import wraps
from backend.main.utils import get_access_token


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        access_token = request.headers["Access-Token"]
        if not get_access_token(access_token):
            return jsonify({"response":"error"}), 400
        return f(*args, **kwargs)
    return decorated_function