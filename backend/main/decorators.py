from flask import request, jsonify, g
from functools import wraps
from backend.main.crud.users_crud import UserCore


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        access_token = request.headers.get("Access-Token")
        user = UserCore().get_user_by_access_token(access_token)
        if not user:
            return jsonify({"response": "Not authorized"}), 401
        
        g.user = user
        return f(*args, **kwargs)
        
    return decorated_function