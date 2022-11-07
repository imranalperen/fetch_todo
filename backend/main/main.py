from flask import(
    Blueprint,
    request,
    jsonify
)
from backend.main.decorators import login_required
from backend.main.utils import (
    db_email_control,
    db_insert_user,
)

main = Blueprint("mian", __name__, url_prefix="/api")

@main.route("signup", methods=["POST"])
def signup():
    signup_form = request.json  #{'email': 'qwe', 'password': 'qwe', 'verify_password': 'qwe'}
    if signup_form["password"] == signup_form["verify_password"]:
        email = signup_form["email"]
        password = signup_form["password"]
        if not db_email_control(email):
            db_insert_user(email, password)
            return jsonify({"response": "success"})
    
    return jsonify({"response": "Error"}), 401


@main.route("login", methods=["POST"])
def login():
    login_form = request.json
    email = login_form["email"]
    password = login_form["password"]

@main.route("index", methods=["POST"])
def index():
    pass