from flask import request, g, redirect, url_for
from functools import wraps


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        access_token = request.headers.get("Access-Token")
        if not access_token:
            return redirect(url_for("http://127.0.0.1:5500/frontend/login/login.html"))
        return f(*args, **kwargs)
    return decorated_function