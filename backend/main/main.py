from flask import(
    Blueprint,
    request,
    jsonify
)
from backend.main.decorators import login_required
from backend.main.crud.users_crud import UserCore

main = Blueprint("mian", __name__, url_prefix="/api")

@main.route("signup", methods=["POST"])
def signup():
    signup_form = request.json
    if signup_form["password"] == signup_form["verify_password"]:
        email = signup_form["email"]
        password = signup_form["password"]
        if UserCore().register(email, password):
            return jsonify({"response": "success"})
        
    return jsonify({"response": "Error"}), 401


@main.route("login", methods=["POST"])
def login():
    login_form = request.json
    email = login_form["email"]
    password = login_form["password"]
    if UserCore().login(email, password):
        return jsonify({"response": "success"})
    
    return jsonify({"response": "fail"}), 401


@main.route("index", methods=["POST"])
def index():
    pass