from flask import request, redirect, url_for
from functools import wraps
from backend.main.crud.users_crud import UserCore
import datetime


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        access_token = request.headers.get("Access-Token")
        token_expire_date = UserCore().get_acctoken_expdate_by_acctoken(access_token)
        if not access_token or token_expire_date <= datetime.datetime.now():
            return redirect(url_for("http://127.0.0.1:5500/frontend/login/login.html"))

        return f(*args, **kwargs)
        
    return decorated_function